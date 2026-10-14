from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LaunchPlansIndexResponse200PlansNextPageArgumentsType1")


@_attrs_define
class LaunchPlansIndexResponse200PlansNextPageArgumentsType1:
    """
    Attributes:
        cursor (int):
        per_page (int):
    """

    cursor: int
    per_page: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        per_page = self.per_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cursor": cursor,
                "per_page": per_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cursor = d.pop("cursor")

        per_page = d.pop("per_page")

        launch_plans_index_response_200_plans_next_page_arguments_type_1 = cls(
            cursor=cursor,
            per_page=per_page,
        )

        launch_plans_index_response_200_plans_next_page_arguments_type_1.additional_properties = d
        return launch_plans_index_response_200_plans_next_page_arguments_type_1

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
