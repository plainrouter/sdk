from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200Sync")


@_attrs_define
class GetInventoryMetricsResponse200Sync:
    """
    Attributes:
        campaigns_count (int | None):
        adsets_count (int | None):
        ads_count (int | None):
        counts_read_at (None | str):
    """

    campaigns_count: int | None
    adsets_count: int | None
    ads_count: int | None
    counts_read_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaigns_count: int | None
        campaigns_count = self.campaigns_count

        adsets_count: int | None
        adsets_count = self.adsets_count

        ads_count: int | None
        ads_count = self.ads_count

        counts_read_at: None | str
        counts_read_at = self.counts_read_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaigns_count": campaigns_count,
                "adsets_count": adsets_count,
                "ads_count": ads_count,
                "counts_read_at": counts_read_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_campaigns_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        campaigns_count = _parse_campaigns_count(d.pop("campaigns_count"))

        def _parse_adsets_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        adsets_count = _parse_adsets_count(d.pop("adsets_count"))

        def _parse_ads_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ads_count = _parse_ads_count(d.pop("ads_count"))

        def _parse_counts_read_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        counts_read_at = _parse_counts_read_at(d.pop("counts_read_at"))

        get_inventory_metrics_response_200_sync = cls(
            campaigns_count=campaigns_count,
            adsets_count=adsets_count,
            ads_count=ads_count,
            counts_read_at=counts_read_at,
        )

        get_inventory_metrics_response_200_sync.additional_properties = d
        return get_inventory_metrics_response_200_sync

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
