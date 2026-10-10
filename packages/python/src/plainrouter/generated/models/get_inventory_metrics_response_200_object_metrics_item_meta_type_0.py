from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200ObjectMetricsItemMetaType0")


@_attrs_define
class GetInventoryMetricsResponse200ObjectMetricsItemMetaType0:
    """
    Attributes:
        account_currency (str):
        spend (str):
        impressions (int):
        clicks (int):
        inline_link_clicks (int):
    """

    account_currency: str
    spend: str
    impressions: int
    clicks: int
    inline_link_clicks: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_currency = self.account_currency

        spend = self.spend

        impressions = self.impressions

        clicks = self.clicks

        inline_link_clicks = self.inline_link_clicks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_currency": account_currency,
                "spend": spend,
                "impressions": impressions,
                "clicks": clicks,
                "inline_link_clicks": inline_link_clicks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_currency = d.pop("account_currency")

        spend = d.pop("spend")

        impressions = d.pop("impressions")

        clicks = d.pop("clicks")

        inline_link_clicks = d.pop("inline_link_clicks")

        get_inventory_metrics_response_200_object_metrics_item_meta_type_0 = cls(
            account_currency=account_currency,
            spend=spend,
            impressions=impressions,
            clicks=clicks,
            inline_link_clicks=inline_link_clicks,
        )

        get_inventory_metrics_response_200_object_metrics_item_meta_type_0.additional_properties = d
        return get_inventory_metrics_response_200_object_metrics_item_meta_type_0

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
