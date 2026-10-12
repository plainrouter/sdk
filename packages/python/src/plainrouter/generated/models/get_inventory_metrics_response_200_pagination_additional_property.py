from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200PaginationAdditionalProperty")


@_attrs_define
class GetInventoryMetricsResponse200PaginationAdditionalProperty:
    """
    Attributes:
        total (int):
        truncated (bool):
        next_cursor (int | None):
    """

    total: int
    truncated: bool
    next_cursor: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        truncated = self.truncated

        next_cursor: int | None
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "truncated": truncated,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        truncated = d.pop("truncated")

        def _parse_next_cursor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        get_inventory_metrics_response_200_pagination_additional_property = cls(
            total=total,
            truncated=truncated,
            next_cursor=next_cursor,
        )

        get_inventory_metrics_response_200_pagination_additional_property.additional_properties = d
        return get_inventory_metrics_response_200_pagination_additional_property

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
