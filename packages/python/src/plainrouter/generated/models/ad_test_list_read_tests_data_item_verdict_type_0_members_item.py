from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_test_list_read_tests_data_item_verdict_type_0_members_item_state import (
    AdTestListReadTestsDataItemVerdictType0MembersItemState,
)

T = TypeVar("T", bound="AdTestListReadTestsDataItemVerdictType0MembersItem")


@_attrs_define
class AdTestListReadTestsDataItemVerdictType0MembersItem:
    """
    Attributes:
        ad_id (str):
        state (AdTestListReadTestsDataItemVerdictType0MembersItemState):
        rank (int | None):
        spend (None | str):
        impressions (int | None):
        counted_arrivals (int | None):
        recorded_conversions (int | None): PlainRouter recorded consented conversions of this Test event.
        admitted_conversions (int | None): Admitted conversions are shown beside recorded conversions and are never
            substituted for them.
        spend_per_recorded_conversion (None | str): Major-unit spend divided by PlainRouter recorded conversions; used
            only to compare members within this Test.
        covered_days (list[datetime.date]):
    """

    ad_id: str
    state: AdTestListReadTestsDataItemVerdictType0MembersItemState
    rank: int | None
    spend: None | str
    impressions: int | None
    counted_arrivals: int | None
    recorded_conversions: int | None
    admitted_conversions: int | None
    spend_per_recorded_conversion: None | str
    covered_days: list[datetime.date]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_id = self.ad_id

        state = self.state.value

        rank: int | None
        rank = self.rank

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

        spend_per_recorded_conversion: None | str
        spend_per_recorded_conversion = self.spend_per_recorded_conversion

        covered_days = []
        for covered_days_item_data in self.covered_days:
            covered_days_item = covered_days_item_data.isoformat()
            covered_days.append(covered_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ad_id": ad_id,
                "state": state,
                "rank": rank,
                "spend": spend,
                "impressions": impressions,
                "counted_arrivals": counted_arrivals,
                "recorded_conversions": recorded_conversions,
                "admitted_conversions": admitted_conversions,
                "spend_per_recorded_conversion": spend_per_recorded_conversion,
                "covered_days": covered_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_id = d.pop("ad_id")

        state = AdTestListReadTestsDataItemVerdictType0MembersItemState(d.pop("state"))

        def _parse_rank(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank = _parse_rank(d.pop("rank"))

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

        def _parse_spend_per_recorded_conversion(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        spend_per_recorded_conversion = _parse_spend_per_recorded_conversion(d.pop("spend_per_recorded_conversion"))

        covered_days = []
        _covered_days = d.pop("covered_days")
        for covered_days_item_data in _covered_days:
            covered_days_item = datetime.date.fromisoformat(covered_days_item_data)

            covered_days.append(covered_days_item)

        ad_test_list_read_tests_data_item_verdict_type_0_members_item = cls(
            ad_id=ad_id,
            state=state,
            rank=rank,
            spend=spend,
            impressions=impressions,
            counted_arrivals=counted_arrivals,
            recorded_conversions=recorded_conversions,
            admitted_conversions=admitted_conversions,
            spend_per_recorded_conversion=spend_per_recorded_conversion,
            covered_days=covered_days,
        )

        ad_test_list_read_tests_data_item_verdict_type_0_members_item.additional_properties = d
        return ad_test_list_read_tests_data_item_verdict_type_0_members_item

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
