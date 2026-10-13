from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsRulesIndexResponse200RulesDataItemCounts")


@_attrs_define
class ActionsRulesIndexResponse200RulesDataItemCounts:
    """
    Attributes:
        revisions (int | Unset):
        runs (int | Unset):
    """

    revisions: int | Unset = UNSET
    runs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revisions = self.revisions

        runs = self.runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if runs is not UNSET:
            field_dict["runs"] = runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revisions = d.pop("revisions", UNSET)

        runs = d.pop("runs", UNSET)

        actions_rules_index_response_200_rules_data_item_counts = cls(
            revisions=revisions,
            runs=runs,
        )

        actions_rules_index_response_200_rules_data_item_counts.additional_properties = d
        return actions_rules_index_response_200_rules_data_item_counts

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
