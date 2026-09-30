from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.action_proposal_input_actions_item_type_11_target_entity_type import (
    ActionProposalInputActionsItemType11TargetEntityType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionProposalInputActionsItemType11TargetEntity")


@_attrs_define
class ActionProposalInputActionsItemType11TargetEntity:
    """
    Attributes:
        type_ (ActionProposalInputActionsItemType11TargetEntityType):
        id (str):
        name (None | str | Unset):
    """

    type_: ActionProposalInputActionsItemType11TargetEntityType
    id: str
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ActionProposalInputActionsItemType11TargetEntityType(d.pop("type"))

        id = d.pop("id")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        action_proposal_input_actions_item_type_11_target_entity = cls(
            type_=type_,
            id=id,
            name=name,
        )

        return action_proposal_input_actions_item_type_11_target_entity
