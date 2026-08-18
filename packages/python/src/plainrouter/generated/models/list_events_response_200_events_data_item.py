from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_events_response_200_events_data_item_click_ids_type_0 import (
        ListEventsResponse200EventsDataItemClickIdsType0,
    )
    from ..models.list_events_response_200_events_data_item_consent_type_0 import (
        ListEventsResponse200EventsDataItemConsentType0,
    )
    from ..models.list_events_response_200_events_data_item_deliveries_item import (
        ListEventsResponse200EventsDataItemDeliveriesItem,
    )
    from ..models.list_events_response_200_events_data_item_session_type_0 import (
        ListEventsResponse200EventsDataItemSessionType0,
    )
    from ..models.list_events_response_200_events_data_item_user_data_hashed_type_0 import (
        ListEventsResponse200EventsDataItemUserDataHashedType0,
    )
    from ..models.list_events_response_200_events_data_item_value_data_type_0 import (
        ListEventsResponse200EventsDataItemValueDataType0,
    )


T = TypeVar("T", bound="ListEventsResponse200EventsDataItem")


@_attrs_define
class ListEventsResponse200EventsDataItem:
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
        consent (list[Any] | ListEventsResponse200EventsDataItemConsentType0 | None):
        user_data_hashed (list[Any] | ListEventsResponse200EventsDataItemUserDataHashedType0 | None):
        click_ids (list[Any] | ListEventsResponse200EventsDataItemClickIdsType0 | None):
        session (list[Any] | ListEventsResponse200EventsDataItemSessionType0 | None):
        value_data (list[Any] | ListEventsResponse200EventsDataItemValueDataType0 | None):
        event_source (None | str):
        payload_expired (bool):
        deliveries (list[ListEventsResponse200EventsDataItemDeliveriesItem]):
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
    consent: list[Any] | ListEventsResponse200EventsDataItemConsentType0 | None
    user_data_hashed: list[Any] | ListEventsResponse200EventsDataItemUserDataHashedType0 | None
    click_ids: list[Any] | ListEventsResponse200EventsDataItemClickIdsType0 | None
    session: list[Any] | ListEventsResponse200EventsDataItemSessionType0 | None
    value_data: list[Any] | ListEventsResponse200EventsDataItemValueDataType0 | None
    event_source: None | str
    payload_expired: bool
    deliveries: list[ListEventsResponse200EventsDataItemDeliveriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_events_response_200_events_data_item_click_ids_type_0 import (
            ListEventsResponse200EventsDataItemClickIdsType0,
        )
        from ..models.list_events_response_200_events_data_item_consent_type_0 import (
            ListEventsResponse200EventsDataItemConsentType0,
        )
        from ..models.list_events_response_200_events_data_item_session_type_0 import (
            ListEventsResponse200EventsDataItemSessionType0,
        )
        from ..models.list_events_response_200_events_data_item_user_data_hashed_type_0 import (
            ListEventsResponse200EventsDataItemUserDataHashedType0,
        )
        from ..models.list_events_response_200_events_data_item_value_data_type_0 import (
            ListEventsResponse200EventsDataItemValueDataType0,
        )

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
        if isinstance(self.consent, ListEventsResponse200EventsDataItemConsentType0):
            consent = self.consent.to_dict()
        elif isinstance(self.consent, list):
            consent = self.consent

        else:
            consent = self.consent

        user_data_hashed: dict[str, Any] | list[Any] | None
        if isinstance(self.user_data_hashed, ListEventsResponse200EventsDataItemUserDataHashedType0):
            user_data_hashed = self.user_data_hashed.to_dict()
        elif isinstance(self.user_data_hashed, list):
            user_data_hashed = self.user_data_hashed

        else:
            user_data_hashed = self.user_data_hashed

        click_ids: dict[str, Any] | list[Any] | None
        if isinstance(self.click_ids, ListEventsResponse200EventsDataItemClickIdsType0):
            click_ids = self.click_ids.to_dict()
        elif isinstance(self.click_ids, list):
            click_ids = self.click_ids

        else:
            click_ids = self.click_ids

        session: dict[str, Any] | list[Any] | None
        if isinstance(self.session, ListEventsResponse200EventsDataItemSessionType0):
            session = self.session.to_dict()
        elif isinstance(self.session, list):
            session = self.session

        else:
            session = self.session

        value_data: dict[str, Any] | list[Any] | None
        if isinstance(self.value_data, ListEventsResponse200EventsDataItemValueDataType0):
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
        from ..models.list_events_response_200_events_data_item_click_ids_type_0 import (
            ListEventsResponse200EventsDataItemClickIdsType0,
        )
        from ..models.list_events_response_200_events_data_item_consent_type_0 import (
            ListEventsResponse200EventsDataItemConsentType0,
        )
        from ..models.list_events_response_200_events_data_item_deliveries_item import (
            ListEventsResponse200EventsDataItemDeliveriesItem,
        )
        from ..models.list_events_response_200_events_data_item_session_type_0 import (
            ListEventsResponse200EventsDataItemSessionType0,
        )
        from ..models.list_events_response_200_events_data_item_user_data_hashed_type_0 import (
            ListEventsResponse200EventsDataItemUserDataHashedType0,
        )
        from ..models.list_events_response_200_events_data_item_value_data_type_0 import (
            ListEventsResponse200EventsDataItemValueDataType0,
        )

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

        def _parse_consent(data: object) -> list[Any] | ListEventsResponse200EventsDataItemConsentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consent_type_0 = ListEventsResponse200EventsDataItemConsentType0.from_dict(data)

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
            return cast(list[Any] | ListEventsResponse200EventsDataItemConsentType0 | None, data)

        consent = _parse_consent(d.pop("consent"))

        def _parse_user_data_hashed(
            data: object,
        ) -> list[Any] | ListEventsResponse200EventsDataItemUserDataHashedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_data_hashed_type_0 = ListEventsResponse200EventsDataItemUserDataHashedType0.from_dict(data)

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
            return cast(list[Any] | ListEventsResponse200EventsDataItemUserDataHashedType0 | None, data)

        user_data_hashed = _parse_user_data_hashed(d.pop("user_data_hashed"))

        def _parse_click_ids(data: object) -> list[Any] | ListEventsResponse200EventsDataItemClickIdsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                click_ids_type_0 = ListEventsResponse200EventsDataItemClickIdsType0.from_dict(data)

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
            return cast(list[Any] | ListEventsResponse200EventsDataItemClickIdsType0 | None, data)

        click_ids = _parse_click_ids(d.pop("click_ids"))

        def _parse_session(data: object) -> list[Any] | ListEventsResponse200EventsDataItemSessionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_type_0 = ListEventsResponse200EventsDataItemSessionType0.from_dict(data)

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
            return cast(list[Any] | ListEventsResponse200EventsDataItemSessionType0 | None, data)

        session = _parse_session(d.pop("session"))

        def _parse_value_data(data: object) -> list[Any] | ListEventsResponse200EventsDataItemValueDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_data_type_0 = ListEventsResponse200EventsDataItemValueDataType0.from_dict(data)

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
            return cast(list[Any] | ListEventsResponse200EventsDataItemValueDataType0 | None, data)

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
            deliveries_item = ListEventsResponse200EventsDataItemDeliveriesItem.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        list_events_response_200_events_data_item = cls(
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

        list_events_response_200_events_data_item.additional_properties = d
        return list_events_response_200_events_data_item

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
