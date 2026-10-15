from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ActionProposalInputActionsItemType8Params")


@_attrs_define
class ActionProposalInputActionsItemType8Params:
    """ """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        action_proposal_input_actions_item_type_8_params = cls()

        return action_proposal_input_actions_item_type_8_params
