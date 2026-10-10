from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdTestListReadObservedConversionEventsItem")


@_attrs_define
class AdTestListReadObservedConversionEventsItem:
    """
    Attributes:
        event_name (str):
        recorded_count (int):
    """

    event_name: str
    recorded_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        recorded_count = self.recorded_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_name": event_name,
                "recorded_count": recorded_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_name = d.pop("event_name")

        recorded_count = d.pop("recorded_count")

        ad_test_list_read_observed_conversion_events_item = cls(
            event_name=event_name,
            recorded_count=recorded_count,
        )

        ad_test_list_read_observed_conversion_events_item.additional_properties = d
        return ad_test_list_read_observed_conversion_events_item

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
