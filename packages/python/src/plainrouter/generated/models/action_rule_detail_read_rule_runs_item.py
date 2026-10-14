from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_rule_detail_read_rule_runs_item_decisions_item import (
        ActionRuleDetailReadRuleRunsItemDecisionsItem,
    )


T = TypeVar("T", bound="ActionRuleDetailReadRuleRunsItem")


@_attrs_define
class ActionRuleDetailReadRuleRunsItem:
    """
    Attributes:
        id (str):
        revision_id (str):
        window_start (datetime.datetime):
        window_end (datetime.datetime):
        timezone (str):
        status (str):
        reason (None | str):
        account_spend_minor (None | str):
        account_counted_arrivals (int | None):
        evaluated_at (datetime.datetime | None):
        decisions (list[ActionRuleDetailReadRuleRunsItemDecisionsItem]):
        decisions_truncated (bool):
    """

    id: str
    revision_id: str
    window_start: datetime.datetime
    window_end: datetime.datetime
    timezone: str
    status: str
    reason: None | str
    account_spend_minor: None | str
    account_counted_arrivals: int | None
    evaluated_at: datetime.datetime | None
    decisions: list[ActionRuleDetailReadRuleRunsItemDecisionsItem]
    decisions_truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision_id = self.revision_id

        window_start = self.window_start.isoformat()

        window_end = self.window_end.isoformat()

        timezone = self.timezone

        status = self.status

        reason: None | str
        reason = self.reason

        account_spend_minor: None | str
        account_spend_minor = self.account_spend_minor

        account_counted_arrivals: int | None
        account_counted_arrivals = self.account_counted_arrivals

        evaluated_at: None | str
        if isinstance(self.evaluated_at, datetime.datetime):
            evaluated_at = self.evaluated_at.isoformat()
        else:
            evaluated_at = self.evaluated_at

        decisions = []
        for decisions_item_data in self.decisions:
            decisions_item = decisions_item_data.to_dict()
            decisions.append(decisions_item)

        decisions_truncated = self.decisions_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "revision_id": revision_id,
                "window_start": window_start,
                "window_end": window_end,
                "timezone": timezone,
                "status": status,
                "reason": reason,
                "account_spend_minor": account_spend_minor,
                "account_counted_arrivals": account_counted_arrivals,
                "evaluated_at": evaluated_at,
                "decisions": decisions,
                "decisions_truncated": decisions_truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_rule_detail_read_rule_runs_item_decisions_item import (
            ActionRuleDetailReadRuleRunsItemDecisionsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        revision_id = d.pop("revision_id")

        window_start = datetime.datetime.fromisoformat(d.pop("window_start"))

        window_end = datetime.datetime.fromisoformat(d.pop("window_end"))

        timezone = d.pop("timezone")

        status = d.pop("status")

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_account_spend_minor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_spend_minor = _parse_account_spend_minor(d.pop("account_spend_minor"))

        def _parse_account_counted_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_counted_arrivals = _parse_account_counted_arrivals(d.pop("account_counted_arrivals"))

        def _parse_evaluated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                evaluated_at_type_0 = datetime.datetime.fromisoformat(data)

                return evaluated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        evaluated_at = _parse_evaluated_at(d.pop("evaluated_at"))

        decisions = []
        _decisions = d.pop("decisions")
        for decisions_item_data in _decisions:
            decisions_item = ActionRuleDetailReadRuleRunsItemDecisionsItem.from_dict(decisions_item_data)

            decisions.append(decisions_item)

        decisions_truncated = d.pop("decisions_truncated")

        action_rule_detail_read_rule_runs_item = cls(
            id=id,
            revision_id=revision_id,
            window_start=window_start,
            window_end=window_end,
            timezone=timezone,
            status=status,
            reason=reason,
            account_spend_minor=account_spend_minor,
            account_counted_arrivals=account_counted_arrivals,
            evaluated_at=evaluated_at,
            decisions=decisions,
            decisions_truncated=decisions_truncated,
        )

        action_rule_detail_read_rule_runs_item.additional_properties = d
        return action_rule_detail_read_rule_runs_item

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
