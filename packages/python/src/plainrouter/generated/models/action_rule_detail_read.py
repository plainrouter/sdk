from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_rule_detail_read_rule import ActionRuleDetailReadRule


T = TypeVar("T", bound="ActionRuleDetailRead")


@_attrs_define
class ActionRuleDetailRead:
    """
    Attributes:
        rule (ActionRuleDetailReadRule):
    """

    rule: ActionRuleDetailReadRule
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_rule_detail_read_rule import ActionRuleDetailReadRule

        d = dict(src_dict)
        rule = ActionRuleDetailReadRule.from_dict(d.pop("rule"))

        action_rule_detail_read = cls(
            rule=rule,
        )

        action_rule_detail_read.additional_properties = d
        return action_rule_detail_read

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
