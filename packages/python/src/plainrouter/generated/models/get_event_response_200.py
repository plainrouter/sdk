from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_event_response_200_deliveries_item import GetEventResponse200DeliveriesItem
    from ..models.get_event_response_200_event import GetEventResponse200Event
    from ..models.get_event_response_200_lineage import GetEventResponse200Lineage


T = TypeVar("T", bound="GetEventResponse200")


@_attrs_define
class GetEventResponse200:
    """
    Attributes:
        event (GetEventResponse200Event):
        lineage (GetEventResponse200Lineage):
        deliveries (list[GetEventResponse200DeliveriesItem]):
    """

    event: GetEventResponse200Event
    lineage: GetEventResponse200Lineage
    deliveries: list[GetEventResponse200DeliveriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event.to_dict()

        lineage = self.lineage.to_dict()

        deliveries = []
        for deliveries_item_data in self.deliveries:
            deliveries_item = deliveries_item_data.to_dict()
            deliveries.append(deliveries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "lineage": lineage,
                "deliveries": deliveries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_event_response_200_deliveries_item import GetEventResponse200DeliveriesItem
        from ..models.get_event_response_200_event import GetEventResponse200Event
        from ..models.get_event_response_200_lineage import GetEventResponse200Lineage

        d = dict(src_dict)
        event = GetEventResponse200Event.from_dict(d.pop("event"))

        lineage = GetEventResponse200Lineage.from_dict(d.pop("lineage"))

        deliveries = []
        _deliveries = d.pop("deliveries")
        for deliveries_item_data in _deliveries:
            deliveries_item = GetEventResponse200DeliveriesItem.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        get_event_response_200 = cls(
            event=event,
            lineage=lineage,
            deliveries=deliveries,
        )

        get_event_response_200.additional_properties = d
        return get_event_response_200

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
