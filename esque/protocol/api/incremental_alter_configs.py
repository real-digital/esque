# FIXME autogenerated module, check for errors!
from typing import Dict, List

from dataclasses import dataclass

from esque.protocol.api.base import ApiKey, RequestData, ResponseData
from esque.protocol.serializers import (
    ArraySerializer, BaseSerializer, NamedTupleSerializer, Schema, booleanSerializer, int16Serializer, int32Serializer,
    int8Serializer, nullableStringSerializer, stringSerializer
)


@dataclass
class Configs:
    # The configuration key name.
    name: "str"  # STRING

    # The type (Set, Delete, Append, Subtract) of operation.
    config_operation: "int"  # INT8

    # The value to set for the configuration key.
    value: "Optional[str]"  # NULLABLE_STRING


@dataclass
class Resources:
    # The resource type.
    resource_type: "int"  # INT8

    # The resource name.
    resource_name: "str"  # STRING

    # The configurations.
    configs: List["Configs"]


@dataclass
class IncrementalAlterConfigsRequestData(RequestData):
    # The incremental updates for each resource.
    resources: List["Resources"]

    # True if we should validate the request, but not change the configurations.
    validate_only: "bool"  # BOOLEAN

    @staticmethod
    def api_key() -> int:
        return ApiKey.INCREMENTAL_ALTER_CONFIGS  # == 44


@dataclass
class Responses:
    # The resource error code.
    error_code: "int"  # INT16

    # The resource error message, or null if there was no error.
    error_message: "Optional[str]"  # NULLABLE_STRING

    # The resource type.
    resource_type: "int"  # INT8

    # The resource name.
    resource_name: "str"  # STRING


@dataclass
class IncrementalAlterConfigsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to a quota violation, or zero if
    # the request did not violate any quota.
    throttle_time_ms: "int"  # INT32

    # The responses for each resource.
    responses: List["Responses"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.INCREMENTAL_ALTER_CONFIGS  # == 44


configsSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("config_operation", int8Serializer), ("value", nullableStringSerializer)]
}


configsSerializers: Dict[int, BaseSerializer[Configs]] = {
    version: NamedTupleSerializer(Configs, schema) for version, schema in configsSchemas.items()
}


resourcesSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("configs", ArraySerializer(configsSerializers[0])),
    ]
}


resourcesSerializers: Dict[int, BaseSerializer[Resources]] = {
    version: NamedTupleSerializer(Resources, schema) for version, schema in resourcesSchemas.items()
}


incrementalAlterConfigsRequestDataSchemas: Dict[int, Schema] = {
    0: [("resources", ArraySerializer(resourcesSerializers[0])), ("validate_only", booleanSerializer)]
}


incrementalAlterConfigsRequestDataSerializers: Dict[int, BaseSerializer[IncrementalAlterConfigsRequestData]] = {
    version: NamedTupleSerializer(IncrementalAlterConfigsRequestData, schema)
    for version, schema in incrementalAlterConfigsRequestDataSchemas.items()
}


responsesSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
    ]
}


responsesSerializers: Dict[int, BaseSerializer[Responses]] = {
    version: NamedTupleSerializer(Responses, schema) for version, schema in responsesSchemas.items()
}


incrementalAlterConfigsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responsesSerializers[0]))]
}


incrementalAlterConfigsResponseDataSerializers: Dict[int, BaseSerializer[IncrementalAlterConfigsResponseData]] = {
    version: NamedTupleSerializer(IncrementalAlterConfigsResponseData, schema)
    for version, schema in incrementalAlterConfigsResponseDataSchemas.items()
}
