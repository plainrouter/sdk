from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ActionProposalInputActionsItemType0Params")


@_attrs_define
class ActionProposalInputActionsItemType0Params:
    """
    Attributes:
        new_daily_budget_minor (int):
    """

    new_daily_budget_minor: int

    def to_dict(self) -> dict[str, Any]:
        new_daily_budget_minor = self.new_daily_budget_minor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "new_daily_budget_minor": new_daily_budget_minor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_daily_budget_minor = d.pop("new_daily_budget_minor")

        action_proposal_input_actions_item_type_0_params = cls(
            new_daily_budget_minor=new_daily_budget_minor,
        )

        return action_proposal_input_actions_item_type_0_params
