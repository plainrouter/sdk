from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_read_item_counted_evidence_type_0_coverage_arrivals_type_0 import (
        ActionReadItemCountedEvidenceType0CoverageArrivalsType0,
    )
    from ..models.action_read_item_counted_evidence_type_0_coverage_purchases_type_0 import (
        ActionReadItemCountedEvidenceType0CoveragePurchasesType0,
    )


T = TypeVar("T", bound="ActionReadItemCountedEvidenceType0Coverage")


@_attrs_define
class ActionReadItemCountedEvidenceType0Coverage:
    """
    Attributes:
        arrivals (ActionReadItemCountedEvidenceType0CoverageArrivalsType0 | None):
        purchases (ActionReadItemCountedEvidenceType0CoveragePurchasesType0 | None):
    """

    arrivals: ActionReadItemCountedEvidenceType0CoverageArrivalsType0 | None
    purchases: ActionReadItemCountedEvidenceType0CoveragePurchasesType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_read_item_counted_evidence_type_0_coverage_arrivals_type_0 import (
            ActionReadItemCountedEvidenceType0CoverageArrivalsType0,
        )
        from ..models.action_read_item_counted_evidence_type_0_coverage_purchases_type_0 import (
            ActionReadItemCountedEvidenceType0CoveragePurchasesType0,
        )

        arrivals: dict[str, Any] | None
        if isinstance(self.arrivals, ActionReadItemCountedEvidenceType0CoverageArrivalsType0):
            arrivals = self.arrivals.to_dict()
        else:
            arrivals = self.arrivals

        purchases: dict[str, Any] | None
        if isinstance(self.purchases, ActionReadItemCountedEvidenceType0CoveragePurchasesType0):
            purchases = self.purchases.to_dict()
        else:
            purchases = self.purchases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arrivals": arrivals,
                "purchases": purchases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_read_item_counted_evidence_type_0_coverage_arrivals_type_0 import (
            ActionReadItemCountedEvidenceType0CoverageArrivalsType0,
        )
        from ..models.action_read_item_counted_evidence_type_0_coverage_purchases_type_0 import (
            ActionReadItemCountedEvidenceType0CoveragePurchasesType0,
        )

        d = dict(src_dict)

        def _parse_arrivals(data: object) -> ActionReadItemCountedEvidenceType0CoverageArrivalsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                arrivals_type_0 = ActionReadItemCountedEvidenceType0CoverageArrivalsType0.from_dict(data)

                return arrivals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionReadItemCountedEvidenceType0CoverageArrivalsType0 | None, data)

        arrivals = _parse_arrivals(d.pop("arrivals"))

        def _parse_purchases(data: object) -> ActionReadItemCountedEvidenceType0CoveragePurchasesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                purchases_type_0 = ActionReadItemCountedEvidenceType0CoveragePurchasesType0.from_dict(data)

                return purchases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionReadItemCountedEvidenceType0CoveragePurchasesType0 | None, data)

        purchases = _parse_purchases(d.pop("purchases"))

        action_read_item_counted_evidence_type_0_coverage = cls(
            arrivals=arrivals,
            purchases=purchases,
        )

        action_read_item_counted_evidence_type_0_coverage.additional_properties = d
        return action_read_item_counted_evidence_type_0_coverage

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
