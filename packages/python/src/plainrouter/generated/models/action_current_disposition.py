from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_current_disposition_outcome_status_type_1 import ActionCurrentDispositionOutcomeStatusType1
from ..models.action_current_disposition_outcome_status_type_2_type_1 import (
    ActionCurrentDispositionOutcomeStatusType2Type1,
)
from ..models.action_current_disposition_outcome_status_type_3_type_1 import (
    ActionCurrentDispositionOutcomeStatusType3Type1,
)
from ..models.action_current_disposition_receipt_status_type_1 import ActionCurrentDispositionReceiptStatusType1
from ..models.action_current_disposition_receipt_status_type_2_type_1 import (
    ActionCurrentDispositionReceiptStatusType2Type1,
)
from ..models.action_current_disposition_receipt_status_type_3_type_1 import (
    ActionCurrentDispositionReceiptStatusType3Type1,
)
from ..models.action_current_disposition_recovery_disposition_type_1 import (
    ActionCurrentDispositionRecoveryDispositionType1,
)
from ..models.action_current_disposition_recovery_disposition_type_2_type_1 import (
    ActionCurrentDispositionRecoveryDispositionType2Type1,
)
from ..models.action_current_disposition_recovery_disposition_type_3_type_1 import (
    ActionCurrentDispositionRecoveryDispositionType3Type1,
)

if TYPE_CHECKING:
    from ..models.action_current_disposition_outcome_payload_type_0 import ActionCurrentDispositionOutcomePayloadType0


T = TypeVar("T", bound="ActionCurrentDisposition")


