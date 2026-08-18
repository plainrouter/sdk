from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.destination_credential_source import DestinationCredentialSource
from ..models.destination_status import DestinationStatus
from ..models.destination_type import DestinationType

T = TypeVar("T", bound="Destination")


@_attrs_define
class Destination:
    """
    Attributes:
        id (str):
        signal_tracker_id (str):
        platform_ad_account_id (int | None):
        type_ (DestinationType):
        credential_source (DestinationCredentialSource):
        config (list[Any]):
        status (DestinationStatus):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
    """

    id: str
    signal_tracker_id: str
    platform_ad_account_id: int | None
    type_: DestinationType
    credential_source: DestinationCredentialSource
    config: list[Any]
    status: DestinationStatus
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signal_tracker_id = self.signal_tracker_id

        platform_ad_account_id: int | None
        platform_ad_account_id = self.platform_ad_account_id

        type_ = self.type_.value

        credential_source = self.credential_source.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "platform_ad_account_id": platform_ad_account_id,
                "type": type_,
                "credential_source": credential_source,
                "config": config,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_platform_ad_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        platform_ad_account_id = _parse_platform_ad_account_id(d.pop("platform_ad_account_id"))

        type_ = DestinationType(d.pop("type"))

        credential_source = DestinationCredentialSource(d.pop("credential_source"))

        config = cast(list[Any], d.pop("config"))

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

        destination = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            platform_ad_account_id=platform_ad_account_id,
            type_=type_,
            credential_source=credential_source,
            config=config,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
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
