# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
    package='google.events.cloud.beyondcorp.clientgateways.v1',
    manifest={
        'ClientGateway',
        'ClientGatewayEventData',
    },
)


class ClientGateway(proto.Message):
    r"""Message describing ClientGateway object.

    Attributes:
        name (str):
            Required. name of resource. The name is
            ignored during creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        state (google.events.cloud.beyondcorp.clientgateways_v1.types.ClientGateway.State):
            Output only. The operational state of the
            gateway.
        id (str):
            Output only. A unique identifier for the
            instance generated by the system.
        client_connector_service (str):
            Output only. The client connector service name that the
            client gateway is associated to. Client Connector Services,
            named as follows:
            ``projects/{project_id}/locations/{location_id}/client_connector_services/{client_connector_service_id}``.
    """
    class State(proto.Enum):
        r"""Represents the different states of a gateway.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                Gateway is being created.
            UPDATING (2):
                Gateway is being updated.
            DELETING (3):
                Gateway is being deleted.
            RUNNING (4):
                Gateway is running.
            DOWN (5):
                Gateway is down and may be restored in the
                future. This happens when CCFE sends
                ProjectState = OFF.
            ERROR (6):
                ClientGateway encountered an error and is in
                indeterministic state.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        UPDATING = 2
        DELETING = 3
        RUNNING = 4
        DOWN = 5
        ERROR = 6

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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    client_connector_service: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ClientGatewayEventData(proto.Message):
    r"""The data within all ClientGateway events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.beyondcorp.clientgateways_v1.types.ClientGateway):
            Optional. The ClientGateway event payload.
            Unset for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'ClientGateway' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='ClientGateway',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
