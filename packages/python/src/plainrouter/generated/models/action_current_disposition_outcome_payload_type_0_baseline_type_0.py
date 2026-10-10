from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_current_disposition_outcome_payload_type_0_baseline_type_0_scope import (
    ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionCurrentDispositionOutcomePayloadType0BaselineType0")


@_attrs_define
class ActionCurrentDispositionOutcomePayloadType0BaselineType0:
    """
    Attributes:
        scope (ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope | Unset):
        days (list[datetime.date] | Unset): Three whole days in the ad account timezone; excludes the change day.
        currency (None | str | Unset):
        timezone (str | Unset):
        spend_minor (None | str | Unset): Decimal spend in ISO currency minor units; null when daily mirror data is
            missing.
        counted_arrivals (int | None | Unset): Arrivals counted by PlainRouter through Signals, never provider
            conversions.
        cost_per_counted_arrival_minor (None | str | Unset): Spend divided by counted arrivals, in ISO currency minor
            units, displayed to six decimal places.
    """

    scope: ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope | Unset = UNSET
    days: list[datetime.date] | Unset = UNSET
    currency: None | str | Unset = UNSET
    timezone: str | Unset = UNSET
    spend_minor: None | str | Unset = UNSET
    counted_arrivals: int | None | Unset = UNSET
    cost_per_counted_arrival_minor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.isoformat()
                days.append(days_item)

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        timezone = self.timezone

        spend_minor: None | str | Unset
        if isinstance(self.spend_minor, Unset):
            spend_minor = UNSET
        else:
            spend_minor = self.spend_minor

        counted_arrivals: int | None | Unset
        if isinstance(self.counted_arrivals, Unset):
            counted_arrivals = UNSET
        else:
            counted_arrivals = self.counted_arrivals

        cost_per_counted_arrival_minor: None | str | Unset
        if isinstance(self.cost_per_counted_arrival_minor, Unset):
            cost_per_counted_arrival_minor = UNSET
        else:
            cost_per_counted_arrival_minor = self.cost_per_counted_arrival_minor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if days is not UNSET:
            field_dict["days"] = days
        if currency is not UNSET:
            field_dict["currency"] = currency
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if spend_minor is not UNSET:
            field_dict["spend_minor"] = spend_minor
        if counted_arrivals is not UNSET:
            field_dict["counted_arrivals"] = counted_arrivals
        if cost_per_counted_arrival_minor is not UNSET:
            field_dict["cost_per_counted_arrival_minor"] = cost_per_counted_arrival_minor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope(_scope)

        _days = d.pop("days", UNSET)
        days: list[datetime.date] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = datetime.date.fromisoformat(days_item_data)

                days.append(days_item)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        timezone = d.pop("timezone", UNSET)

        def _parse_spend_minor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spend_minor = _parse_spend_minor(d.pop("spend_minor", UNSET))

        def _parse_counted_arrivals(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        counted_arrivals = _parse_counted_arrivals(d.pop("counted_arrivals", UNSET))

        def _parse_cost_per_counted_arrival_minor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_per_counted_arrival_minor = _parse_cost_per_counted_arrival_minor(
            d.pop("cost_per_counted_arrival_minor", UNSET)
        )

        action_current_disposition_outcome_payload_type_0_baseline_type_0 = cls(
            scope=scope,
            days=days,
            currency=currency,
            timezone=timezone,
            spend_minor=spend_minor,
            counted_arrivals=counted_arrivals,
            cost_per_counted_arrival_minor=cost_per_counted_arrival_minor,
        )

        action_current_disposition_outcome_payload_type_0_baseline_type_0.additional_properties = d
        return action_current_disposition_outcome_payload_type_0_baseline_type_0

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
