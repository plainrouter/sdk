from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteUserDataResponse200")


@_attrs_define
class DeleteUserDataResponse200:
    """
    Attributes:
        deletion_request_id (str):
        duplicate (bool):
        events_updated (int):
        sessions_updated (int):
        completed_at (str):
    """

    deletion_request_id: str
    duplicate: bool
    events_updated: int
    sessions_updated: int
    completed_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deletion_request_id = self.deletion_request_id

        duplicate = self.duplicate

        events_updated = self.events_updated

        sessions_updated = self.sessions_updated

        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deletion_request_id": deletion_request_id,
                "duplicate": duplicate,
                "events_updated": events_updated,
                "sessions_updated": sessions_updated,
                "completed_at": completed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deletion_request_id = d.pop("deletion_request_id")

        duplicate = d.pop("duplicate")

        events_updated = d.pop("events_updated")

        sessions_updated = d.pop("sessions_updated")

        completed_at = d.pop("completed_at")

        delete_user_data_response_200 = cls(
            deletion_request_id=deletion_request_id,
            duplicate=duplicate,
            events_updated=events_updated,
            sessions_updated=sessions_updated,
            completed_at=completed_at,
        )

        delete_user_data_response_200.additional_properties = d
        return delete_user_data_response_200

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
