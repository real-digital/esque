# FIXME autogenerated module, check for errors!
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional

from esque.protocol.api.base import *
from esque.protocol.serializers import *


@dataclass
class Topics:
    # Name of topic
    topic: "str"  # STRING

    # List of partition ids of the topic.
    partitions: List["int"]  # INT32


@dataclass
class LogDirs:
    # The absolute log directory path.
    log_dir: "str"  # STRING

    topics: List["Topics"]


@dataclass
class AlterReplicaLogDirsRequestData(RequestData):
    log_dirs: List["LogDirs"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.ALTER_REPLICA_LOG_DIRS  # == 34


@dataclass
class Partitions:
    # Topic partition id
    partition: "int"  # INT32

    # Response error code
    error_code: "int"  # INT16


@dataclass
class Topics:
    # Name of topic
    topic: "str"  # STRING

    partitions: List["Partitions"]


@dataclass
class AlterReplicaLogDirsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    topics: List["Topics"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.ALTER_REPLICA_LOG_DIRS  # == 34


topicsSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
}


topicsSerializers: Dict[int, BaseSerializer[Topics]] = {
    version: NamedTupleSerializer(Topics, schema) for version, schema in topicsSchemas.items()
}


logDirsSchemas: Dict[int, Schema] = {
    0: [("log_dir", stringSerializer), ("topics", ArraySerializer(topicsSerializers[0]))],
    1: [("log_dir", stringSerializer), ("topics", ArraySerializer(topicsSerializers[1]))],
}


logDirsSerializers: Dict[int, BaseSerializer[LogDirs]] = {
    version: NamedTupleSerializer(LogDirs, schema) for version, schema in logDirsSchemas.items()
}


alterReplicaLogDirsRequestDataSchemas: Dict[int, Schema] = {
    0: [("log_dirs", ArraySerializer(logDirsSerializers[0]))],
    1: [("log_dirs", ArraySerializer(logDirsSerializers[1]))],
}


alterReplicaLogDirsRequestDataSerializers: Dict[int, BaseSerializer[AlterReplicaLogDirsRequestData]] = {
    version: NamedTupleSerializer(AlterReplicaLogDirsRequestData, schema)
    for version, schema in alterReplicaLogDirsRequestDataSchemas.items()
}


partitionsSchemas: Dict[int, Schema] = {
    0: [("partition", int32Serializer), ("error_code", int16Serializer)],
    1: [("partition", int32Serializer), ("error_code", int16Serializer)],
}


partitionsSerializers: Dict[int, BaseSerializer[Partitions]] = {
    version: NamedTupleSerializer(Partitions, schema) for version, schema in partitionsSchemas.items()
}


topicsSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[0]))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[1]))],
}


topicsSerializers: Dict[int, BaseSerializer[Topics]] = {
    version: NamedTupleSerializer(Topics, schema) for version, schema in topicsSchemas.items()
}


alterReplicaLogDirsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[1]))],
}


alterReplicaLogDirsResponseDataSerializers: Dict[int, BaseSerializer[AlterReplicaLogDirsResponseData]] = {
    version: NamedTupleSerializer(AlterReplicaLogDirsResponseData, schema)
    for version, schema in alterReplicaLogDirsResponseDataSchemas.items()
}