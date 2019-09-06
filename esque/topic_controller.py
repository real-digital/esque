import json
import re
from typing import Any, Dict, List, TYPE_CHECKING

import click
from confluent_kafka.admin import ConfigResource
from confluent_kafka.cimpl import NewTopic
from kazoo.exceptions import NodeExistsError

from esque.config import Config
from esque.errors import raise_for_kafka_exception
from esque.helpers import ensure_kafka_futures_done, invalidate_cache_after
from esque.topic import AttributeDiff, Topic

if TYPE_CHECKING:
    from esque.cluster import Cluster


class TopicController:
    def __init__(self, cluster: "Cluster", config: Config):
        self.cluster: "Cluster" = cluster
        self.config = config

    @raise_for_kafka_exception
    def list_topics(self, *, search_string: str = None, sort: bool = True, hide_internal: bool = True) -> List[Topic]:
        self.cluster.confluent_client.poll(timeout=1)
        topic_results = self.cluster.confluent_client.list_topics().topics.values()
        topic_names = [t.topic for t in topic_results]
        if search_string:
            topic_names = [topic for topic in topic_names if re.match(search_string, topic)]
        if hide_internal:
            topic_names = [topic for topic in topic_names if not topic.startswith("__")]
        if sort:
            topic_names = sorted(topic_names)

        topics = list(map(self.get_cluster_topic, topic_names))
        return topics

    @raise_for_kafka_exception
    @invalidate_cache_after
    def create_topics(self, topics: List[Topic]):
        for topic in topics:
            partitions = topic.num_partitions if topic.num_partitions is not None else self.config.default_partitions
            replicas = (
                topic.replication_factor
                if topic.replication_factor is not None
                else self.config.default_replication_factor
            )
            new_topic = NewTopic(
                topic.name, num_partitions=partitions, replication_factor=replicas, config=topic.config
            )
            future_list = self.cluster.confluent_client.create_topics([new_topic])
            ensure_kafka_futures_done(list(future_list.values()))

    @raise_for_kafka_exception
    @invalidate_cache_after
    def alter_configs(self, topics: List[Topic]):
        for topic in topics:
            config_resource = ConfigResource(ConfigResource.Type.TOPIC, topic.name, topic.config)
            future_list = self.cluster.confluent_client.alter_configs([config_resource])
            ensure_kafka_futures_done(list(future_list.values()))

    @raise_for_kafka_exception
    @invalidate_cache_after
    def delete_topic(self, topic: Topic):
        future = self.cluster.confluent_client.delete_topics([topic.name])[topic.name]
        ensure_kafka_futures_done([future])

    def get_cluster_topic(self, topic_name: str) -> Topic:
        """Convenience function getting an existing topic based on topic_name"""
        return self.update_from_cluster(Topic(topic_name))

    @raise_for_kafka_exception
    def update_from_cluster(self, topic: Topic):
        """Takes a topic and, based on its name, updates all attributes from the cluster"""
        if topic.is_only_local:  # only have to instantiate those once
            topic._pykafka_topic = self.cluster.pykafka_client.cluster.topics[topic.name]
            topic._confluent_topic = self.cluster.confluent_client.list_topics(topic=topic.name, timeout=10).topics

        # TODO put the topic instances into a cache of this class
        low_watermarks = topic._pykafka_topic.earliest_available_offsets()
        high_watermarks = topic._pykafka_topic.latest_available_offsets()
        topic.update_partitions(low_watermarks, high_watermarks)

        topic.config = self.cluster.retrieve_config(ConfigResource.Type.TOPIC, topic.name)
        topic.is_only_local = False
        return topic

    @raise_for_kafka_exception
    def diff_with_cluster(self, local_topic: Topic) -> Dict[str, AttributeDiff]:
        cluster_topic = self.get_cluster_topic(local_topic.name)
        return local_topic.diff_settings(cluster_topic)

    def execute_cluster_assignment(self, plan: Dict[str, List[Dict[str, Any]]]):
        with self.cluster.zookeeper_client as zk:
            reassignment_path = f"/admin/reassign_partitions"
            for partition in plan["partitions"]:
                click.echo(f"Reassigning {partition['topic']}")
            try:
                # TODO: Validate plan
                zk.create(reassignment_path, json.dumps(plan, sort_keys=True).encode(), makepath=True)
                click.echo("Reassigned partitions.")
            except NodeExistsError:
                click.echo("Previous plan still in progress..")
            except Exception as e:
                click.echo(f"Could not re-assign partitions. Error: {e}")