from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_proposal_read_proposal_actions_item_policy_decision import (
    ActionProposalReadProposalActionsItemPolicyDecision,
)
from ..models.action_proposal_read_proposal_actions_item_type import ActionProposalReadProposalActionsItemType

if TYPE_CHECKING:
    from ..models.action_proposal_read_proposal_actions_item_params_type_0 import (
        ActionProposalReadProposalActionsItemParamsType0,
    )
    from ..models.action_proposal_read_proposal_actions_item_proposed_by import (
        ActionProposalReadProposalActionsItemProposedBy,
    )
    from ..models.action_proposal_read_proposal_actions_item_target_entity import (
        ActionProposalReadProposalActionsItemTargetEntity,
    )


T = TypeVar("T", bound="ActionProposalReadProposalActionsItem")


@_attrs_define
class ActionProposalReadProposalActionsItem:
    """
    Attributes:
        id (str):
        type_ (ActionProposalReadProposalActionsItemType):
        target_entity (ActionProposalReadProposalActionsItemTargetEntity):
        params (ActionProposalReadProposalActionsItemParamsType0 | list[Any]):
        rationale (str):
        proposed_by (ActionProposalReadProposalActionsItemProposedBy):
        policy_decision (ActionProposalReadProposalActionsItemPolicyDecision):
        policy_reasons (list[str]):
        policy_evidence (Any):
    """

    id: str
    type_: ActionProposalReadProposalActionsItemType
    target_entity: ActionProposalReadProposalActionsItemTargetEntity
    params: ActionProposalReadProposalActionsItemParamsType0 | list[Any]
    rationale: str
    proposed_by: ActionProposalReadProposalActionsItemProposedBy
    policy_decision: ActionProposalReadProposalActionsItemPolicyDecision
    policy_reasons: list[str]
    policy_evidence: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_proposal_read_proposal_actions_item_params_type_0 import (
            ActionProposalReadProposalActionsItemParamsType0,
        )

        id = self.id

        type_ = self.type_.value

        target_entity = self.target_entity.to_dict()

        params: dict[str, Any] | list[Any]
        if isinstance(self.params, ActionProposalReadProposalActionsItemParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        rationale = self.rationale

        proposed_by = self.proposed_by.to_dict()

        policy_decision = self.policy_decision.value

        policy_reasons = self.policy_reasons

        policy_evidence = self.policy_evidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "target_entity": target_entity,
                "params": params,
                "rationale": rationale,
                "proposed_by": proposed_by,
                "policy_decision": policy_decision,
                "policy_reasons": policy_reasons,
                "policy_evidence": policy_evidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_proposal_read_proposal_actions_item_params_type_0 import (
            ActionProposalReadProposalActionsItemParamsType0,
        )
        from ..models.action_proposal_read_proposal_actions_item_proposed_by import (
            ActionProposalReadProposalActionsItemProposedBy,
        )
        from ..models.action_proposal_read_proposal_actions_item_target_entity import (
            ActionProposalReadProposalActionsItemTargetEntity,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = ActionProposalReadProposalActionsItemType(d.pop("type"))

        target_entity = ActionProposalReadProposalActionsItemTargetEntity.from_dict(d.pop("target_entity"))

        def _parse_params(data: object) -> ActionProposalReadProposalActionsItemParamsType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ActionProposalReadProposalActionsItemParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            params_type_1 = cast(list[Any], data)

            return params_type_1

        params = _parse_params(d.pop("params"))

        rationale = d.pop("rationale")

        proposed_by = ActionProposalReadProposalActionsItemProposedBy.from_dict(d.pop("proposed_by"))

        policy_decision = ActionProposalReadProposalActionsItemPolicyDecision(d.pop("policy_decision"))

        policy_reasons = cast(list[str], d.pop("policy_reasons"))

        policy_evidence = d.pop("policy_evidence")

        action_proposal_read_proposal_actions_item = cls(
            id=id,
            type_=type_,
            target_entity=target_entity,
            params=params,
            rationale=rationale,
            proposed_by=proposed_by,
            policy_decision=policy_decision,
            policy_reasons=policy_reasons,
            policy_evidence=policy_evidence,
        )

        action_proposal_read_proposal_actions_item.additional_properties = d
        return action_proposal_read_proposal_actions_item

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