@_attrs_define
class ActionCurrentDisposition:
    """
    Attributes:
        receipt_status (ActionCurrentDispositionReceiptStatusType1 | ActionCurrentDispositionReceiptStatusType2Type1 |
            ActionCurrentDispositionReceiptStatusType3Type1 | None):
        outcome_payload (ActionCurrentDispositionOutcomePayloadType0 | None): Write-once outcome. Management comparisons
            use PlainRouter counted arrivals and Inventory spend. Resume compares the target after the change with the rest
            of the same account over those same days. Pause is not judged. Missing data never yields a verdict. Other action
            types retain their existing payloads.
        outcome_status (ActionCurrentDispositionOutcomeStatusType1 | ActionCurrentDispositionOutcomeStatusType2Type1 |
            ActionCurrentDispositionOutcomeStatusType3Type1 | None):
        outcome_reason_code (None | str):
        outcome_checked_at (datetime.datetime | None):
        compensation_reason_code (None | str):
        recovery_disposition (ActionCurrentDispositionRecoveryDispositionType1 |
            ActionCurrentDispositionRecoveryDispositionType2Type1 | ActionCurrentDispositionRecoveryDispositionType3Type1 |
            None):
        late_restored (bool):
    """

    receipt_status: (
        ActionCurrentDispositionReceiptStatusType1
        | ActionCurrentDispositionReceiptStatusType2Type1
        | ActionCurrentDispositionReceiptStatusType3Type1
        | None
    )
    outcome_payload: ActionCurrentDispositionOutcomePayloadType0 | None
    outcome_status: (
        ActionCurrentDispositionOutcomeStatusType1
        | ActionCurrentDispositionOutcomeStatusType2Type1
        | ActionCurrentDispositionOutcomeStatusType3Type1
        | None
    )
    outcome_reason_code: None | str
    outcome_checked_at: datetime.datetime | None
    compensation_reason_code: None | str
    recovery_disposition: (
        ActionCurrentDispositionRecoveryDispositionType1
        | ActionCurrentDispositionRecoveryDispositionType2Type1
        | ActionCurrentDispositionRecoveryDispositionType3Type1
        | None
    )
    late_restored: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_current_disposition_outcome_payload_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0,
        )

        receipt_status: None | str
        if isinstance(self.receipt_status, ActionCurrentDispositionReceiptStatusType1):
            receipt_status = self.receipt_status.value
        elif isinstance(self.receipt_status, ActionCurrentDispositionReceiptStatusType2Type1):
            receipt_status = self.receipt_status.value
        elif isinstance(self.receipt_status, ActionCurrentDispositionReceiptStatusType3Type1):
            receipt_status = self.receipt_status.value
        else:
            receipt_status = self.receipt_status

        outcome_payload: dict[str, Any] | None
        if isinstance(self.outcome_payload, ActionCurrentDispositionOutcomePayloadType0):
            outcome_payload = self.outcome_payload.to_dict()
        else:
            outcome_payload = self.outcome_payload

        outcome_status: None | str
        if isinstance(self.outcome_status, ActionCurrentDispositionOutcomeStatusType1):
            outcome_status = self.outcome_status.value
        elif isinstance(self.outcome_status, ActionCurrentDispositionOutcomeStatusType2Type1):
            outcome_status = self.outcome_status.value
        elif isinstance(self.outcome_status, ActionCurrentDispositionOutcomeStatusType3Type1):
            outcome_status = self.outcome_status.value
        else:
            outcome_status = self.outcome_status

        outcome_reason_code: None | str
        outcome_reason_code = self.outcome_reason_code

        outcome_checked_at: None | str
        if isinstance(self.outcome_checked_at, datetime.datetime):
            outcome_checked_at = self.outcome_checked_at.isoformat()
        else:
            outcome_checked_at = self.outcome_checked_at

        compensation_reason_code: None | str
        compensation_reason_code = self.compensation_reason_code

        recovery_disposition: None | str
        if isinstance(self.recovery_disposition, ActionCurrentDispositionRecoveryDispositionType1):
            recovery_disposition = self.recovery_disposition.value
        elif isinstance(self.recovery_disposition, ActionCurrentDispositionRecoveryDispositionType2Type1):
            recovery_disposition = self.recovery_disposition.value
        elif isinstance(self.recovery_disposition, ActionCurrentDispositionRecoveryDispositionType3Type1):
            recovery_disposition = self.recovery_disposition.value
        else:
            recovery_disposition = self.recovery_disposition

        late_restored = self.late_restored

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "receipt_status": receipt_status,
                "outcome_payload": outcome_payload,
                "outcome_status": outcome_status,
                "outcome_reason_code": outcome_reason_code,
                "outcome_checked_at": outcome_checked_at,
                "compensation_reason_code": compensation_reason_code,
                "recovery_disposition": recovery_disposition,
                "late_restored": late_restored,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_current_disposition_outcome_payload_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0,
        )

        d = dict(src_dict)

        def _parse_receipt_status(
            data: object,
        ) -> (
            ActionCurrentDispositionReceiptStatusType1
            | ActionCurrentDispositionReceiptStatusType2Type1
            | ActionCurrentDispositionReceiptStatusType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receipt_status_type_1 = ActionCurrentDispositionReceiptStatusType1(data)

                return receipt_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receipt_status_type_2_type_1 = ActionCurrentDispositionReceiptStatusType2Type1(data)

                return receipt_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receipt_status_type_3_type_1 = ActionCurrentDispositionReceiptStatusType3Type1(data)

                return receipt_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ActionCurrentDispositionReceiptStatusType1
                | ActionCurrentDispositionReceiptStatusType2Type1
                | ActionCurrentDispositionReceiptStatusType3Type1
                | None,
                data,
            )

        receipt_status = _parse_receipt_status(d.pop("receipt_status"))

        def _parse_outcome_payload(data: object) -> ActionCurrentDispositionOutcomePayloadType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outcome_payload_type_0 = ActionCurrentDispositionOutcomePayloadType0.from_dict(data)

                return outcome_payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionCurrentDispositionOutcomePayloadType0 | None, data)

        outcome_payload = _parse_outcome_payload(d.pop("outcome_payload"))

        def _parse_outcome_status(
            data: object,
        ) -> (
            ActionCurrentDispositionOutcomeStatusType1
            | ActionCurrentDispositionOutcomeStatusType2Type1
            | ActionCurrentDispositionOutcomeStatusType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_status_type_1 = ActionCurrentDispositionOutcomeStatusType1(data)

                return outcome_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_status_type_2_type_1 = ActionCurrentDispositionOutcomeStatusType2Type1(data)

                return outcome_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_status_type_3_type_1 = ActionCurrentDispositionOutcomeStatusType3Type1(data)

                return outcome_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ActionCurrentDispositionOutcomeStatusType1
                | ActionCurrentDispositionOutcomeStatusType2Type1
                | ActionCurrentDispositionOutcomeStatusType3Type1
                | None,
                data,
            )

        outcome_status = _parse_outcome_status(d.pop("outcome_status"))

        def _parse_outcome_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_reason_code = _parse_outcome_reason_code(d.pop("outcome_reason_code"))

        def _parse_outcome_checked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return outcome_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        outcome_checked_at = _parse_outcome_checked_at(d.pop("outcome_checked_at"))

        def _parse_compensation_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        compensation_reason_code = _parse_compensation_reason_code(d.pop("compensation_reason_code"))

        def _parse_recovery_disposition(
            data: object,
        ) -> (
            ActionCurrentDispositionRecoveryDispositionType1
            | ActionCurrentDispositionRecoveryDispositionType2Type1
            | ActionCurrentDispositionRecoveryDispositionType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recovery_disposition_type_1 = ActionCurrentDispositionRecoveryDispositionType1(data)

                return recovery_disposition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recovery_disposition_type_2_type_1 = ActionCurrentDispositionRecoveryDispositionType2Type1(data)

                return recovery_disposition_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recovery_disposition_type_3_type_1 = ActionCurrentDispositionRecoveryDispositionType3Type1(data)

                return recovery_disposition_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ActionCurrentDispositionRecoveryDispositionType1
                | ActionCurrentDispositionRecoveryDispositionType2Type1
                | ActionCurrentDispositionRecoveryDispositionType3Type1
                | None,
                data,
            )

        recovery_disposition = _parse_recovery_disposition(d.pop("recovery_disposition"))

        late_restored = d.pop("late_restored")

        action_current_disposition = cls(
            receipt_status=receipt_status,
            outcome_payload=outcome_payload,
            outcome_status=outcome_status,
            outcome_reason_code=outcome_reason_code,
            outcome_checked_at=outcome_checked_at,
            compensation_reason_code=compensation_reason_code,
            recovery_disposition=recovery_disposition,
            late_restored=late_restored,
        )

        action_current_disposition.additional_properties = d
        return action_current_disposition

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
