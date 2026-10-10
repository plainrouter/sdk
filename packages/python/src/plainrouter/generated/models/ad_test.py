from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdTest")


@_attrs_define
class AdTest:
    """
    Attributes:
        id (str):
        workspace_id (int):
        platform_ad_account_id (int):
        ad_set_id (str):
        axis (str):
        event_name (str):
        arrivals_floor (int):
        minimum_conversions (int):
        maximum_days (int):
        maximum_spend_minor (None | str):
        anomaly_threshold_percent (str):
        currency (str):
        timezone (str):
        first_day (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        count_health_click_threshold (int | None):
    """

    id: str
    workspace_id: int
    platform_ad_account_id: int
    ad_set_id: str
    axis: str
    event_name: str
    arrivals_floor: int
    minimum_conversions: int
    maximum_days: int
    maximum_spend_minor: None | str
    anomaly_threshold_percent: str
    currency: str
    timezone: str
    first_day: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    count_health_click_threshold: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        platform_ad_account_id = self.platform_ad_account_id

        ad_set_id = self.ad_set_id

        axis = self.axis

        event_name = self.event_name

        arrivals_floor = self.arrivals_floor

        minimum_conversions = self.minimum_conversions

        maximum_days = self.maximum_days

        maximum_spend_minor: None | str
        maximum_spend_minor = self.maximum_spend_minor

        anomaly_threshold_percent = self.anomaly_threshold_percent

        currency = self.currency

        timezone = self.timezone

        first_day = self.first_day.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        count_health_click_threshold: int | None
        count_health_click_threshold = self.count_health_click_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "platform_ad_account_id": platform_ad_account_id,
                "ad_set_id": ad_set_id,
                "axis": axis,
                "event_name": event_name,
                "arrivals_floor": arrivals_floor,
                "minimum_conversions": minimum_conversions,
                "maximum_days": maximum_days,
                "maximum_spend_minor": maximum_spend_minor,
                "anomaly_threshold_percent": anomaly_threshold_percent,
                "currency": currency,
                "timezone": timezone,
                "first_day": first_day,
                "created_at": created_at,
                "updated_at": updated_at,
                "count_health_click_threshold": count_health_click_threshold,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        ad_set_id = d.pop("ad_set_id")

        axis = d.pop("axis")

        event_name = d.pop("event_name")

        arrivals_floor = d.pop("arrivals_floor")

        minimum_conversions = d.pop("minimum_conversions")

        maximum_days = d.pop("maximum_days")

        def _parse_maximum_spend_minor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        maximum_spend_minor = _parse_maximum_spend_minor(d.pop("maximum_spend_minor"))

        anomaly_threshold_percent = d.pop("anomaly_threshold_percent")

        currency = d.pop("currency")

        timezone = d.pop("timezone")

        first_day = datetime.datetime.fromisoformat(d.pop("first_day"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_count_health_click_threshold(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        count_health_click_threshold = _parse_count_health_click_threshold(d.pop("count_health_click_threshold"))

        ad_test = cls(
            id=id,
            workspace_id=workspace_id,
            platform_ad_account_id=platform_ad_account_id,
            ad_set_id=ad_set_id,
            axis=axis,
            event_name=event_name,
            arrivals_floor=arrivals_floor,
            minimum_conversions=minimum_conversions,
            maximum_days=maximum_days,
            maximum_spend_minor=maximum_spend_minor,
            anomaly_threshold_percent=anomaly_threshold_percent,
            currency=currency,
            timezone=timezone,
            first_day=first_day,
            created_at=created_at,
            updated_at=updated_at,
            count_health_click_threshold=count_health_click_threshold,
        )

        ad_test.additional_properties = d
        return ad_test

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
