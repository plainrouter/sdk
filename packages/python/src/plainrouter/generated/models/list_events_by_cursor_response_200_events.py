from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_events_by_cursor_response_200_events_data_item import ListEventsByCursorResponse200EventsDataItem


T = TypeVar("T", bound="ListEventsByCursorResponse200Events")


@_attrs_define
class ListEventsByCursorResponse200Events:
    """
    Attributes:
        data (list[ListEventsByCursorResponse200EventsDataItem]):
        path (None | str):
        per_page (int):
        next_cursor (None | str):
        next_page_url (None | str):
        prev_cursor (None | str):
        prev_page_url (None | str):
    """

    data: list[ListEventsByCursorResponse200EventsDataItem]
    path: None | str
    per_page: int
    next_cursor: None | str
    next_page_url: None | str
    prev_cursor: None | str
    prev_page_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        path: None | str
        path = self.path

        per_page = self.per_page

        next_cursor: None | str
        next_cursor = self.next_cursor

        next_page_url: None | str
        next_page_url = self.next_page_url

        prev_cursor: None | str
        prev_cursor = self.prev_cursor

        prev_page_url: None | str
        prev_page_url = self.prev_page_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "path": path,
                "per_page": per_page,
                "next_cursor": next_cursor,
                "next_page_url": next_page_url,
                "prev_cursor": prev_cursor,
                "prev_page_url": prev_page_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_by_cursor_response_200_events_data_item import (
            ListEventsByCursorResponse200EventsDataItem,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListEventsByCursorResponse200EventsDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path = _parse_path(d.pop("path"))

        per_page = d.pop("per_page")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        def _parse_next_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page_url = _parse_next_page_url(d.pop("next_page_url"))

        def _parse_prev_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_cursor = _parse_prev_cursor(d.pop("prev_cursor"))

        def _parse_prev_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_page_url = _parse_prev_page_url(d.pop("prev_page_url"))

        list_events_by_cursor_response_200_events = cls(
            data=data,
            path=path,
            per_page=per_page,
            next_cursor=next_cursor,
            next_page_url=next_page_url,
            prev_cursor=prev_cursor,
            prev_page_url=prev_page_url,
        )

        list_events_by_cursor_response_200_events.additional_properties = d
        return list_events_by_cursor_response_200_events

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
