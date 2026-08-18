from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListEventsResponse200Metrics")


@_attrs_define
class ListEventsResponse200Metrics:
    """
    Attributes:
        accepted (int):
        total_deliveries (int):
        acceptance_rate (float | None):
        acceptance_rate_window (str):
    """

    accepted: int
    total_deliveries: int
    acceptance_rate: float | None
    acceptance_rate_window: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        total_deliveries = self.total_deliveries

        acceptance_rate: float | None
        acceptance_rate = self.acceptance_rate

        acceptance_rate_window = self.acceptance_rate_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "total_deliveries": total_deliveries,
                "acceptance_rate": acceptance_rate,
                "acceptance_rate_window": acceptance_rate_window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        total_deliveries = d.pop("total_deliveries")

        def _parse_acceptance_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        acceptance_rate = _parse_acceptance_rate(d.pop("acceptance_rate"))

        acceptance_rate_window = d.pop("acceptance_rate_window")

        list_events_response_200_metrics = cls(
            accepted=accepted,
            total_deliveries=total_deliveries,
            acceptance_rate=acceptance_rate,
            acceptance_rate_window=acceptance_rate_window,
        )

        list_events_response_200_metrics.additional_properties = d
        return list_events_response_200_metrics

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
