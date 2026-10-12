from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_account_inventory_response_200_summary_by_level import (
        GetAccountInventoryResponse200SummaryByLevel,
    )


T = TypeVar("T", bound="GetAccountInventoryResponse200Summary")


@_attrs_define
class GetAccountInventoryResponse200Summary:
    """
    Attributes:
        total (int | Unset):
        by_level (GetAccountInventoryResponse200SummaryByLevel | Unset):
    """

    total: int | Unset = UNSET
    by_level: GetAccountInventoryResponse200SummaryByLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_level, Unset):
            by_level = self.by_level.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if by_level is not UNSET:
            field_dict["by_level"] = by_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_account_inventory_response_200_summary_by_level import (
            GetAccountInventoryResponse200SummaryByLevel,
        )

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _by_level = d.pop("by_level", UNSET)
        by_level: GetAccountInventoryResponse200SummaryByLevel | Unset
        if isinstance(_by_level, Unset):
            by_level = UNSET
        else:
            by_level = GetAccountInventoryResponse200SummaryByLevel.from_dict(_by_level)

        get_account_inventory_response_200_summary = cls(
            total=total,
            by_level=by_level,
        )

        get_account_inventory_response_200_summary.additional_properties = d
        return get_account_inventory_response_200_summary

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
