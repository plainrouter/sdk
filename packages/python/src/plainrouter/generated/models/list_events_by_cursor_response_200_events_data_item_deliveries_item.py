from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery_status import DeliveryStatus

if TYPE_CHECKING:
    from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_last_error_type_0 import (
        ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0,
    )
    from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_platform_response_type_0 import (
        ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0,
    )


T = TypeVar("T", bound="ListEventsByCursorResponse200EventsDataItemDeliveriesItem")


@_attrs_define
class ListEventsByCursorResponse200EventsDataItemDeliveriesItem:
    """
    Attributes:
        id (int):
        signal_tracker_id (str):
        event_id (str):
        destination_id (None | str):
        status (DeliveryStatus):
        is_test (bool):
        attempt_count (int):
        last_error (list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0 | None):
        platform_response (list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0 |
            None):
        platform_trace_id (None | str):
        next_attempt_at (None | str):
        created_at (str):
        updated_at (None | str):
    """

    id: int
    signal_tracker_id: str
    event_id: str
    destination_id: None | str
    status: DeliveryStatus
    is_test: bool
    attempt_count: int
    last_error: list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0 | None
    platform_response: list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0 | None
    platform_trace_id: None | str
    next_attempt_at: None | str
    created_at: str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_last_error_type_0 import (
            ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0,
        )
        from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_platform_response_type_0 import (
            ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0,
        )

        id = self.id

        signal_tracker_id = self.signal_tracker_id

        event_id = self.event_id

        destination_id: None | str
        destination_id = self.destination_id

        status = self.status.value

        is_test = self.is_test

        attempt_count = self.attempt_count

        last_error: dict[str, Any] | list[Any] | None
        if isinstance(self.last_error, ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0):
            last_error = self.last_error.to_dict()
        elif isinstance(self.last_error, list):
            last_error = self.last_error

        else:
            last_error = self.last_error

        platform_response: dict[str, Any] | list[Any] | None
        if isinstance(
            self.platform_response, ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0
        ):
            platform_response = self.platform_response.to_dict()
        elif isinstance(self.platform_response, list):
            platform_response = self.platform_response

        else:
            platform_response = self.platform_response

        platform_trace_id: None | str
        platform_trace_id = self.platform_trace_id

        next_attempt_at: None | str
        next_attempt_at = self.next_attempt_at

        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "event_id": event_id,
                "destination_id": destination_id,
                "status": status,
                "is_test": is_test,
                "attempt_count": attempt_count,
                "last_error": last_error,
                "platform_response": platform_response,
                "platform_trace_id": platform_trace_id,
                "next_attempt_at": next_attempt_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_last_error_type_0 import (
            ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0,
        )
        from ..models.list_events_by_cursor_response_200_events_data_item_deliveries_item_platform_response_type_0 import (
            ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        event_id = d.pop("event_id")

        def _parse_destination_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        destination_id = _parse_destination_id(d.pop("destination_id"))

        status = DeliveryStatus(d.pop("status"))

        is_test = d.pop("is_test")

        attempt_count = d.pop("attempt_count")

        def _parse_last_error(
            data: object,
        ) -> list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_error_type_0 = ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0.from_dict(
                    data
                )

                return last_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                last_error_type_1 = cast(list[Any], data)

                return last_error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemLastErrorType0 | None, data
            )

        last_error = _parse_last_error(d.pop("last_error"))

        def _parse_platform_response(
            data: object,
        ) -> list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_response_type_0 = (
                    ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0.from_dict(data)
                )

                return platform_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platform_response_type_1 = cast(list[Any], data)

                return platform_response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[Any] | ListEventsByCursorResponse200EventsDataItemDeliveriesItemPlatformResponseType0 | None, data
            )

        platform_response = _parse_platform_response(d.pop("platform_response"))

        def _parse_platform_trace_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        platform_trace_id = _parse_platform_trace_id(d.pop("platform_trace_id"))

        def _parse_next_attempt_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        created_at = d.pop("created_at")

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        list_events_by_cursor_response_200_events_data_item_deliveries_item = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            event_id=event_id,
            destination_id=destination_id,
            status=status,
            is_test=is_test,
            attempt_count=attempt_count,
            last_error=last_error,
            platform_response=platform_response,
            platform_trace_id=platform_trace_id,
            next_attempt_at=next_attempt_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        list_events_by_cursor_response_200_events_data_item_deliveries_item.additional_properties = d
        return list_events_by_cursor_response_200_events_data_item_deliveries_item

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
