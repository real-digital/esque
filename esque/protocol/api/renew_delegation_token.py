# FIXME autogenerated module, check for errors!
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional

from esque.protocol.api.base import *
from esque.protocol.serializers import *


@dataclass
class RenewDelegationTokenRequestData(RequestData):
    # HMAC of the delegation token to be renewed.
    hmac: "bytes"  # BYTES

    # Renew time period in milli seconds.
    renew_time_period: "int"  # INT64

    @staticmethod
    def api_key() -> int:
        return ApiKey.RENEW_DELEGATION_TOKEN  # == 39


@dataclass
class RenewDelegationTokenResponseData(ResponseData):
    # Response error code
    error_code: "int"  # INT16

    # timestamp (in msec) at which this token expires..
    expiry_timestamp: "int"  # INT64

    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    @staticmethod
    def api_key() -> int:
        return ApiKey.RENEW_DELEGATION_TOKEN  # == 39


renewDelegationTokenRequestDataSchemas: Dict[int, Schema] = {
    0: [("hmac", bytesSerializer), ("renew_time_period", int64Serializer)],
    1: [("hmac", bytesSerializer), ("renew_time_period", int64Serializer)],
}


renewDelegationTokenRequestDataSerializers: Dict[int, BaseSerializer[RenewDelegationTokenRequestData]] = {
    version: NamedTupleSerializer(RenewDelegationTokenRequestData, schema)
    for version, schema in renewDelegationTokenRequestDataSchemas.items()
}


renewDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", int16Serializer), ("expiry_timestamp", int64Serializer), ("throttle_time_ms", int32Serializer)],
    1: [("error_code", int16Serializer), ("expiry_timestamp", int64Serializer), ("throttle_time_ms", int32Serializer)],
}


renewDelegationTokenResponseDataSerializers: Dict[int, BaseSerializer[RenewDelegationTokenResponseData]] = {
    version: NamedTupleSerializer(RenewDelegationTokenResponseData, schema)
    for version, schema in renewDelegationTokenResponseDataSchemas.items()
}