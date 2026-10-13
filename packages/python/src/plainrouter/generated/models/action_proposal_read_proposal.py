from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_proposal_read_proposal_policy_decision import ActionProposalReadProposalPolicyDecision
from ..models.action_proposal_read_proposal_status import ActionProposalReadProposalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_proposal_read_proposal_actions_item import ActionProposalReadProposalActionsItem
    from ..models.action_proposal_read_proposal_proposed_by import ActionProposalReadProposalProposedBy


T = TypeVar("T", bound="ActionProposalReadProposal")


@_attrs_define
class ActionProposalReadProposal:
    """Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP representations. Defaults are
    bounded. Follow next_cursor with the same scope and filters. One oversized row is explicitly refused; fields are
    never silently clipped.

        Attributes:
            id (str):
            scope (Any):
            evidence_provenance (Any):
            status (ActionProposalReadProposalStatus):
            policy_decision (ActionProposalReadProposalPolicyDecision):
            policy_reasons (list[str]):
            approval_required (bool):
            inbox_url (str):
            approval_queue_url (str):
            rationale (str):
            proposed_by (ActionProposalReadProposalProposedBy):
            actions (list[ActionProposalReadProposalActionsItem]):
            next_cursor (int | None | Unset):
            truncated (bool | Unset):
            continuation (str | Unset):
            total (int | Unset):
    """

    id: str
    scope: Any
    evidence_provenance: Any
    status: ActionProposalReadProposalStatus
    policy_decision: ActionProposalReadProposalPolicyDecision
    policy_reasons: list[str]
    approval_required: bool
    inbox_url: str
    approval_queue_url: str
    rationale: str
    proposed_by: ActionProposalReadProposalProposedBy
    actions: list[ActionProposalReadProposalActionsItem]
    next_cursor: int | None | Unset = UNSET
    truncated: bool | Unset = UNSET
    continuation: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scope = self.scope

        evidence_provenance = self.evidence_provenance

        status = self.status.value

        policy_decision = self.policy_decision.value

        policy_reasons = self.policy_reasons

        approval_required = self.approval_required

        inbox_url = self.inbox_url

        approval_queue_url = self.approval_queue_url

        rationale = self.rationale

        proposed_by = self.proposed_by.to_dict()

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        truncated = self.truncated

        continuation = self.continuation

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scope": scope,
                "evidence_provenance": evidence_provenance,
                "status": status,
                "policy_decision": policy_decision,
                "policy_reasons": policy_reasons,
                "approval_required": approval_required,
                "inbox_url": inbox_url,
                "approval_queue_url": approval_queue_url,
                "rationale": rationale,
                "proposed_by": proposed_by,
                "actions": actions,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if continuation is not UNSET:
            field_dict["continuation"] = continuation
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_proposal_read_proposal_actions_item import ActionProposalReadProposalActionsItem
        from ..models.action_proposal_read_proposal_proposed_by import ActionProposalReadProposalProposedBy

        d = dict(src_dict)
        id = d.pop("id")

        scope = d.pop("scope")

        evidence_provenance = d.pop("evidence_provenance")

        status = ActionProposalReadProposalStatus(d.pop("status"))

        policy_decision = ActionProposalReadProposalPolicyDecision(d.pop("policy_decision"))

        policy_reasons = cast(list[str], d.pop("policy_reasons"))

        approval_required = d.pop("approval_required")

        inbox_url = d.pop("inbox_url")

        approval_queue_url = d.pop("approval_queue_url")

        rationale = d.pop("rationale")

        proposed_by = ActionProposalReadProposalProposedBy.from_dict(d.pop("proposed_by"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = ActionProposalReadProposalActionsItem.from_dict(actions_item_data)

            actions.append(actions_item)

        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        truncated = d.pop("truncated", UNSET)

        continuation = d.pop("continuation", UNSET)

        total = d.pop("total", UNSET)

        action_proposal_read_proposal = cls(
            id=id,
            scope=scope,
            evidence_provenance=evidence_provenance,
            status=status,
            policy_decision=policy_decision,
            policy_reasons=policy_reasons,
            approval_required=approval_required,
            inbox_url=inbox_url,
            approval_queue_url=approval_queue_url,
            rationale=rationale,
            proposed_by=proposed_by,
            actions=actions,
            next_cursor=next_cursor,
            truncated=truncated,
            continuation=continuation,
            total=total,
        )

        action_proposal_read_proposal.additional_properties = d
        return action_proposal_read_proposal

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
