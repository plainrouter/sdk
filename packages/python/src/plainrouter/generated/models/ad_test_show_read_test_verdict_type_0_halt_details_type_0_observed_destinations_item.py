from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem")


@_attrs_define
class AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem:
    """
    Attributes:
        host (str):
        path (str):
        counted_arrivals (int):
    """

    host: str
    path: str
    counted_arrivals: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        path = self.path

        counted_arrivals = self.counted_arrivals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "path": path,
                "counted_arrivals": counted_arrivals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        path = d.pop("path")

        counted_arrivals = d.pop("counted_arrivals")

        ad_test_show_read_test_verdict_type_0_halt_details_type_0_observed_destinations_item = cls(
            host=host,
            path=path,
            counted_arrivals=counted_arrivals,
        )

        ad_test_show_read_test_verdict_type_0_halt_details_type_0_observed_destinations_item.additional_properties = d
        return ad_test_show_read_test_verdict_type_0_halt_details_type_0_observed_destinations_item

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
