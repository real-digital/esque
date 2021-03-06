import random
import string
from typing import List, Tuple
from unittest import mock

import pytest
from click.testing import CliRunner
from confluent_kafka.cimpl import Producer as ConfluentProducer

from esque.config import Config
from esque.messages.message import KafkaMessage, MessageHeader


@pytest.fixture()
def interactive_cli_runner(mocker: mock, unittest_config: Config) -> CliRunner:
    mocker.patch("esque.cli.helpers._isatty", return_value=True)
    mocker.patch("esque.cli.environment.ESQUE_VERBOSE", new_callable=mock.PropertyMock, return_value="1")
    return CliRunner()


@pytest.fixture()
def non_interactive_cli_runner(mocker: mock, unittest_config: Config) -> CliRunner:
    mocker.patch("esque.cli.helpers._isatty", return_value=False)
    mocker.patch("esque.cli.environment.ESQUE_VERBOSE", new_callable=mock.PropertyMock, return_value="1")
    return CliRunner()


def produce_binary_test_messages(
    producer: ConfluentProducer, topic: Tuple[str, int], amount: int = 10
) -> List[KafkaMessage]:
    topic_name, num_partitions = topic
    messages = []
    for i in range(amount):
        partition = random.randrange(0, num_partitions)
        key = random_bytes()
        value = random_bytes()
        messages.append(KafkaMessage(key, value, partition))
        producer.produce(topic=topic_name, key=key, value=value, partition=partition)
    producer.flush()
    return messages


def random_bytes(length: int = 16) -> bytes:
    return random.getrandbits(length * 8).to_bytes(length, "big")


def produce_text_test_messages(
    producer: ConfluentProducer, topic: Tuple[str, int], amount: int = 10
) -> List[KafkaMessage]:
    topic_name, num_partitions = topic
    messages = []
    for i in range(amount):
        partition = random.randrange(0, num_partitions)
        key = random_str()
        value = random_str()
        messages.append(KafkaMessage(key, value, partition))
        producer.produce(topic=topic_name, key=key, value=value, partition=partition)
    producer.flush()
    return messages


def random_str(length: int = 16) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def produce_text_test_messages_with_headers(
    producer: ConfluentProducer, topic: Tuple[str, int], amount: int = 10
) -> List[KafkaMessage]:
    topic_name, num_partitions = topic
    messages = []
    for i in range(amount):
        partition = random.randrange(0, num_partitions)
        key = random_str()
        value = random_str()
        headers = [
            MessageHeader(random_str(4), random.choice((None, random_str(8)))) for _ in range(random.randrange(0, 4))
        ]
        messages.append(KafkaMessage(key, value, partition, headers=headers))
        producer.produce(topic=topic_name, key=key, value=value, partition=partition, headers=headers)
    producer.flush()
    return messages
