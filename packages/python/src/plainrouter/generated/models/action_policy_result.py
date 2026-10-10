from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_policy_result_outcome import ActionPolicyResultOutcome
from ..models.action_policy_result_phase import ActionPolicyResultPhase

T = TypeVar("T", bound="ActionPolicyResult")


@_attrs_define
class ActionPolicyResult:
    """
    Attributes:
        id (str):
        policy_id (str):
        policy_version (int):
        phase (ActionPolicyResultPhase):
        outcome (ActionPolicyResultOutcome):
        reasons (list[str]):
        reason_details (list[str] | None):
        requested_minor (int | None):
        evaluated_at (datetime.datetime):
    """

    id: str
    policy_id: str
    policy_version: int
    phase: ActionPolicyResultPhase
    outcome: ActionPolicyResultOutcome
    reasons: list[str]
    reason_details: list[str] | None
    requested_minor: int | None
    evaluated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        policy_id = self.policy_id

        policy_version = self.policy_version

        phase = self.phase.value

        outcome = self.outcome.value

        reasons = self.reasons

        reason_details: list[str] | None
        if isinstance(self.reason_details, list):
            reason_details = self.reason_details

        else:
            reason_details = self.reason_details

        requested_minor: int | None
        requested_minor = self.requested_minor

        evaluated_at = self.evaluated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy_id": policy_id,
                "policy_version": policy_version,
                "phase": phase,
                "outcome": outcome,
                "reasons": reasons,
                "reason_details": reason_details,
                "requested_minor": requested_minor,
                "evaluated_at": evaluated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        policy_id = d.pop("policy_id")

        policy_version = d.pop("policy_version")

        phase = ActionPolicyResultPhase(d.pop("phase"))

        outcome = ActionPolicyResultOutcome(d.pop("outcome"))

        reasons = cast(list[str], d.pop("reasons"))

        def _parse_reason_details(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reason_details_type_0 = cast(list[str], data)

                return reason_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        reason_details = _parse_reason_details(d.pop("reason_details"))

        def _parse_requested_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        requested_minor = _parse_requested_minor(d.pop("requested_minor"))

        evaluated_at = datetime.datetime.fromisoformat(d.pop("evaluated_at"))

        action_policy_result = cls(
            id=id,
            policy_id=policy_id,
            policy_version=policy_version,
            phase=phase,
            outcome=outcome,
            reasons=reasons,
            reason_details=reason_details,
            requested_minor=requested_minor,
            evaluated_at=evaluated_at,
        )

        action_policy_result.additional_properties = d
        return action_policy_result

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
