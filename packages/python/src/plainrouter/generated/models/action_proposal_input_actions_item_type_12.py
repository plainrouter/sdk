from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_proposal_input_actions_item_type_12_type import ActionProposalInputActionsItemType12Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_proposal_input_actions_item_type_12_params import ActionProposalInputActionsItemType12Params
    from ..models.action_proposal_input_actions_item_type_12_target_entity import (
        ActionProposalInputActionsItemType12TargetEntity,
    )


T = TypeVar("T", bound="ActionProposalInputActionsItemType12")


@_attrs_define
class ActionProposalInputActionsItemType12:
    """
    Attributes:
        type_ (ActionProposalInputActionsItemType12Type):
        target_entity (ActionProposalInputActionsItemType12TargetEntity):
        params (ActionProposalInputActionsItemType12Params):
        rationale (str):
        idempotency_key (str | Unset):
    """

    type_: ActionProposalInputActionsItemType12Type
    target_entity: ActionProposalInputActionsItemType12TargetEntity
    params: ActionProposalInputActionsItemType12Params
    rationale: str
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        target_entity = self.target_entity.to_dict()

        params = self.params.to_dict()

        rationale = self.rationale

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "target_entity": target_entity,
                "params": params,
                "rationale": rationale,
            }
        )
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_proposal_input_actions_item_type_12_params import (
            ActionProposalInputActionsItemType12Params,
        )
        from ..models.action_proposal_input_actions_item_type_12_target_entity import (
            ActionProposalInputActionsItemType12TargetEntity,
        )

        d = dict(src_dict)
        type_ = ActionProposalInputActionsItemType12Type(d.pop("type"))

        target_entity = ActionProposalInputActionsItemType12TargetEntity.from_dict(d.pop("target_entity"))

        params = ActionProposalInputActionsItemType12Params.from_dict(d.pop("params"))

        rationale = d.pop("rationale")

        idempotency_key = d.pop("idempotency_key", UNSET)

        action_proposal_input_actions_item_type_12 = cls(
            type_=type_,
            target_entity=target_entity,
            params=params,
            rationale=rationale,
            idempotency_key=idempotency_key,
        )

        action_proposal_input_actions_item_type_12.additional_properties = d
        return action_proposal_input_actions_item_type_12

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
