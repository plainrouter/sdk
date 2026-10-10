from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_tests_api_store_body_axis import ActionsTestsApiStoreBodyAxis
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsTestsApiStoreBody")


@_attrs_define
class ActionsTestsApiStoreBody:
    """
    Attributes:
        platform_ad_account_id (int):
        ad_set_id (str):
        member_ad_ids (list[str]): Two to four distinct Meta ad IDs shown in the selected ad set inventory.
        axis (ActionsTestsApiStoreBodyAxis):
        event_name (str): An observed workspace conversion event other than PageView.
        arrivals_floor (int | Unset): Optional override; default 50 counted arrivals per member.
        minimum_conversions (int | Unset): Optional override; default 10 recorded conversions for a winner.
        maximum_days (int | Unset): Optional override; default 14 complete account-local days.
        maximum_spend_minor (int | None | str | Unset): Optional stop limit in positive whole Meta minor units, using
            the same unit scale as Launch plan budget_amount_minor.
    """

    platform_ad_account_id: int
    ad_set_id: str
    member_ad_ids: list[str]
    axis: ActionsTestsApiStoreBodyAxis
    event_name: str
    arrivals_floor: int | Unset = UNSET
    minimum_conversions: int | Unset = UNSET
    maximum_days: int | Unset = UNSET
    maximum_spend_minor: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_ad_account_id = self.platform_ad_account_id

        ad_set_id = self.ad_set_id

        member_ad_ids = self.member_ad_ids

        axis = self.axis.value

        event_name = self.event_name

        arrivals_floor = self.arrivals_floor

        minimum_conversions = self.minimum_conversions

        maximum_days = self.maximum_days

        maximum_spend_minor: int | None | str | Unset
        if isinstance(self.maximum_spend_minor, Unset):
            maximum_spend_minor = UNSET
        else:
            maximum_spend_minor = self.maximum_spend_minor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform_ad_account_id": platform_ad_account_id,
                "ad_set_id": ad_set_id,
                "member_ad_ids": member_ad_ids,
                "axis": axis,
                "event_name": event_name,
            }
        )
        if arrivals_floor is not UNSET:
            field_dict["arrivals_floor"] = arrivals_floor
        if minimum_conversions is not UNSET:
            field_dict["minimum_conversions"] = minimum_conversions
        if maximum_days is not UNSET:
            field_dict["maximum_days"] = maximum_days
        if maximum_spend_minor is not UNSET:
            field_dict["maximum_spend_minor"] = maximum_spend_minor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_ad_account_id = d.pop("platform_ad_account_id")

        ad_set_id = d.pop("ad_set_id")

        member_ad_ids = cast(list[str], d.pop("member_ad_ids"))

        axis = ActionsTestsApiStoreBodyAxis(d.pop("axis"))

        event_name = d.pop("event_name")

        arrivals_floor = d.pop("arrivals_floor", UNSET)

        minimum_conversions = d.pop("minimum_conversions", UNSET)

        maximum_days = d.pop("maximum_days", UNSET)

        def _parse_maximum_spend_minor(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        maximum_spend_minor = _parse_maximum_spend_minor(d.pop("maximum_spend_minor", UNSET))

        actions_tests_api_store_body = cls(
            platform_ad_account_id=platform_ad_account_id,
            ad_set_id=ad_set_id,
            member_ad_ids=member_ad_ids,
            axis=axis,
            event_name=event_name,
            arrivals_floor=arrivals_floor,
            minimum_conversions=minimum_conversions,
            maximum_days=maximum_days,
            maximum_spend_minor=maximum_spend_minor,
        )

        actions_tests_api_store_body.additional_properties = d
        return actions_tests_api_store_body

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
