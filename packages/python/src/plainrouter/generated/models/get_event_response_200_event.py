from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_event_response_200_event_click_ids_type_0 import GetEventResponse200EventClickIdsType0
    from ..models.get_event_response_200_event_consent_type_0 import GetEventResponse200EventConsentType0
    from ..models.get_event_response_200_event_deliveries_item import GetEventResponse200EventDeliveriesItem
    from ..models.get_event_response_200_event_session_type_0 import GetEventResponse200EventSessionType0
    from ..models.get_event_response_200_event_user_data_hashed_type_0 import (
        GetEventResponse200EventUserDataHashedType0,
    )
    from ..models.get_event_response_200_event_value_data_type_0 import GetEventResponse200EventValueDataType0


T = TypeVar("T", bound="GetEventResponse200Event")


@_attrs_define
class GetEventResponse200Event:
    """
    Attributes:
        id (str):
        signal_tracker_id (str):
        parent_event_id (None | str):
        event_name (str):
        event_time (str):
        action_source (str):
        event_class (str):
        order_id (None | str):
        value_amount (int | None):
        value_currency (None | str):
        created_at (str):
        consent (GetEventResponse200EventConsentType0 | list[Any] | None):
        user_data_hashed (GetEventResponse200EventUserDataHashedType0 | list[Any] | None):
        click_ids (GetEventResponse200EventClickIdsType0 | list[Any] | None):
        session (GetEventResponse200EventSessionType0 | list[Any] | None):
        value_data (GetEventResponse200EventValueDataType0 | list[Any] | None):
        event_source (None | str):
        payload_expired (bool):
        deliveries (list[GetEventResponse200EventDeliveriesItem]):
    """

    id: str
    signal_tracker_id: str
    parent_event_id: None | str
    event_name: str
    event_time: str
    action_source: str
    event_class: str
    order_id: None | str
    value_amount: int | None
    value_currency: None | str
    created_at: str
    consent: GetEventResponse200EventConsentType0 | list[Any] | None
    user_data_hashed: GetEventResponse200EventUserDataHashedType0 | list[Any] | None
    click_ids: GetEventResponse200EventClickIdsType0 | list[Any] | None
    session: GetEventResponse200EventSessionType0 | list[Any] | None
    value_data: GetEventResponse200EventValueDataType0 | list[Any] | None
    event_source: None | str
    payload_expired: bool
    deliveries: list[GetEventResponse200EventDeliveriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_event_response_200_event_click_ids_type_0 import GetEventResponse200EventClickIdsType0
        from ..models.get_event_response_200_event_consent_type_0 import GetEventResponse200EventConsentType0
        from ..models.get_event_response_200_event_session_type_0 import GetEventResponse200EventSessionType0
        from ..models.get_event_response_200_event_user_data_hashed_type_0 import (
            GetEventResponse200EventUserDataHashedType0,
        )
        from ..models.get_event_response_200_event_value_data_type_0 import GetEventResponse200EventValueDataType0

        id = self.id

        signal_tracker_id = self.signal_tracker_id

        parent_event_id: None | str
        parent_event_id = self.parent_event_id

        event_name = self.event_name

        event_time = self.event_time

        action_source = self.action_source

        event_class = self.event_class

        order_id: None | str
        order_id = self.order_id

        value_amount: int | None
        value_amount = self.value_amount

        value_currency: None | str
        value_currency = self.value_currency

        created_at = self.created_at

        consent: dict[str, Any] | list[Any] | None
        if isinstance(self.consent, GetEventResponse200EventConsentType0):
            consent = self.consent.to_dict()
        elif isinstance(self.consent, list):
            consent = self.consent

        else:
            consent = self.consent

        user_data_hashed: dict[str, Any] | list[Any] | None
        if isinstance(self.user_data_hashed, GetEventResponse200EventUserDataHashedType0):
            user_data_hashed = self.user_data_hashed.to_dict()
        elif isinstance(self.user_data_hashed, list):
            user_data_hashed = self.user_data_hashed

        else:
            user_data_hashed = self.user_data_hashed

        click_ids: dict[str, Any] | list[Any] | None
        if isinstance(self.click_ids, GetEventResponse200EventClickIdsType0):
            click_ids = self.click_ids.to_dict()
        elif isinstance(self.click_ids, list):
            click_ids = self.click_ids

        else:
            click_ids = self.click_ids

        session: dict[str, Any] | list[Any] | None
        if isinstance(self.session, GetEventResponse200EventSessionType0):
            session = self.session.to_dict()
        elif isinstance(self.session, list):
            session = self.session

        else:
            session = self.session

        value_data: dict[str, Any] | list[Any] | None
        if isinstance(self.value_data, GetEventResponse200EventValueDataType0):
            value_data = self.value_data.to_dict()
        elif isinstance(self.value_data, list):
            value_data = self.value_data

        else:
            value_data = self.value_data

        event_source: None | str
        event_source = self.event_source

        payload_expired = self.payload_expired

        deliveries = []
        for deliveries_item_data in self.deliveries:
            deliveries_item = deliveries_item_data.to_dict()
            deliveries.append(deliveries_item)

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
        from ..models.get_event_response_200_event_click_ids_type_0 import GetEventResponse200EventClickIdsType0
        from ..models.get_event_response_200_event_consent_type_0 import GetEventResponse200EventConsentType0
        from ..models.get_event_response_200_event_deliveries_item import GetEventResponse200EventDeliveriesItem
        from ..models.get_event_response_200_event_session_type_0 import GetEventResponse200EventSessionType0
        from ..models.get_event_response_200_event_user_data_hashed_type_0 import (
            GetEventResponse200EventUserDataHashedType0,
        )
        from ..models.get_event_response_200_event_value_data_type_0 import GetEventResponse200EventValueDataType0

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_parent_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_event_id = _parse_parent_event_id(d.pop("parent_event_id"))

        event_name = d.pop("event_name")

        event_time = d.pop("event_time")

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

        created_at = d.pop("created_at")

        def _parse_consent(data: object) -> GetEventResponse200EventConsentType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consent_type_0 = GetEventResponse200EventConsentType0.from_dict(data)

                return consent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                consent_type_1 = cast(list[Any], data)

                return consent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200EventConsentType0 | list[Any] | None, data)

        consent = _parse_consent(d.pop("consent"))

        def _parse_user_data_hashed(data: object) -> GetEventResponse200EventUserDataHashedType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_data_hashed_type_0 = GetEventResponse200EventUserDataHashedType0.from_dict(data)

                return user_data_hashed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_data_hashed_type_1 = cast(list[Any], data)

                return user_data_hashed_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200EventUserDataHashedType0 | list[Any] | None, data)

        user_data_hashed = _parse_user_data_hashed(d.pop("user_data_hashed"))

        def _parse_click_ids(data: object) -> GetEventResponse200EventClickIdsType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                click_ids_type_0 = GetEventResponse200EventClickIdsType0.from_dict(data)

                return click_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                click_ids_type_1 = cast(list[Any], data)

                return click_ids_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200EventClickIdsType0 | list[Any] | None, data)

        click_ids = _parse_click_ids(d.pop("click_ids"))

        def _parse_session(data: object) -> GetEventResponse200EventSessionType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_type_0 = GetEventResponse200EventSessionType0.from_dict(data)

                return session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                session_type_1 = cast(list[Any], data)

                return session_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200EventSessionType0 | list[Any] | None, data)

        session = _parse_session(d.pop("session"))

        def _parse_value_data(data: object) -> GetEventResponse200EventValueDataType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_data_type_0 = GetEventResponse200EventValueDataType0.from_dict(data)

                return value_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_data_type_1 = cast(list[Any], data)

                return value_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200EventValueDataType0 | list[Any] | None, data)

        value_data = _parse_value_data(d.pop("value_data"))

        def _parse_event_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_source = _parse_event_source(d.pop("event_source"))

        payload_expired = d.pop("payload_expired")

        deliveries = []
        _deliveries = d.pop("deliveries")
        for deliveries_item_data in _deliveries:
            deliveries_item = GetEventResponse200EventDeliveriesItem.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        get_event_response_200_event = cls(
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

        get_event_response_200_event.additional_properties = d
        return get_event_response_200_event

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
