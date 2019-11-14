import operator
from typing import Dict, List

from confluent_kafka.admin import ConfigResource

from esque.resources.resource import KafkaResource


class Broker(KafkaResource):
    def __init__(self, cluster, *, broker_id: int = None, host: str = None, port: int = None):
        self.cluster = cluster
        self.broker_id = broker_id
        self.host = host
        self.port = port

    @classmethod
    def from_id(cls, cluster, broker_id) -> "Broker":
        return cls(cluster=cluster, broker_id=broker_id)

    @classmethod
    def from_host(cls, cluster, host: str) -> "Broker":
        brokers = cluster.get_metadata().brokers.values()
        broker_to_return = None
        for broker in brokers:
            if broker.host == host:
                if not broker_to_return:
                    broker_to_return = cls(cluster, broker_id=broker.id, host=host, port=broker.port)
                else:
                    raise ValueError(
                        f"Broker host name {host} is not unique! Please provide with port number i.e. {host}:port."
                    )
        if not broker_to_return:
            raise ValueError(f"There is no broker with {host} as host name!")
        return broker_to_return

    @classmethod
    def from_host_and_port(cls, cluster, host: str, port: int) -> "Broker":
        brokers = cluster.get_metadata().brokers.values()
        for broker in brokers:
            if broker.host == host and broker.port == port:
                return cls(cluster, broker_id=broker.id, host=host, port=port)

    @classmethod
    def from_attributes(cls, cluster, broker_id: int, host: str, port: int) -> "Broker":
        return cls(cluster, broker_id=broker_id, host=host, port=port)

    @classmethod
    def get_all(cls, cluster) -> List["Broker"]:
        metadata = cluster.get_metadata().brokers.values()
        brokers = [
            cls.from_attributes(cluster, broker_id=broker.id, host=broker.host, port=broker.port) for broker in metadata
        ]
        return sorted(brokers, key=operator.attrgetter("broker_id"))

    def describe(self) -> Dict:
        return self.cluster.retrieve_config(ConfigResource.Type.BROKER, self.broker_id)

    def as_dict(self):
        return {"cluster": self.cluster, "broker_id": self.broker_id, "host": self.host, "port": self.port}
