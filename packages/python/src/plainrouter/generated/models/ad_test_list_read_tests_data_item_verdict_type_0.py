from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_test_list_read_tests_data_item_verdict_type_0_outcome_type_1 import (
    AdTestListReadTestsDataItemVerdictType0OutcomeType1,
)
from ..models.ad_test_list_read_tests_data_item_verdict_type_0_outcome_type_2_type_1 import (
    AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1,
)
from ..models.ad_test_list_read_tests_data_item_verdict_type_0_outcome_type_3_type_1 import (
    AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_test_list_read_tests_data_item_verdict_type_0_daily_facts_item import (
        AdTestListReadTestsDataItemVerdictType0DailyFactsItem,
    )
    from ..models.ad_test_list_read_tests_data_item_verdict_type_0_halt_details_type_0 import (
        AdTestListReadTestsDataItemVerdictType0HaltDetailsType0,
    )
    from ..models.ad_test_list_read_tests_data_item_verdict_type_0_members_item import (
        AdTestListReadTestsDataItemVerdictType0MembersItem,
    )


T = TypeVar("T", bound="AdTestListReadTestsDataItemVerdictType0")


@_attrs_define
class AdTestListReadTestsDataItemVerdictType0:
    """
    Attributes:
        outcome (AdTestListReadTestsDataItemVerdictType0OutcomeType1 |
            AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1 |
            AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1 | None):
        winner_ad_id (None | str):
        reason (None | str):
        window_start (datetime.date | None):
        window_end (datetime.date | None):
        concluded_at (datetime.datetime | None):
        members (list[AdTestListReadTestsDataItemVerdictType0MembersItem]):
        daily_facts (list[AdTestListReadTestsDataItemVerdictType0DailyFactsItem]):
        halt_details (AdTestListReadTestsDataItemVerdictType0HaltDetailsType0 | None | Unset):
    """

    outcome: (
        AdTestListReadTestsDataItemVerdictType0OutcomeType1
        | AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1
        | AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1
        | None
    )
    winner_ad_id: None | str
    reason: None | str
    window_start: datetime.date | None
    window_end: datetime.date | None
    concluded_at: datetime.datetime | None
    members: list[AdTestListReadTestsDataItemVerdictType0MembersItem]
    daily_facts: list[AdTestListReadTestsDataItemVerdictType0DailyFactsItem]
    halt_details: AdTestListReadTestsDataItemVerdictType0HaltDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ad_test_list_read_tests_data_item_verdict_type_0_halt_details_type_0 import (
            AdTestListReadTestsDataItemVerdictType0HaltDetailsType0,
        )

        outcome: None | str
        if isinstance(self.outcome, AdTestListReadTestsDataItemVerdictType0OutcomeType1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1):
            outcome = self.outcome.value
        else:
            outcome = self.outcome

        winner_ad_id: None | str
        winner_ad_id = self.winner_ad_id

        reason: None | str
        reason = self.reason

        window_start: None | str
        if isinstance(self.window_start, datetime.date):
            window_start = self.window_start.isoformat()
        else:
            window_start = self.window_start

        window_end: None | str
        if isinstance(self.window_end, datetime.date):
            window_end = self.window_end.isoformat()
        else:
            window_end = self.window_end

        concluded_at: None | str
        if isinstance(self.concluded_at, datetime.datetime):
            concluded_at = self.concluded_at.isoformat()
        else:
            concluded_at = self.concluded_at

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        daily_facts = []
        for daily_facts_item_data in self.daily_facts:
            daily_facts_item = daily_facts_item_data.to_dict()
            daily_facts.append(daily_facts_item)

        halt_details: dict[str, Any] | None | Unset
        if isinstance(self.halt_details, Unset):
            halt_details = UNSET
        elif isinstance(self.halt_details, AdTestListReadTestsDataItemVerdictType0HaltDetailsType0):
            halt_details = self.halt_details.to_dict()
        else:
            halt_details = self.halt_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "winner_ad_id": winner_ad_id,
                "reason": reason,
                "window_start": window_start,
                "window_end": window_end,
                "concluded_at": concluded_at,
                "members": members,
                "daily_facts": daily_facts,
            }
        )
        if halt_details is not UNSET:
            field_dict["halt_details"] = halt_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_test_list_read_tests_data_item_verdict_type_0_daily_facts_item import (
            AdTestListReadTestsDataItemVerdictType0DailyFactsItem,
        )
        from ..models.ad_test_list_read_tests_data_item_verdict_type_0_halt_details_type_0 import (
            AdTestListReadTestsDataItemVerdictType0HaltDetailsType0,
        )
        from ..models.ad_test_list_read_tests_data_item_verdict_type_0_members_item import (
            AdTestListReadTestsDataItemVerdictType0MembersItem,
        )

        d = dict(src_dict)

        def _parse_outcome(
            data: object,
        ) -> (
            AdTestListReadTestsDataItemVerdictType0OutcomeType1
            | AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1
            | AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_1 = AdTestListReadTestsDataItemVerdictType0OutcomeType1(data)

                return outcome_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_2_type_1 = AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1(data)

                return outcome_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_3_type_1 = AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1(data)

                return outcome_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AdTestListReadTestsDataItemVerdictType0OutcomeType1
                | AdTestListReadTestsDataItemVerdictType0OutcomeType2Type1
                | AdTestListReadTestsDataItemVerdictType0OutcomeType3Type1
                | None,
                data,
            )

        outcome = _parse_outcome(d.pop("outcome"))

        def _parse_winner_ad_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        winner_ad_id = _parse_winner_ad_id(d.pop("winner_ad_id"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_window_start(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_start_type_0 = datetime.date.fromisoformat(data)

                return window_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        window_start = _parse_window_start(d.pop("window_start"))

        def _parse_window_end(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_end_type_0 = datetime.date.fromisoformat(data)

                return window_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        window_end = _parse_window_end(d.pop("window_end"))

        def _parse_concluded_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                concluded_at_type_0 = datetime.datetime.fromisoformat(data)

                return concluded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        concluded_at = _parse_concluded_at(d.pop("concluded_at"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = AdTestListReadTestsDataItemVerdictType0MembersItem.from_dict(members_item_data)

            members.append(members_item)

        daily_facts = []
        _daily_facts = d.pop("daily_facts")
        for daily_facts_item_data in _daily_facts:
            daily_facts_item = AdTestListReadTestsDataItemVerdictType0DailyFactsItem.from_dict(daily_facts_item_data)

            daily_facts.append(daily_facts_item)

        def _parse_halt_details(data: object) -> AdTestListReadTestsDataItemVerdictType0HaltDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                halt_details_type_0 = AdTestListReadTestsDataItemVerdictType0HaltDetailsType0.from_dict(data)

                return halt_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdTestListReadTestsDataItemVerdictType0HaltDetailsType0 | None | Unset, data)

        halt_details = _parse_halt_details(d.pop("halt_details", UNSET))

        ad_test_list_read_tests_data_item_verdict_type_0 = cls(
            outcome=outcome,
            winner_ad_id=winner_ad_id,
            reason=reason,
            window_start=window_start,
            window_end=window_end,
            concluded_at=concluded_at,
            members=members,
            daily_facts=daily_facts,
            halt_details=halt_details,
        )

        ad_test_list_read_tests_data_item_verdict_type_0.additional_properties = d
        return ad_test_list_read_tests_data_item_verdict_type_0

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
