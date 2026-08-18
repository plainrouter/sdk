from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReplayDeliveriesResponse202")


@_attrs_define
class ReplayDeliveriesResponse202:
    """
    Attributes:
        queued (int):
        expired (int):
        payload_expired (int):
        capped (bool):
    """

    queued: int
    expired: int
    payload_expired: int
    capped: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queued = self.queued

        expired = self.expired

        payload_expired = self.payload_expired

        capped = self.capped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queued": queued,
                "expired": expired,
                "payload_expired": payload_expired,
                "capped": capped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queued = d.pop("queued")

        expired = d.pop("expired")

        payload_expired = d.pop("payload_expired")

        capped = d.pop("capped")

        replay_deliveries_response_202 = cls(
            queued=queued,
            expired=expired,
            payload_expired=payload_expired,
            capped=capped,
        )

        replay_deliveries_response_202.additional_properties = d
        return replay_deliveries_response_202

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
