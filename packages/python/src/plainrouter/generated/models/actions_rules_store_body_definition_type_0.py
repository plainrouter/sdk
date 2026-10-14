from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.actions_rules_store_body_definition_type_0_action import ActionsRulesStoreBodyDefinitionType0Action
from ..models.actions_rules_store_body_definition_type_0_cost_comparison import (
    ActionsRulesStoreBodyDefinitionType0CostComparison,
)
from ..models.actions_rules_store_body_definition_type_0_target_level import (
    ActionsRulesStoreBodyDefinitionType0TargetLevel,
)

T = TypeVar("T", bound="ActionsRulesStoreBodyDefinitionType0")


@_attrs_define
class ActionsRulesStoreBodyDefinitionType0:
    """Only target_level, action, budget_change_percent, minimum_counted_arrivals, cost_comparison and cost_ratio are
    accepted.

        Attributes:
            target_level (ActionsRulesStoreBodyDefinitionType0TargetLevel):
            action (ActionsRulesStoreBodyDefinitionType0Action):
            minimum_counted_arrivals (int):
            cost_comparison (ActionsRulesStoreBodyDefinitionType0CostComparison):
            cost_ratio (float | str): Numeric value from 0.10 to 10.00, with zero to two decimal places.
    """

    target_level: ActionsRulesStoreBodyDefinitionType0TargetLevel
    action: ActionsRulesStoreBodyDefinitionType0Action
    minimum_counted_arrivals: int
    cost_comparison: ActionsRulesStoreBodyDefinitionType0CostComparison
    cost_ratio: float | str

    def to_dict(self) -> dict[str, Any]:
        target_level = self.target_level.value

        action = self.action.value

        minimum_counted_arrivals = self.minimum_counted_arrivals

        cost_comparison = self.cost_comparison.value

        cost_ratio: float | str
        cost_ratio = self.cost_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_level": target_level,
                "action": action,
                "minimum_counted_arrivals": minimum_counted_arrivals,
                "cost_comparison": cost_comparison,
                "cost_ratio": cost_ratio,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_level = ActionsRulesStoreBodyDefinitionType0TargetLevel(d.pop("target_level"))

        action = ActionsRulesStoreBodyDefinitionType0Action(d.pop("action"))

        minimum_counted_arrivals = d.pop("minimum_counted_arrivals")

        cost_comparison = ActionsRulesStoreBodyDefinitionType0CostComparison(d.pop("cost_comparison"))

        def _parse_cost_ratio(data: object) -> float | str:
            return cast(float | str, data)

        cost_ratio = _parse_cost_ratio(d.pop("cost_ratio"))

        actions_rules_store_body_definition_type_0 = cls(
            target_level=target_level,
            action=action,
            minimum_counted_arrivals=minimum_counted_arrivals,
            cost_comparison=cost_comparison,
            cost_ratio=cost_ratio,
        )

        return actions_rules_store_body_definition_type_0
