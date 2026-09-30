from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionDryRunReadDryRunActionsItemType0Diff")


@_attrs_define
class ActionDryRunReadDryRunActionsItemType0Diff:
    """
    Attributes:
        before (Any):
        proposed (Any):
    """

    before: Any
    proposed: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        before = self.before

        proposed = self.proposed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "before": before,
                "proposed": proposed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        before = d.pop("before")

        proposed = d.pop("proposed")

        action_dry_run_read_dry_run_actions_item_type_0_diff = cls(
            before=before,
            proposed=proposed,
        )

        action_dry_run_read_dry_run_actions_item_type_0_diff.additional_properties = d
        return action_dry_run_read_dry_run_actions_item_type_0_diff

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
