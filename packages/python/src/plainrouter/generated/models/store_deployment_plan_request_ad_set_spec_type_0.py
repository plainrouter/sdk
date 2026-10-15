from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreDeploymentPlanRequestAdSetSpecType0")


@_attrs_define
class StoreDeploymentPlanRequestAdSetSpecType0:
    """Budget fields use positive whole Meta minor units. JSON booleans return 422 with field errors; digit-only strings
    retain their existing normalization.

        Attributes:
            daily_budget (int | Unset):
            bid_amount (int | Unset):
            lifetime_budget (int | None | Unset):
    """

    daily_budget: int | Unset = UNSET
    bid_amount: int | Unset = UNSET
    lifetime_budget: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_budget = self.daily_budget

        bid_amount = self.bid_amount

        lifetime_budget: int | None | Unset
        if isinstance(self.lifetime_budget, Unset):
            lifetime_budget = UNSET
        else:
            lifetime_budget = self.lifetime_budget

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_budget is not UNSET:
            field_dict["daily_budget"] = daily_budget
        if bid_amount is not UNSET:
            field_dict["bid_amount"] = bid_amount
        if lifetime_budget is not UNSET:
            field_dict["lifetime_budget"] = lifetime_budget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daily_budget = d.pop("daily_budget", UNSET)

        bid_amount = d.pop("bid_amount", UNSET)

        def _parse_lifetime_budget(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lifetime_budget = _parse_lifetime_budget(d.pop("lifetime_budget", UNSET))

        store_deployment_plan_request_ad_set_spec_type_0 = cls(
            daily_budget=daily_budget,
            bid_amount=bid_amount,
            lifetime_budget=lifetime_budget,
        )

        store_deployment_plan_request_ad_set_spec_type_0.additional_properties = d
        return store_deployment_plan_request_ad_set_spec_type_0

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
