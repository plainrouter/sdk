from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_read_item_counted_evidence_type_0_counted import ActionReadItemCountedEvidenceType0Counted
    from ..models.action_read_item_counted_evidence_type_0_coverage import ActionReadItemCountedEvidenceType0Coverage
    from ..models.action_read_item_counted_evidence_type_0_meta_reported import (
        ActionReadItemCountedEvidenceType0MetaReported,
    )
    from ..models.action_read_item_counted_evidence_type_0_target import ActionReadItemCountedEvidenceType0Target
    from ..models.action_read_item_counted_evidence_type_0_window_type_0 import (
        ActionReadItemCountedEvidenceType0WindowType0,
    )


T = TypeVar("T", bound="ActionReadItemCountedEvidenceType0")


@_attrs_define
class ActionReadItemCountedEvidenceType0:
    """Frozen proposal-time target figures over completed account-local dates. Purchase values are decimal strings in the
    account currency; counted values in other currencies are excluded and never converted. Null means figures were not
    captured. Display only; never an enforcement input.

        Attributes:
            target (ActionReadItemCountedEvidenceType0Target):
            captured_at (str):
            window (ActionReadItemCountedEvidenceType0WindowType0 | None):
            currency (None | str):
            currency_note (str):
            meta_reported (ActionReadItemCountedEvidenceType0MetaReported):
            counted (ActionReadItemCountedEvidenceType0Counted):
            coverage (ActionReadItemCountedEvidenceType0Coverage):
    """

    target: ActionReadItemCountedEvidenceType0Target
    captured_at: str
    window: ActionReadItemCountedEvidenceType0WindowType0 | None
    currency: None | str
    currency_note: str
    meta_reported: ActionReadItemCountedEvidenceType0MetaReported
    counted: ActionReadItemCountedEvidenceType0Counted
    coverage: ActionReadItemCountedEvidenceType0Coverage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_read_item_counted_evidence_type_0_window_type_0 import (
            ActionReadItemCountedEvidenceType0WindowType0,
        )

        target = self.target.to_dict()

        captured_at = self.captured_at

        window: dict[str, Any] | None
        if isinstance(self.window, ActionReadItemCountedEvidenceType0WindowType0):
            window = self.window.to_dict()
        else:
            window = self.window

        currency: None | str
        currency = self.currency

        currency_note = self.currency_note

        meta_reported = self.meta_reported.to_dict()

        counted = self.counted.to_dict()

        coverage = self.coverage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "captured_at": captured_at,
                "window": window,
                "currency": currency,
                "currency_note": currency_note,
                "meta_reported": meta_reported,
                "counted": counted,
                "coverage": coverage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_read_item_counted_evidence_type_0_counted import ActionReadItemCountedEvidenceType0Counted
        from ..models.action_read_item_counted_evidence_type_0_coverage import (
            ActionReadItemCountedEvidenceType0Coverage,
        )
        from ..models.action_read_item_counted_evidence_type_0_meta_reported import (
            ActionReadItemCountedEvidenceType0MetaReported,
        )
        from ..models.action_read_item_counted_evidence_type_0_target import ActionReadItemCountedEvidenceType0Target
        from ..models.action_read_item_counted_evidence_type_0_window_type_0 import (
            ActionReadItemCountedEvidenceType0WindowType0,
        )

        d = dict(src_dict)
        target = ActionReadItemCountedEvidenceType0Target.from_dict(d.pop("target"))

        captured_at = d.pop("captured_at")

        def _parse_window(data: object) -> ActionReadItemCountedEvidenceType0WindowType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = ActionReadItemCountedEvidenceType0WindowType0.from_dict(data)

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionReadItemCountedEvidenceType0WindowType0 | None, data)

        window = _parse_window(d.pop("window"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        currency_note = d.pop("currency_note")

        meta_reported = ActionReadItemCountedEvidenceType0MetaReported.from_dict(d.pop("meta_reported"))

        counted = ActionReadItemCountedEvidenceType0Counted.from_dict(d.pop("counted"))

        coverage = ActionReadItemCountedEvidenceType0Coverage.from_dict(d.pop("coverage"))

        action_read_item_counted_evidence_type_0 = cls(
            target=target,
            captured_at=captured_at,
            window=window,
            currency=currency,
            currency_note=currency_note,
            meta_reported=meta_reported,
            counted=counted,
            coverage=coverage,
        )

        action_read_item_counted_evidence_type_0.additional_properties = d
        return action_read_item_counted_evidence_type_0

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
