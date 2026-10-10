from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_test_show_read_test_verdict_type_0_halt_details_type_0_effective_status import (
    AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_test_show_read_test_verdict_type_0_halt_details_type_0_baseline import (
        AdTestShowReadTestVerdictType0HaltDetailsType0Baseline,
    )
    from ..models.ad_test_show_read_test_verdict_type_0_halt_details_type_0_observed_destinations_item import (
        AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem,
    )


T = TypeVar("T", bound="AdTestShowReadTestVerdictType0HaltDetailsType0")


@_attrs_define
class AdTestShowReadTestVerdictType0HaltDetailsType0:
    """
    Attributes:
        ad_id (str | Unset):
        effective_status (AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus | Unset):
        date (datetime.date | Unset):
        link_clicks (int | Unset):
        counted_arrivals (int | Unset):
        ad_test_member_id (str | Unset):
        baseline (AdTestShowReadTestVerdictType0HaltDetailsType0Baseline | Unset):
        observed_destinations (list[AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem] | Unset):
    """

    ad_id: str | Unset = UNSET
    effective_status: AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus | Unset = UNSET
    date: datetime.date | Unset = UNSET
    link_clicks: int | Unset = UNSET
    counted_arrivals: int | Unset = UNSET
    ad_test_member_id: str | Unset = UNSET
    baseline: AdTestShowReadTestVerdictType0HaltDetailsType0Baseline | Unset = UNSET
    observed_destinations: list[AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_id = self.ad_id

        effective_status: str | Unset = UNSET
        if not isinstance(self.effective_status, Unset):
            effective_status = self.effective_status.value

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        link_clicks = self.link_clicks

        counted_arrivals = self.counted_arrivals

        ad_test_member_id = self.ad_test_member_id

        baseline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline, Unset):
            baseline = self.baseline.to_dict()

        observed_destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.observed_destinations, Unset):
            observed_destinations = []
            for observed_destinations_item_data in self.observed_destinations:
                observed_destinations_item = observed_destinations_item_data.to_dict()
                observed_destinations.append(observed_destinations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_id is not UNSET:
            field_dict["ad_id"] = ad_id
        if effective_status is not UNSET:
            field_dict["effective_status"] = effective_status
        if date is not UNSET:
            field_dict["date"] = date
        if link_clicks is not UNSET:
            field_dict["link_clicks"] = link_clicks
        if counted_arrivals is not UNSET:
            field_dict["counted_arrivals"] = counted_arrivals
        if ad_test_member_id is not UNSET:
            field_dict["ad_test_member_id"] = ad_test_member_id
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if observed_destinations is not UNSET:
            field_dict["observed_destinations"] = observed_destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_test_show_read_test_verdict_type_0_halt_details_type_0_baseline import (
            AdTestShowReadTestVerdictType0HaltDetailsType0Baseline,
        )
        from ..models.ad_test_show_read_test_verdict_type_0_halt_details_type_0_observed_destinations_item import (
            AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem,
        )

        d = dict(src_dict)
        ad_id = d.pop("ad_id", UNSET)

        _effective_status = d.pop("effective_status", UNSET)
        effective_status: AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus | Unset
        if isinstance(_effective_status, Unset):
            effective_status = UNSET
        else:
            effective_status = AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus(_effective_status)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        link_clicks = d.pop("link_clicks", UNSET)

        counted_arrivals = d.pop("counted_arrivals", UNSET)

        ad_test_member_id = d.pop("ad_test_member_id", UNSET)

        _baseline = d.pop("baseline", UNSET)
        baseline: AdTestShowReadTestVerdictType0HaltDetailsType0Baseline | Unset
        if isinstance(_baseline, Unset):
            baseline = UNSET
        else:
            baseline = AdTestShowReadTestVerdictType0HaltDetailsType0Baseline.from_dict(_baseline)

        _observed_destinations = d.pop("observed_destinations", UNSET)
        observed_destinations: list[AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem] | Unset = (
            UNSET
        )
        if _observed_destinations is not UNSET:
            observed_destinations = []
            for observed_destinations_item_data in _observed_destinations:
                observed_destinations_item = (
                    AdTestShowReadTestVerdictType0HaltDetailsType0ObservedDestinationsItem.from_dict(
                        observed_destinations_item_data
                    )
                )

                observed_destinations.append(observed_destinations_item)

        ad_test_show_read_test_verdict_type_0_halt_details_type_0 = cls(
            ad_id=ad_id,
            effective_status=effective_status,
            date=date,
            link_clicks=link_clicks,
            counted_arrivals=counted_arrivals,
            ad_test_member_id=ad_test_member_id,
            baseline=baseline,
            observed_destinations=observed_destinations,
        )

        ad_test_show_read_test_verdict_type_0_halt_details_type_0.additional_properties = d
        return ad_test_show_read_test_verdict_type_0_halt_details_type_0

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
