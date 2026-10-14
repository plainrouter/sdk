from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionRuleDetailReadRuleRunsItemDecisionsItem")


@_attrs_define
class ActionRuleDetailReadRuleRunsItemDecisionsItem:
    """
    Attributes:
        id (str):
        target_type (str):
        target_id (str):
        target_name (None | str):
        target_spend_minor (str):
        target_counted_arrivals (int):
        decision (str):
        reason (str):
        action_type (str):
        new_daily_budget_minor (int | None):
        action_batch_id (None | str):
    """

    id: str
    target_type: str
    target_id: str
    target_name: None | str
    target_spend_minor: str
    target_counted_arrivals: int
    decision: str
    reason: str
    action_type: str
    new_daily_budget_minor: int | None
    action_batch_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_type = self.target_type

        target_id = self.target_id

        target_name: None | str
        target_name = self.target_name

        target_spend_minor = self.target_spend_minor

        target_counted_arrivals = self.target_counted_arrivals

        decision = self.decision

        reason = self.reason

        action_type = self.action_type

        new_daily_budget_minor: int | None
        new_daily_budget_minor = self.new_daily_budget_minor

        action_batch_id: None | str
        action_batch_id = self.action_batch_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_type": target_type,
                "target_id": target_id,
                "target_name": target_name,
                "target_spend_minor": target_spend_minor,
                "target_counted_arrivals": target_counted_arrivals,
                "decision": decision,
                "reason": reason,
                "action_type": action_type,
                "new_daily_budget_minor": new_daily_budget_minor,
                "action_batch_id": action_batch_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        target_type = d.pop("target_type")

        target_id = d.pop("target_id")

        def _parse_target_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_name = _parse_target_name(d.pop("target_name"))

        target_spend_minor = d.pop("target_spend_minor")

        target_counted_arrivals = d.pop("target_counted_arrivals")

        decision = d.pop("decision")

        reason = d.pop("reason")

        action_type = d.pop("action_type")

        def _parse_new_daily_budget_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        new_daily_budget_minor = _parse_new_daily_budget_minor(d.pop("new_daily_budget_minor"))

        def _parse_action_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        action_batch_id = _parse_action_batch_id(d.pop("action_batch_id"))

        action_rule_detail_read_rule_runs_item_decisions_item = cls(
            id=id,
            target_type=target_type,
            target_id=target_id,
            target_name=target_name,
            target_spend_minor=target_spend_minor,
            target_counted_arrivals=target_counted_arrivals,
            decision=decision,
            reason=reason,
            action_type=action_type,
            new_daily_budget_minor=new_daily_budget_minor,
            action_batch_id=action_batch_id,
        )

        action_rule_detail_read_rule_runs_item_decisions_item.additional_properties = d
        return action_rule_detail_read_rule_runs_item_decisions_item

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
