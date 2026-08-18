from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_events_response_200_events_data_item import ListEventsResponse200EventsDataItem
    from ..models.list_events_response_200_events_links_item import ListEventsResponse200EventsLinksItem


T = TypeVar("T", bound="ListEventsResponse200Events")


@_attrs_define
class ListEventsResponse200Events:
    """
    Attributes:
        current_page (int):
        data (list[ListEventsResponse200EventsDataItem]):
        first_page_url (None | str):
        from_ (int | None):
        last_page (int):
        last_page_url (None | str):
        links (list[ListEventsResponse200EventsLinksItem]):
        next_page_url (None | str):
        path (None | str):
        per_page (int):
        prev_page_url (None | str):
        to (int | None):
        total (int):
    """

    current_page: int
    data: list[ListEventsResponse200EventsDataItem]
    first_page_url: None | str
    from_: int | None
    last_page: int
    last_page_url: None | str
    links: list[ListEventsResponse200EventsLinksItem]
    next_page_url: None | str
    path: None | str
    per_page: int
    prev_page_url: None | str
    to: int | None
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        first_page_url: None | str
        first_page_url = self.first_page_url

        from_: int | None
        from_ = self.from_

        last_page = self.last_page

        last_page_url: None | str
        last_page_url = self.last_page_url

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        next_page_url: None | str
        next_page_url = self.next_page_url

        path: None | str
        path = self.path

        per_page = self.per_page

        prev_page_url: None | str
        prev_page_url = self.prev_page_url

        to: int | None
        to = self.to

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "data": data,
                "first_page_url": first_page_url,
                "from": from_,
                "last_page": last_page,
                "last_page_url": last_page_url,
                "links": links,
                "next_page_url": next_page_url,
                "path": path,
                "per_page": per_page,
                "prev_page_url": prev_page_url,
                "to": to,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_response_200_events_data_item import ListEventsResponse200EventsDataItem
        from ..models.list_events_response_200_events_links_item import ListEventsResponse200EventsLinksItem

        d = dict(src_dict)
        current_page = d.pop("current_page")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListEventsResponse200EventsDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_first_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_page_url = _parse_first_page_url(d.pop("first_page_url"))

        def _parse_from_(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        from_ = _parse_from_(d.pop("from"))

        last_page = d.pop("last_page")

        def _parse_last_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_page_url = _parse_last_page_url(d.pop("last_page_url"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = ListEventsResponse200EventsLinksItem.from_dict(links_item_data)

            links.append(links_item)

        def _parse_next_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page_url = _parse_next_page_url(d.pop("next_page_url"))

        def _parse_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path = _parse_path(d.pop("path"))

        per_page = d.pop("per_page")

        def _parse_prev_page_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_page_url = _parse_prev_page_url(d.pop("prev_page_url"))

        def _parse_to(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        to = _parse_to(d.pop("to"))

        total = d.pop("total")

        list_events_response_200_events = cls(
            current_page=current_page,
            data=data,
            first_page_url=first_page_url,
            from_=from_,
            last_page=last_page,
            last_page_url=last_page_url,
            links=links,
            next_page_url=next_page_url,
            path=path,
            per_page=per_page,
            prev_page_url=prev_page_url,
            to=to,
            total=total,
        )

        list_events_response_200_events.additional_properties = d
        return list_events_response_200_events

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
