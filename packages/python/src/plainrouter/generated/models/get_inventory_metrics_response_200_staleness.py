from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200Staleness")


@_attrs_define
class GetInventoryMetricsResponse200Staleness:
    """
    Attributes:
        structure_synced_at (None | str):
        metrics_synced_at (None | str):
        last_error_code (None | str):
        state (str):
    """

    structure_synced_at: None | str
    metrics_synced_at: None | str
    last_error_code: None | str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structure_synced_at: None | str
        structure_synced_at = self.structure_synced_at

        metrics_synced_at: None | str
        metrics_synced_at = self.metrics_synced_at

        last_error_code: None | str
        last_error_code = self.last_error_code

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structure_synced_at": structure_synced_at,
                "metrics_synced_at": metrics_synced_at,
                "last_error_code": last_error_code,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_structure_synced_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        structure_synced_at = _parse_structure_synced_at(d.pop("structure_synced_at"))

        def _parse_metrics_synced_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        metrics_synced_at = _parse_metrics_synced_at(d.pop("metrics_synced_at"))

        def _parse_last_error_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error_code = _parse_last_error_code(d.pop("last_error_code"))

        state = d.pop("state")

        get_inventory_metrics_response_200_staleness = cls(
            structure_synced_at=structure_synced_at,
            metrics_synced_at=metrics_synced_at,
            last_error_code=last_error_code,
            state=state,
        )

        get_inventory_metrics_response_200_staleness.additional_properties = d
        return get_inventory_metrics_response_200_staleness

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
