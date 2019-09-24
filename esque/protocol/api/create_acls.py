# FIXME autogenerated module, check for errors!
from typing import Dict, List

from dataclasses import dataclass

from esque.protocol.api.base import ApiKey, RequestData, ResponseData
from esque.protocol.serializers import (
    ArraySerializer, BaseSerializer, DummySerializer, NamedTupleSerializer, Schema, int16Serializer, int32Serializer,
    int8Serializer, nullableStringSerializer, stringSerializer
)


@dataclass
class Creations:
    # The resource type
    resource_type: "int"  # INT8

    # The resource name
    resource_name: "str"  # STRING

    # The resource pattern type
    resource_pattern_type: "int"  # INT8

    # The ACL principal
    principal: "str"  # STRING

    # The ACL host
    host: "str"  # STRING

    # The ACL operation
    operation: "int"  # INT8

    # The ACL permission type
    permission_type: "int"  # INT8


@dataclass
class CreateAclsRequestData(RequestData):
    creations: List["Creations"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.CREATE_ACLS  # == 30


@dataclass
class CreationResponses:
    # Response error code
    error_code: "int"  # INT16

    # Response error message
    error_message: "Optional[str]"  # NULLABLE_STRING


@dataclass
class CreateAclsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    creation_responses: List["CreationResponses"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.CREATE_ACLS  # == 30


creationsSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("principal", stringSerializer),
        ("host", stringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
        ("resource_pattern_type", DummySerializer(int())),
    ],
    1: [
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("resource_pattern_type", int8Serializer),
        ("principal", stringSerializer),
        ("host", stringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
    ],
}


creationsSerializers: Dict[int, BaseSerializer[Creations]] = {
    version: NamedTupleSerializer(Creations, schema) for version, schema in creationsSchemas.items()
}


createAclsRequestDataSchemas: Dict[int, Schema] = {
    0: [("creations", ArraySerializer(creationsSerializers[0]))],
    1: [("creations", ArraySerializer(creationsSerializers[1]))],
}


createAclsRequestDataSerializers: Dict[int, BaseSerializer[CreateAclsRequestData]] = {
    version: NamedTupleSerializer(CreateAclsRequestData, schema)
    for version, schema in createAclsRequestDataSchemas.items()
}


creationResponsesSchemas: Dict[int, Schema] = {
    0: [("error_code", int16Serializer), ("error_message", nullableStringSerializer)],
    1: [("error_code", int16Serializer), ("error_message", nullableStringSerializer)],
}


creationResponsesSerializers: Dict[int, BaseSerializer[CreationResponses]] = {
    version: NamedTupleSerializer(CreationResponses, schema) for version, schema in creationResponsesSchemas.items()
}


createAclsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("creation_responses", ArraySerializer(creationResponsesSerializers[0])),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("creation_responses", ArraySerializer(creationResponsesSerializers[1])),
    ],
}


createAclsResponseDataSerializers: Dict[int, BaseSerializer[CreateAclsResponseData]] = {
    version: NamedTupleSerializer(CreateAclsResponseData, schema)
    for version, schema in createAclsResponseDataSchemas.items()
}
