from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (str):
        signal_tracker_id (str):
        parent_event_id (None | str):
        event_name (str):
        event_time (datetime.datetime):
        action_source (str):
        event_class (str):
        order_id (None | str):
        value_amount (int | None):
        value_currency (None | str):
        created_at (datetime.datetime):
        consent (str):
        user_data_hashed (str):
        click_ids (str):
        session (str):
        value_data (str):
        event_source (str):
        payload_expired (bool):
        deliveries (list[Any]):
    """

    id: str
    signal_tracker_id: str
    parent_event_id: None | str
    event_name: str
    event_time: datetime.datetime
    action_source: str
    event_class: str
    order_id: None | str
    value_amount: int | None
    value_currency: None | str
    created_at: datetime.datetime
    consent: str
    user_data_hashed: str
    click_ids: str
    session: str
    value_data: str
    event_source: str
    payload_expired: bool
    deliveries: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signal_tracker_id = self.signal_tracker_id

        parent_event_id: None | str
        parent_event_id = self.parent_event_id

        event_name = self.event_name

        event_time = self.event_time.isoformat()

        action_source = self.action_source

        event_class = self.event_class

        order_id: None | str
        order_id = self.order_id

        value_amount: int | None
        value_amount = self.value_amount

        value_currency: None | str
        value_currency = self.value_currency

        created_at = self.created_at.isoformat()

        consent = self.consent

        user_data_hashed = self.user_data_hashed

        click_ids = self.click_ids

        session = self.session

        value_data = self.value_data

        event_source = self.event_source

        payload_expired = self.payload_expired

        deliveries = self.deliveries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "parent_event_id": parent_event_id,
                "event_name": event_name,
                "event_time": event_time,
                "action_source": action_source,
                "event_class": event_class,
                "order_id": order_id,
                "value_amount": value_amount,
                "value_currency": value_currency,
                "created_at": created_at,
                "consent": consent,
                "user_data_hashed": user_data_hashed,
                "click_ids": click_ids,
                "session": session,
                "value_data": value_data,
                "event_source": event_source,
                "payload_expired": payload_expired,
                "deliveries": deliveries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_parent_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_event_id = _parse_parent_event_id(d.pop("parent_event_id"))

        event_name = d.pop("event_name")

        event_time = datetime.datetime.fromisoformat(d.pop("event_time"))

        action_source = d.pop("action_source")

        event_class = d.pop("event_class")

        def _parse_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_id = _parse_order_id(d.pop("order_id"))

        def _parse_value_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        value_amount = _parse_value_amount(d.pop("value_amount"))

        def _parse_value_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value_currency = _parse_value_currency(d.pop("value_currency"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        consent = d.pop("consent")

        user_data_hashed = d.pop("user_data_hashed")

        click_ids = d.pop("click_ids")

        session = d.pop("session")

        value_data = d.pop("value_data")

        event_source = d.pop("event_source")

        payload_expired = d.pop("payload_expired")

        deliveries = cast(list[Any], d.pop("deliveries"))

        event = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            parent_event_id=parent_event_id,
            event_name=event_name,
            event_time=event_time,
            action_source=action_source,
            event_class=event_class,
            order_id=order_id,
            value_amount=value_amount,
            value_currency=value_currency,
            created_at=created_at,
            consent=consent,
            user_data_hashed=user_data_hashed,
            click_ids=click_ids,
            session=session,
            value_data=value_data,
            event_source=event_source,
            payload_expired=payload_expired,
            deliveries=deliveries,
        )

        event.additional_properties = d
        return event

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
