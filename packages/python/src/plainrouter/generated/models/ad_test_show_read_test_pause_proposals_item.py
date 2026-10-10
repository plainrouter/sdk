from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_test_show_read_test_pause_proposals_item_reason_type_1 import (
    AdTestShowReadTestPauseProposalsItemReasonType1,
)
from ..models.ad_test_show_read_test_pause_proposals_item_reason_type_2_type_1 import (
    AdTestShowReadTestPauseProposalsItemReasonType2Type1,
)
from ..models.ad_test_show_read_test_pause_proposals_item_reason_type_3_type_1 import (
    AdTestShowReadTestPauseProposalsItemReasonType3Type1,
)
from ..models.ad_test_show_read_test_pause_proposals_item_status import AdTestShowReadTestPauseProposalsItemStatus

T = TypeVar("T", bound="AdTestShowReadTestPauseProposalsItem")


@_attrs_define
class AdTestShowReadTestPauseProposalsItem:
    """
    Attributes:
        ad_id (str):
        status (AdTestShowReadTestPauseProposalsItemStatus):
        reason (AdTestShowReadTestPauseProposalsItemReasonType1 | AdTestShowReadTestPauseProposalsItemReasonType2Type1 |
            AdTestShowReadTestPauseProposalsItemReasonType3Type1 | None): Stable reason code when the proposal was skipped
            or expired.
        decision_deadline_at (datetime.datetime): Immutable deadline 24 hours after the Test's candidates are created on
            the database clock.
    """

    ad_id: str
    status: AdTestShowReadTestPauseProposalsItemStatus
    reason: (
        AdTestShowReadTestPauseProposalsItemReasonType1
        | AdTestShowReadTestPauseProposalsItemReasonType2Type1
        | AdTestShowReadTestPauseProposalsItemReasonType3Type1
        | None
    )
    decision_deadline_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_id = self.ad_id

        status = self.status.value

        reason: None | str
        if isinstance(self.reason, AdTestShowReadTestPauseProposalsItemReasonType1):
            reason = self.reason.value
        elif isinstance(self.reason, AdTestShowReadTestPauseProposalsItemReasonType2Type1):
            reason = self.reason.value
        elif isinstance(self.reason, AdTestShowReadTestPauseProposalsItemReasonType3Type1):
            reason = self.reason.value
        else:
            reason = self.reason

        decision_deadline_at = self.decision_deadline_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ad_id": ad_id,
                "status": status,
                "reason": reason,
                "decision_deadline_at": decision_deadline_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_id = d.pop("ad_id")

        status = AdTestShowReadTestPauseProposalsItemStatus(d.pop("status"))

        def _parse_reason(
            data: object,
        ) -> (
            AdTestShowReadTestPauseProposalsItemReasonType1
            | AdTestShowReadTestPauseProposalsItemReasonType2Type1
            | AdTestShowReadTestPauseProposalsItemReasonType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = AdTestShowReadTestPauseProposalsItemReasonType1(data)

                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_2_type_1 = AdTestShowReadTestPauseProposalsItemReasonType2Type1(data)

                return reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_3_type_1 = AdTestShowReadTestPauseProposalsItemReasonType3Type1(data)

                return reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AdTestShowReadTestPauseProposalsItemReasonType1
                | AdTestShowReadTestPauseProposalsItemReasonType2Type1
                | AdTestShowReadTestPauseProposalsItemReasonType3Type1
                | None,
                data,
            )

        reason = _parse_reason(d.pop("reason"))

        decision_deadline_at = datetime.datetime.fromisoformat(d.pop("decision_deadline_at"))

        ad_test_show_read_test_pause_proposals_item = cls(
            ad_id=ad_id,
            status=status,
            reason=reason,
            decision_deadline_at=decision_deadline_at,
        )

        ad_test_show_read_test_pause_proposals_item.additional_properties = d
        return ad_test_show_read_test_pause_proposals_item

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
