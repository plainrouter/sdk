from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_rule_write_read_rule_revisions_item_action import ActionRuleWriteReadRuleRevisionsItemAction
from ..models.action_rule_write_read_rule_revisions_item_author_type import (
    ActionRuleWriteReadRuleRevisionsItemAuthorType,
)
from ..models.action_rule_write_read_rule_revisions_item_cost_comparison import (
    ActionRuleWriteReadRuleRevisionsItemCostComparison,
)
from ..models.action_rule_write_read_rule_revisions_item_target_level import (
    ActionRuleWriteReadRuleRevisionsItemTargetLevel,
)

T = TypeVar("T", bound="ActionRuleWriteReadRuleRevisionsItem")


@_attrs_define
class ActionRuleWriteReadRuleRevisionsItem:
    """
    Attributes:
        id (str):
        target_level (ActionRuleWriteReadRuleRevisionsItemTargetLevel):
        action (ActionRuleWriteReadRuleRevisionsItemAction):
        budget_change_percent (int | None):
        minimum_counted_arrivals (int):
        cost_comparison (ActionRuleWriteReadRuleRevisionsItemCostComparison):
        cost_ratio (str):
        author_type (ActionRuleWriteReadRuleRevisionsItemAuthorType):
        created_at (datetime.datetime):
    """

    id: str
    target_level: ActionRuleWriteReadRuleRevisionsItemTargetLevel
    action: ActionRuleWriteReadRuleRevisionsItemAction
    budget_change_percent: int | None
    minimum_counted_arrivals: int
    cost_comparison: ActionRuleWriteReadRuleRevisionsItemCostComparison
    cost_ratio: str
    author_type: ActionRuleWriteReadRuleRevisionsItemAuthorType
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_level = self.target_level.value

        action = self.action.value

        budget_change_percent: int | None
        budget_change_percent = self.budget_change_percent

        minimum_counted_arrivals = self.minimum_counted_arrivals

        cost_comparison = self.cost_comparison.value

        cost_ratio = self.cost_ratio

        author_type = self.author_type.value

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_level": target_level,
                "action": action,
                "budget_change_percent": budget_change_percent,
                "minimum_counted_arrivals": minimum_counted_arrivals,
                "cost_comparison": cost_comparison,
                "cost_ratio": cost_ratio,
                "author_type": author_type,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        target_level = ActionRuleWriteReadRuleRevisionsItemTargetLevel(d.pop("target_level"))

        action = ActionRuleWriteReadRuleRevisionsItemAction(d.pop("action"))

        def _parse_budget_change_percent(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        budget_change_percent = _parse_budget_change_percent(d.pop("budget_change_percent"))

        minimum_counted_arrivals = d.pop("minimum_counted_arrivals")

        cost_comparison = ActionRuleWriteReadRuleRevisionsItemCostComparison(d.pop("cost_comparison"))

        cost_ratio = d.pop("cost_ratio")

        author_type = ActionRuleWriteReadRuleRevisionsItemAuthorType(d.pop("author_type"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        action_rule_write_read_rule_revisions_item = cls(
            id=id,
            target_level=target_level,
            action=action,
            budget_change_percent=budget_change_percent,
            minimum_counted_arrivals=minimum_counted_arrivals,
            cost_comparison=cost_comparison,
            cost_ratio=cost_ratio,
            author_type=author_type,
            created_at=created_at,
        )

        action_rule_write_read_rule_revisions_item.additional_properties = d
        return action_rule_write_read_rule_revisions_item

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
