from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_test_show_read_test_axis import AdTestShowReadTestAxis
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_test_show_read_test_members_item import AdTestShowReadTestMembersItem
    from ..models.ad_test_show_read_test_pause_proposals_item import AdTestShowReadTestPauseProposalsItem
    from ..models.ad_test_show_read_test_verdict_type_0 import AdTestShowReadTestVerdictType0


T = TypeVar("T", bound="AdTestShowReadTest")


@_attrs_define
class AdTestShowReadTest:
    """
    Attributes:
        id (str):
        workspace_id (int):
        platform_ad_account_id (int):
        ad_set_id (str):
        axis (AdTestShowReadTestAxis):
        event_name (str):
        arrivals_floor (int):
        minimum_conversions (int):
        maximum_days (int):
        maximum_spend_minor (None | str): Optional maximum in positive whole Meta minor units, using the same unit scale
            as Launch plan budget_amount_minor.
        anomaly_threshold_percent (str):
        first_day (datetime.date):
        timezone (str):
        currency (str):
        created_at (datetime.datetime | None):
        members (list[AdTestShowReadTestMembersItem]):
        pause_proposals (list[AdTestShowReadTestPauseProposalsItem]):
        verdict (AdTestShowReadTestVerdictType0 | None):
        count_health_click_threshold (int | None | Unset): Link-click threshold frozen at conclusion; null until
            concluded or for legacy Tests.
    """

    id: str
    workspace_id: int
    platform_ad_account_id: int
    ad_set_id: str
    axis: AdTestShowReadTestAxis
    event_name: str
    arrivals_floor: int
    minimum_conversions: int
    maximum_days: int
    maximum_spend_minor: None | str
    anomaly_threshold_percent: str
    first_day: datetime.date
    timezone: str
    currency: str
    created_at: datetime.datetime | None
    members: list[AdTestShowReadTestMembersItem]
    pause_proposals: list[AdTestShowReadTestPauseProposalsItem]
    verdict: AdTestShowReadTestVerdictType0 | None
    count_health_click_threshold: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ad_test_show_read_test_verdict_type_0 import AdTestShowReadTestVerdictType0

        id = self.id

        workspace_id = self.workspace_id

        platform_ad_account_id = self.platform_ad_account_id

        ad_set_id = self.ad_set_id

        axis = self.axis.value

        event_name = self.event_name

        arrivals_floor = self.arrivals_floor

        minimum_conversions = self.minimum_conversions

        maximum_days = self.maximum_days

        maximum_spend_minor: None | str
        maximum_spend_minor = self.maximum_spend_minor

        anomaly_threshold_percent = self.anomaly_threshold_percent

        first_day = self.first_day.isoformat()

        timezone = self.timezone

        currency = self.currency

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        pause_proposals = []
        for pause_proposals_item_data in self.pause_proposals:
            pause_proposals_item = pause_proposals_item_data.to_dict()
            pause_proposals.append(pause_proposals_item)

        verdict: dict[str, Any] | None
        if isinstance(self.verdict, AdTestShowReadTestVerdictType0):
            verdict = self.verdict.to_dict()
        else:
            verdict = self.verdict

        count_health_click_threshold: int | None | Unset
        if isinstance(self.count_health_click_threshold, Unset):
            count_health_click_threshold = UNSET
        else:
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
                "first_day": first_day,
                "timezone": timezone,
                "currency": currency,
                "created_at": created_at,
                "members": members,
                "pause_proposals": pause_proposals,
                "verdict": verdict,
            }
        )
        if count_health_click_threshold is not UNSET:
            field_dict["count_health_click_threshold"] = count_health_click_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_test_show_read_test_members_item import AdTestShowReadTestMembersItem
        from ..models.ad_test_show_read_test_pause_proposals_item import AdTestShowReadTestPauseProposalsItem
        from ..models.ad_test_show_read_test_verdict_type_0 import AdTestShowReadTestVerdictType0

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        ad_set_id = d.pop("ad_set_id")

        axis = AdTestShowReadTestAxis(d.pop("axis"))

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

        first_day = datetime.date.fromisoformat(d.pop("first_day"))

        timezone = d.pop("timezone")

        currency = d.pop("currency")

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = AdTestShowReadTestMembersItem.from_dict(members_item_data)

            members.append(members_item)

        pause_proposals = []
        _pause_proposals = d.pop("pause_proposals")
        for pause_proposals_item_data in _pause_proposals:
            pause_proposals_item = AdTestShowReadTestPauseProposalsItem.from_dict(pause_proposals_item_data)

            pause_proposals.append(pause_proposals_item)

        def _parse_verdict(data: object) -> AdTestShowReadTestVerdictType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verdict_type_0 = AdTestShowReadTestVerdictType0.from_dict(data)

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdTestShowReadTestVerdictType0 | None, data)

        verdict = _parse_verdict(d.pop("verdict"))

        def _parse_count_health_click_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count_health_click_threshold = _parse_count_health_click_threshold(d.pop("count_health_click_threshold", UNSET))

        ad_test_show_read_test = cls(
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
            first_day=first_day,
            timezone=timezone,
            currency=currency,
            created_at=created_at,
            members=members,
            pause_proposals=pause_proposals,
            verdict=verdict,
            count_health_click_threshold=count_health_click_threshold,
        )

        ad_test_show_read_test.additional_properties = d
        return ad_test_show_read_test

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
