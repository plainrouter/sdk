from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_rule_write_read_rule_window_days import ActionRuleWriteReadRuleWindowDays
from ..models.action_rule_write_read_rule_window_kind import ActionRuleWriteReadRuleWindowKind

T = TypeVar("T", bound="ActionRuleWriteReadRuleWindow")


@_attrs_define
class ActionRuleWriteReadRuleWindow:
    """
    Attributes:
        days (ActionRuleWriteReadRuleWindowDays):
        kind (ActionRuleWriteReadRuleWindowKind):
        timezone (str):
    """

    days: ActionRuleWriteReadRuleWindowDays
    kind: ActionRuleWriteReadRuleWindowKind
    timezone: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days.value

        kind = self.kind.value

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "kind": kind,
                "timezone": timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = ActionRuleWriteReadRuleWindowDays(d.pop("days"))

        kind = ActionRuleWriteReadRuleWindowKind(d.pop("kind"))

        timezone = d.pop("timezone")

        action_rule_write_read_rule_window = cls(
            days=days,
            kind=kind,
            timezone=timezone,
        )

        action_rule_write_read_rule_window.additional_properties = d
        return action_rule_write_read_rule_window

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
