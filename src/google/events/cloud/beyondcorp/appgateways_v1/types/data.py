# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.beyondcorp.appgateways.v1',
    manifest={
        'AppGateway',
        'AppGatewayEventData',
    },
)


class AppGateway(proto.Message):
    r"""A BeyondCorp AppGateway resource represents a BeyondCorp
    protected AppGateway to a remote application. It creates all the
    necessary GCP components needed for creating a BeyondCorp
    protected AppGateway. Multiple connectors can be authorised for
    a single AppGateway.

    Attributes:
        name (str):
            Required. Unique resource name of the
            AppGateway. The name is ignored when creating an
            AppGateway.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            last modified.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata.
        display_name (str):
            Optional. An arbitrary user-provided name for
            the AppGateway. Cannot exceed 64 characters.
        uid (str):
            Output only. A unique identifier for the
            instance generated by the system.
        type_ (google.events.cloud.beyondcorp.appgateways_v1.types.AppGateway.Type):
            Required. The type of network connectivity
            used by the AppGateway.
        state (google.events.cloud.beyondcorp.appgateways_v1.types.AppGateway.State):
            Output only. The current state of the
            AppGateway.
        uri (str):
            Output only. Server-defined URI for this
            resource.
        allocated_connections (MutableSequence[google.events.cloud.beyondcorp.appgateways_v1.types.AppGateway.AllocatedConnection]):
            Output only. A list of connections allocated
            for the Gateway
        host_type (google.events.cloud.beyondcorp.appgateways_v1.types.AppGateway.HostType):
            Required. The type of hosting used by the
            AppGateway.
    """
    class Type(proto.Enum):
        r"""Enum containing list of all possible network connectivity
        options supported by BeyondCorp AppGateway.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            TCP_PROXY (1):
                TCP Proxy based BeyondCorp Connection. API
                will default to this if unset.
        """
        TYPE_UNSPECIFIED = 0
        TCP_PROXY = 1

    class State(proto.Enum):
        r"""Represents the different states of an AppGateway.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                AppGateway is being created.
            CREATED (2):
                AppGateway has been created.
            UPDATING (3):
                AppGateway's configuration is being updated.
            DELETING (4):
                AppGateway is being deleted.
            DOWN (5):
                AppGateway is down and may be restored in the
                future. This happens when CCFE sends
                ProjectState = OFF.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3
        DELETING = 4
        DOWN = 5

    class HostType(proto.Enum):
        r"""Enum containing list of all possible host types supported by
        BeyondCorp Connection.

        Values:
            HOST_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            GCP_REGIONAL_MIG (1):
                AppGateway hosted in a GCP regional managed
                instance group.
        """
        HOST_TYPE_UNSPECIFIED = 0
        GCP_REGIONAL_MIG = 1

    class AllocatedConnection(proto.Message):
        r"""Allocated connection of the AppGateway.

        Attributes:
            psc_uri (str):
                Required. The PSC uri of an allocated
                connection
            ingress_port (int):
                Required. The ingress port of an allocated
                connection
        """

        psc_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ingress_port: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    allocated_connections: MutableSequence[AllocatedConnection] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=AllocatedConnection,
    )
    host_type: HostType = proto.Field(
        proto.ENUM,
        number=11,
        enum=HostType,
    )


class AppGatewayEventData(proto.Message):
    r"""The data within all AppGateway events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.beyondcorp.appgateways_v1.types.AppGateway):
            Optional. The AppGateway event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'AppGateway' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='AppGateway',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
