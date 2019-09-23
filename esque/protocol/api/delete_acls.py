# FIXME autogenerated module, check for errors!
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional

from esque.protocol.api.base import *
from esque.protocol.serializers import *


@dataclass
class Filters:
    # The resource type
    resource_type: "int"  # INT8

    # The resource name filter
    resource_name: "Optional[str]"  # NULLABLE_STRING

    # The resource pattern type filter
    resource_pattern_type_filter: "int"  # INT8

    # The ACL principal filter
    principal: "Optional[str]"  # NULLABLE_STRING

    # The ACL host filter
    host: "Optional[str]"  # NULLABLE_STRING

    # The ACL operation
    operation: "int"  # INT8

    # The ACL permission type
    permission_type: "int"  # INT8


@dataclass
class DeleteAclsRequestData(RequestData):
    filters: List["Filters"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.DELETE_ACLS  # == 31


@dataclass
class MatchingAcls:
    # Response error code
    error_code: "int"  # INT16

    # Response error message
    error_message: "Optional[str]"  # NULLABLE_STRING

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
class FilterResponses:
    # Response error code
    error_code: "int"  # INT16

    # Response error message
    error_message: "Optional[str]"  # NULLABLE_STRING

    # The matching ACLs
    matching_acls: List["MatchingAcls"]


@dataclass
class DeleteAclsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    filter_responses: List["FilterResponses"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.DELETE_ACLS  # == 31


filtersSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", int8Serializer),
        ("resource_name", nullableStringSerializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
        ("resource_pattern_type_filter", DummySerializer(int())),
    ],
    1: [
        ("resource_type", int8Serializer),
        ("resource_name", nullableStringSerializer),
        ("resource_pattern_type_filter", int8Serializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
    ],
}


filtersSerializers: Dict[int, BaseSerializer[Filters]] = {
    version: NamedTupleSerializer(Filters, schema) for version, schema in filtersSchemas.items()
}


deleteAclsRequestDataSchemas: Dict[int, Schema] = {
    0: [("filters", ArraySerializer(filtersSerializers[0]))],
    1: [("filters", ArraySerializer(filtersSerializers[1]))],
}


deleteAclsRequestDataSerializers: Dict[int, BaseSerializer[DeleteAclsRequestData]] = {
    version: NamedTupleSerializer(DeleteAclsRequestData, schema)
    for version, schema in deleteAclsRequestDataSchemas.items()
}


matchingAclsSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("principal", stringSerializer),
        ("host", stringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
        ("resource_pattern_type", DummySerializer(int())),
    ],
    1: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", int8Serializer),
        ("resource_name", stringSerializer),
        ("resource_pattern_type", int8Serializer),
        ("principal", stringSerializer),
        ("host", stringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
    ],
}


matchingAclsSerializers: Dict[int, BaseSerializer[MatchingAcls]] = {
    version: NamedTupleSerializer(MatchingAcls, schema) for version, schema in matchingAclsSchemas.items()
}


filterResponsesSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("matching_acls", ArraySerializer(matchingAclsSerializers[0])),
    ],
    1: [
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
        ("matching_acls", ArraySerializer(matchingAclsSerializers[1])),
    ],
}


filterResponsesSerializers: Dict[int, BaseSerializer[FilterResponses]] = {
    version: NamedTupleSerializer(FilterResponses, schema) for version, schema in filterResponsesSchemas.items()
}


deleteAclsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("filter_responses", ArraySerializer(filterResponsesSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("filter_responses", ArraySerializer(filterResponsesSerializers[1]))],
}


deleteAclsResponseDataSerializers: Dict[int, BaseSerializer[DeleteAclsResponseData]] = {
    version: NamedTupleSerializer(DeleteAclsResponseData, schema)
    for version, schema in deleteAclsResponseDataSchemas.items()
}