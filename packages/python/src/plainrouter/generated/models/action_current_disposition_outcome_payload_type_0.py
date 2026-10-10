from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_current_disposition_outcome_payload_type_0_status import (
    ActionCurrentDispositionOutcomePayloadType0Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_current_disposition_outcome_payload_type_0_baseline_type_0 import (
        ActionCurrentDispositionOutcomePayloadType0BaselineType0,
    )
    from ..models.action_current_disposition_outcome_payload_type_0_inverse import (
        ActionCurrentDispositionOutcomePayloadType0Inverse,
    )
    from ..models.action_current_disposition_outcome_payload_type_0_metrics_type_0 import (
        ActionCurrentDispositionOutcomePayloadType0MetricsType0,
    )


T = TypeVar("T", bound="ActionCurrentDispositionOutcomePayloadType0")


@_attrs_define
class ActionCurrentDispositionOutcomePayloadType0:
    """Write-once outcome. Management comparisons use PlainRouter counted arrivals and Inventory spend. Resume compares the
    target after the change with the rest of the same account over those same days. Pause is not judged. Missing data
    never yields a verdict. Other action types retain their existing payloads.

        Attributes:
            status (ActionCurrentDispositionOutcomePayloadType0Status | Unset):
            observed_at (datetime.datetime | Unset):
            reason_code (None | str | Unset):
            reason (None | str | Unset):
            baseline (ActionCurrentDispositionOutcomePayloadType0BaselineType0 | list[str] | Unset):
            metrics (ActionCurrentDispositionOutcomePayloadType0MetricsType0 | list[str] | Unset):
            inverse (ActionCurrentDispositionOutcomePayloadType0Inverse | Unset):
    """

    status: ActionCurrentDispositionOutcomePayloadType0Status | Unset = UNSET
    observed_at: datetime.datetime | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    baseline: ActionCurrentDispositionOutcomePayloadType0BaselineType0 | list[str] | Unset = UNSET
    metrics: ActionCurrentDispositionOutcomePayloadType0MetricsType0 | list[str] | Unset = UNSET
    inverse: ActionCurrentDispositionOutcomePayloadType0Inverse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_current_disposition_outcome_payload_type_0_baseline_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0BaselineType0,
        )
        from ..models.action_current_disposition_outcome_payload_type_0_metrics_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0MetricsType0,
        )

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        observed_at: str | Unset = UNSET
        if not isinstance(self.observed_at, Unset):
            observed_at = self.observed_at.isoformat()

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        baseline: dict[str, Any] | list[str] | Unset
        if isinstance(self.baseline, Unset):
            baseline = UNSET
        elif isinstance(self.baseline, ActionCurrentDispositionOutcomePayloadType0BaselineType0):
            baseline = self.baseline.to_dict()
        else:
            baseline = self.baseline

        metrics: dict[str, Any] | list[str] | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, ActionCurrentDispositionOutcomePayloadType0MetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        inverse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inverse, Unset):
            inverse = self.inverse.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_current_disposition_outcome_payload_type_0_baseline_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0BaselineType0,
        )
        from ..models.action_current_disposition_outcome_payload_type_0_inverse import (
            ActionCurrentDispositionOutcomePayloadType0Inverse,
        )
        from ..models.action_current_disposition_outcome_payload_type_0_metrics_type_0 import (
            ActionCurrentDispositionOutcomePayloadType0MetricsType0,
        )

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ActionCurrentDispositionOutcomePayloadType0Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ActionCurrentDispositionOutcomePayloadType0Status(_status)

        _observed_at = d.pop("observed_at", UNSET)
        observed_at: datetime.datetime | Unset
        if isinstance(_observed_at, Unset):
            observed_at = UNSET
        else:
            observed_at = datetime.datetime.fromisoformat(_observed_at)

        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reason_code", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_baseline(
            data: object,
        ) -> ActionCurrentDispositionOutcomePayloadType0BaselineType0 | list[str] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                baseline_type_0 = ActionCurrentDispositionOutcomePayloadType0BaselineType0.from_dict(data)

                return baseline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            baseline_type_1 = cast(list[str], data)

            return baseline_type_1

        baseline = _parse_baseline(d.pop("baseline", UNSET))

        def _parse_metrics(data: object) -> ActionCurrentDispositionOutcomePayloadType0MetricsType0 | list[str] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = ActionCurrentDispositionOutcomePayloadType0MetricsType0.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            metrics_type_1 = cast(list[str], data)

            return metrics_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        _inverse = d.pop("inverse", UNSET)
        inverse: ActionCurrentDispositionOutcomePayloadType0Inverse | Unset
        if isinstance(_inverse, Unset):
            inverse = UNSET
        else:
            inverse = ActionCurrentDispositionOutcomePayloadType0Inverse.from_dict(_inverse)

        action_current_disposition_outcome_payload_type_0 = cls(
            status=status,
            observed_at=observed_at,
            reason_code=reason_code,
            reason=reason,
            baseline=baseline,
            metrics=metrics,
            inverse=inverse,
        )

        action_current_disposition_outcome_payload_type_0.additional_properties = d
        return action_current_disposition_outcome_payload_type_0

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
