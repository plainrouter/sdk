from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.action_proposal_input_actions_item_type_12_params_status import (
    ActionProposalInputActionsItemType12ParamsStatus,
)

T = TypeVar("T", bound="ActionProposalInputActionsItemType12Params")


@_attrs_define
class ActionProposalInputActionsItemType12Params:
    """
    Attributes:
        status (ActionProposalInputActionsItemType12ParamsStatus):
    """

    status: ActionProposalInputActionsItemType12ParamsStatus

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ActionProposalInputActionsItemType12ParamsStatus(d.pop("status"))

        action_proposal_input_actions_item_type_12_params = cls(
            status=status,
        )

        return action_proposal_input_actions_item_type_12_params
