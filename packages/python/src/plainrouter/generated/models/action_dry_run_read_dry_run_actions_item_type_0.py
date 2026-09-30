from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_dry_run_read_dry_run_actions_item_type_0_policy_decision import (
    ActionDryRunReadDryRunActionsItemType0PolicyDecision,
)
from ..models.action_dry_run_read_dry_run_actions_item_type_0_status import ActionDryRunReadDryRunActionsItemType0Status
from ..models.action_dry_run_read_dry_run_actions_item_type_0_type import ActionDryRunReadDryRunActionsItemType0Type

if TYPE_CHECKING:
    from ..models.action_dry_run_read_dry_run_actions_item_type_0_diff import ActionDryRunReadDryRunActionsItemType0Diff
    from ..models.action_dry_run_read_dry_run_actions_item_type_0_target_entity import (
        ActionDryRunReadDryRunActionsItemType0TargetEntity,
    )


T = TypeVar("T", bound="ActionDryRunReadDryRunActionsItemType0")


@_attrs_define
class ActionDryRunReadDryRunActionsItemType0:
    """
    Attributes:
        type_ (ActionDryRunReadDryRunActionsItemType0Type):
        target_entity (ActionDryRunReadDryRunActionsItemType0TargetEntity):
        status (ActionDryRunReadDryRunActionsItemType0Status):
        policy_decision (ActionDryRunReadDryRunActionsItemType0PolicyDecision):
        policy_reasons (list[str]):
        approval_required (bool):
        would_auto_execute (bool):
        diff (ActionDryRunReadDryRunActionsItemType0Diff):
    """

    type_: ActionDryRunReadDryRunActionsItemType0Type
    target_entity: ActionDryRunReadDryRunActionsItemType0TargetEntity
    status: ActionDryRunReadDryRunActionsItemType0Status
    policy_decision: ActionDryRunReadDryRunActionsItemType0PolicyDecision
    policy_reasons: list[str]
    approval_required: bool
    would_auto_execute: bool
    diff: ActionDryRunReadDryRunActionsItemType0Diff
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        target_entity = self.target_entity.to_dict()

        status = self.status.value

        policy_decision = self.policy_decision.value

        policy_reasons = self.policy_reasons

        approval_required = self.approval_required

        would_auto_execute = self.would_auto_execute

        diff = self.diff.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "target_entity": target_entity,
                "status": status,
                "policy_decision": policy_decision,
                "policy_reasons": policy_reasons,
                "approval_required": approval_required,
                "would_auto_execute": would_auto_execute,
                "diff": diff,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dry_run_read_dry_run_actions_item_type_0_diff import (
            ActionDryRunReadDryRunActionsItemType0Diff,
        )
        from ..models.action_dry_run_read_dry_run_actions_item_type_0_target_entity import (
            ActionDryRunReadDryRunActionsItemType0TargetEntity,
        )

        d = dict(src_dict)
        type_ = ActionDryRunReadDryRunActionsItemType0Type(d.pop("type"))

        target_entity = ActionDryRunReadDryRunActionsItemType0TargetEntity.from_dict(d.pop("target_entity"))

        status = ActionDryRunReadDryRunActionsItemType0Status(d.pop("status"))

        policy_decision = ActionDryRunReadDryRunActionsItemType0PolicyDecision(d.pop("policy_decision"))

        policy_reasons = cast(list[str], d.pop("policy_reasons"))

        approval_required = d.pop("approval_required")

        would_auto_execute = d.pop("would_auto_execute")

        diff = ActionDryRunReadDryRunActionsItemType0Diff.from_dict(d.pop("diff"))

        action_dry_run_read_dry_run_actions_item_type_0 = cls(
            type_=type_,
            target_entity=target_entity,
            status=status,
            policy_decision=policy_decision,
            policy_reasons=policy_reasons,
            approval_required=approval_required,
            would_auto_execute=would_auto_execute,
            diff=diff,
        )

        action_dry_run_read_dry_run_actions_item_type_0.additional_properties = d
        return action_dry_run_read_dry_run_actions_item_type_0

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
