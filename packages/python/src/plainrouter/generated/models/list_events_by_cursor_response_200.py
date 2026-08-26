from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_events_by_cursor_response_200_events import ListEventsByCursorResponse200Events
    from ..models.list_events_by_cursor_response_200_metrics import ListEventsByCursorResponse200Metrics


T = TypeVar("T", bound="ListEventsByCursorResponse200")


@_attrs_define
class ListEventsByCursorResponse200:
    """
    Attributes:
        events (ListEventsByCursorResponse200Events):
        metrics (ListEventsByCursorResponse200Metrics):
    """

    events: ListEventsByCursorResponse200Events
    metrics: ListEventsByCursorResponse200Metrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events.to_dict()

        metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_by_cursor_response_200_events import ListEventsByCursorResponse200Events
        from ..models.list_events_by_cursor_response_200_metrics import ListEventsByCursorResponse200Metrics

        d = dict(src_dict)
        events = ListEventsByCursorResponse200Events.from_dict(d.pop("events"))

        metrics = ListEventsByCursorResponse200Metrics.from_dict(d.pop("metrics"))

        list_events_by_cursor_response_200 = cls(
            events=events,
            metrics=metrics,
        )

        list_events_by_cursor_response_200.additional_properties = d
        return list_events_by_cursor_response_200

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
