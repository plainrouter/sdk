from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.actions_rules_update_body_definition_type_1_action import ActionsRulesUpdateBodyDefinitionType1Action
from ..models.actions_rules_update_body_definition_type_1_cost_comparison import (
    ActionsRulesUpdateBodyDefinitionType1CostComparison,
)
from ..models.actions_rules_update_body_definition_type_1_target_level import (
    ActionsRulesUpdateBodyDefinitionType1TargetLevel,
)

T = TypeVar("T", bound="ActionsRulesUpdateBodyDefinitionType1")


@_attrs_define
class ActionsRulesUpdateBodyDefinitionType1:
    """Only target_level, action, budget_change_percent, minimum_counted_arrivals, cost_comparison and cost_ratio are
    accepted.

        Attributes:
            target_level (ActionsRulesUpdateBodyDefinitionType1TargetLevel):
            action (ActionsRulesUpdateBodyDefinitionType1Action):
            minimum_counted_arrivals (int):
            cost_comparison (ActionsRulesUpdateBodyDefinitionType1CostComparison):
            cost_ratio (float | str): Numeric value from 0.10 to 10.00, with zero to two decimal places.
            budget_change_percent (int):
    """

    target_level: ActionsRulesUpdateBodyDefinitionType1TargetLevel
    action: ActionsRulesUpdateBodyDefinitionType1Action
    minimum_counted_arrivals: int
    cost_comparison: ActionsRulesUpdateBodyDefinitionType1CostComparison
    cost_ratio: float | str
    budget_change_percent: int

    def to_dict(self) -> dict[str, Any]:
        target_level = self.target_level.value

        action = self.action.value

        minimum_counted_arrivals = self.minimum_counted_arrivals

        cost_comparison = self.cost_comparison.value

        cost_ratio: float | str
        cost_ratio = self.cost_ratio

        budget_change_percent = self.budget_change_percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_level": target_level,
                "action": action,
                "minimum_counted_arrivals": minimum_counted_arrivals,
                "cost_comparison": cost_comparison,
                "cost_ratio": cost_ratio,
                "budget_change_percent": budget_change_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_level = ActionsRulesUpdateBodyDefinitionType1TargetLevel(d.pop("target_level"))

        action = ActionsRulesUpdateBodyDefinitionType1Action(d.pop("action"))

        minimum_counted_arrivals = d.pop("minimum_counted_arrivals")

        cost_comparison = ActionsRulesUpdateBodyDefinitionType1CostComparison(d.pop("cost_comparison"))

        def _parse_cost_ratio(data: object) -> float | str:
            return cast(float | str, data)

        cost_ratio = _parse_cost_ratio(d.pop("cost_ratio"))

        budget_change_percent = d.pop("budget_change_percent")

        actions_rules_update_body_definition_type_1 = cls(
            target_level=target_level,
            action=action,
            minimum_counted_arrivals=minimum_counted_arrivals,
            cost_comparison=cost_comparison,
            cost_ratio=cost_ratio,
            budget_change_percent=budget_change_percent,
        )

        return actions_rules_update_body_definition_type_1
