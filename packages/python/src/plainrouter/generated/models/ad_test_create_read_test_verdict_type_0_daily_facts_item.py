from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdTestCreateReadTestVerdictType0DailyFactsItem")


@_attrs_define
class AdTestCreateReadTestVerdictType0DailyFactsItem:
    """
    Attributes:
        date (datetime.date):
        ad_test_member_id (str):
        ad_id (str):
        spend_minor (str): Exact spend in Meta minor units for the account currency, including any stored fractional
            component.
        spend (None | str): Account-currency spend in major units.
        impressions (int | None):
        counted_arrivals (int | None):
        recorded_conversions (int | None):
        admitted_conversions (int | None):
        inline_link_clicks (int | None | Unset):
    """

    date: datetime.date
    ad_test_member_id: str
    ad_id: str
    spend_minor: str
    spend: None | str
    impressions: int | None
    counted_arrivals: int | None
    recorded_conversions: int | None
    admitted_conversions: int | None
    inline_link_clicks: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        ad_test_member_id = self.ad_test_member_id

        ad_id = self.ad_id

        spend_minor = self.spend_minor

        spend: None | str
        spend = self.spend

        impressions: int | None
        impressions = self.impressions

        counted_arrivals: int | None
        counted_arrivals = self.counted_arrivals

        recorded_conversions: int | None
        recorded_conversions = self.recorded_conversions

        admitted_conversions: int | None
        admitted_conversions = self.admitted_conversions

        inline_link_clicks: int | None | Unset
        if isinstance(self.inline_link_clicks, Unset):
            inline_link_clicks = UNSET
        else:
            inline_link_clicks = self.inline_link_clicks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "ad_test_member_id": ad_test_member_id,
                "ad_id": ad_id,
                "spend_minor": spend_minor,
                "spend": spend,
                "impressions": impressions,
                "counted_arrivals": counted_arrivals,
                "recorded_conversions": recorded_conversions,
                "admitted_conversions": admitted_conversions,
            }
        )
        if inline_link_clicks is not UNSET:
            field_dict["inline_link_clicks"] = inline_link_clicks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        ad_test_member_id = d.pop("ad_test_member_id")

        ad_id = d.pop("ad_id")

        spend_minor = d.pop("spend_minor")

        def _parse_spend(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        spend = _parse_spend(d.pop("spend"))

        def _parse_impressions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        impressions = _parse_impressions(d.pop("impressions"))

        def _parse_counted_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        counted_arrivals = _parse_counted_arrivals(d.pop("counted_arrivals"))

        def _parse_recorded_conversions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        recorded_conversions = _parse_recorded_conversions(d.pop("recorded_conversions"))

        def _parse_admitted_conversions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        admitted_conversions = _parse_admitted_conversions(d.pop("admitted_conversions"))

        def _parse_inline_link_clicks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inline_link_clicks = _parse_inline_link_clicks(d.pop("inline_link_clicks", UNSET))

        ad_test_create_read_test_verdict_type_0_daily_facts_item = cls(
            date=date,
            ad_test_member_id=ad_test_member_id,
            ad_id=ad_id,
            spend_minor=spend_minor,
            spend=spend,
            impressions=impressions,
            counted_arrivals=counted_arrivals,
            recorded_conversions=recorded_conversions,
            admitted_conversions=admitted_conversions,
            inline_link_clicks=inline_link_clicks,
        )

        ad_test_create_read_test_verdict_type_0_daily_facts_item.additional_properties = d
        return ad_test_create_read_test_verdict_type_0_daily_facts_item

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
