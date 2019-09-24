# FIXME autogenerated module, check for errors!
from typing import Dict, List

from dataclasses import dataclass

from esque.protocol.api.base import ApiKey, RequestData, ResponseData
from esque.protocol.serializers import (
    ArraySerializer, BaseSerializer, NamedTupleSerializer, Schema, booleanSerializer, int16Serializer, int32Serializer,
    int8Serializer, nullableStringSerializer, stringSerializer
)


@dataclass
class ConfigEntries:
    # Configuration name
    config_name: "str"  # STRING

    # Configuration value
    config_value: "Optional[str]"  # NULLABLE_STRING


@dataclass
class Resources:
    resource_type: "int"  # INT8

    resource_name: "str"  # STRING

    config_entries: List["ConfigEntries"]


@dataclass
class AlterConfigsRequestData(RequestData):
    # An array of resources to update with the provided configs.
    resources: List["Resources"]

    validate_only: "bool"  # BOOLEAN

    @staticmethod
    def api_key() -> int:
        return ApiKey.ALTER_CONFIGS  # == 33


@dataclass
class Resources:
    # Response error code
    error_code: "int"  # INT16

    # Response error message
    error_message: "Optional[str]"  # NULLABLE_STRING

    resource_type: "int"  # INT8

    resource_name: "str"  # STRING


@dataclass
class AlterConfigsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    resources: List["Resources"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.ALTER_CONFIGS  # == 33


configEntriesSchemas: Dict[int, Schema] = {
    0: [("config_name", stringSerializer), ("config_value", nullableStringSerializer)],
    1: [("config_name", stringSerializer), ("config_value", nullableStringSerializer)],
}


configEntriesSerializers: Dict[int, BaseSerializer[ConfigEntries]] = {
    version: NamedTupleSerializer(ConfigEntries, schema) for version, schema in configEntriesSchemas.items()
}


resourcesSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("config_entries", ArraySerializer(configEntriesSerializers[0])),
    ],
    1: [
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("config_entries", ArraySerializer(configEntriesSerializers[1])),
    ],
}


resourcesSerializers: Dict[int, BaseSerializer[Resources]] = {
    version: NamedTupleSerializer(Resources, schema) for version, schema in resourcesSchemas.items()
}


alterConfigsRequestDataSchemas: Dict[int, Schema] = {
    0: [("resources", ArraySerializer(resourcesSerializers[0])), ("validate_only", booleanSerializer)],
    1: [("resources", ArraySerializer(resourcesSerializers[1])), ("validate_only", booleanSerializer)],
}


alterConfigsRequestDataSerializers: Dict[int, BaseSerializer[AlterConfigsRequestData]] = {
    version: NamedTupleSerializer(AlterConfigsRequestData, schema)
    for version, schema in alterConfigsRequestDataSchemas.items()
}


resourcesSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
    ],
    1: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
    ],
}


resourcesSerializers: Dict[int, BaseSerializer[Resources]] = {
    version: NamedTupleSerializer(Resources, schema) for version, schema in resourcesSchemas.items()
}


alterConfigsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("resources", ArraySerializer(resourcesSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("resources", ArraySerializer(resourcesSerializers[1]))],
}


alterConfigsResponseDataSerializers: Dict[int, BaseSerializer[AlterConfigsResponseData]] = {
    version: NamedTupleSerializer(AlterConfigsResponseData, schema)
    for version, schema in alterConfigsResponseDataSchemas.items()
}
