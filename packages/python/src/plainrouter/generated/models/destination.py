from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.destination_credential_source import DestinationCredentialSource
from ..models.destination_status import DestinationStatus
from ..models.destination_type import DestinationType

if TYPE_CHECKING:
    from ..models.destination_attention_reason_type_0 import DestinationAttentionReasonType0
    from ..models.destination_config_type_0 import DestinationConfigType0
    from ..models.destination_notices_item import DestinationNoticesItem


T = TypeVar("T", bound="Destination")


@_attrs_define
class Destination:
    """
    Attributes:
        id (str):
        workspace_id (int):
        signal_tracker_id (str): Deprecated alias of workspace_id; contains the workspace ID in decimal string form.
        platform_ad_account_id (int | None):
        type_ (DestinationType):
        credential_source (DestinationCredentialSource):
        config (DestinationConfigType0 | list[Any]):
        status (DestinationStatus):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
        attention_reason (DestinationAttentionReasonType0 | list[Any] | None):
        held_count (int):
        notices (list[DestinationNoticesItem]):
    """

    id: str
    workspace_id: int
    signal_tracker_id: str
    platform_ad_account_id: int | None
    type_: DestinationType
    credential_source: DestinationCredentialSource
    config: DestinationConfigType0 | list[Any]
    status: DestinationStatus
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    attention_reason: DestinationAttentionReasonType0 | list[Any] | None
    held_count: int
    notices: list[DestinationNoticesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.destination_attention_reason_type_0 import DestinationAttentionReasonType0
        from ..models.destination_config_type_0 import DestinationConfigType0

        id = self.id

        workspace_id = self.workspace_id

        signal_tracker_id = self.signal_tracker_id

        platform_ad_account_id: int | None
        platform_ad_account_id = self.platform_ad_account_id

        type_ = self.type_.value

        credential_source = self.credential_source.value

        config: dict[str, Any] | list[Any]
        if isinstance(self.config, DestinationConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        status = self.status.value

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        attention_reason: dict[str, Any] | list[Any] | None
        if isinstance(self.attention_reason, DestinationAttentionReasonType0):
            attention_reason = self.attention_reason.to_dict()
        elif isinstance(self.attention_reason, list):
            attention_reason = self.attention_reason

        else:
            attention_reason = self.attention_reason

        held_count = self.held_count

        notices = []
        for notices_item_data in self.notices:
            notices_item = notices_item_data.to_dict()
            notices.append(notices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "signal_tracker_id": signal_tracker_id,
                "platform_ad_account_id": platform_ad_account_id,
                "type": type_,
                "credential_source": credential_source,
                "config": config,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "attention_reason": attention_reason,
                "held_count": held_count,
                "notices": notices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.destination_attention_reason_type_0 import DestinationAttentionReasonType0
        from ..models.destination_config_type_0 import DestinationConfigType0
        from ..models.destination_notices_item import DestinationNoticesItem

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_platform_ad_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        platform_ad_account_id = _parse_platform_ad_account_id(d.pop("platform_ad_account_id"))

        type_ = DestinationType(d.pop("type"))

        credential_source = DestinationCredentialSource(d.pop("credential_source"))

        def _parse_config(data: object) -> DestinationConfigType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = DestinationConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            config_type_1 = cast(list[Any], data)

            return config_type_1

        config = _parse_config(d.pop("config"))

        status = DestinationStatus(d.pop("status"))

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_attention_reason(data: object) -> DestinationAttentionReasonType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attention_reason_type_0 = DestinationAttentionReasonType0.from_dict(data)

                return attention_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attention_reason_type_1 = cast(list[Any], data)

                return attention_reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DestinationAttentionReasonType0 | list[Any] | None, data)

        attention_reason = _parse_attention_reason(d.pop("attention_reason"))

        held_count = d.pop("held_count")

        notices = []
        _notices = d.pop("notices")
        for notices_item_data in _notices:
            notices_item = DestinationNoticesItem.from_dict(notices_item_data)

            notices.append(notices_item)

        destination = cls(
            id=id,
            workspace_id=workspace_id,
            signal_tracker_id=signal_tracker_id,
            platform_ad_account_id=platform_ad_account_id,
            type_=type_,
            credential_source=credential_source,
            config=config,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            attention_reason=attention_reason,
            held_count=held_count,
            notices=notices,
        )

        destination.additional_properties = d
        return destination

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
