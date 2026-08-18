from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetReconciliationReportResponse200ReportsItemBucketsAdditionalProperty")


@_attrs_define
class GetReconciliationReportResponse200ReportsItemBucketsAdditionalProperty:
    """
    Attributes:
        count (int):
        basis (str):
        explanation (str):
    """

    count: int
    basis: str
    explanation: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        basis = self.basis

        explanation = self.explanation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "basis": basis,
                "explanation": explanation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        basis = d.pop("basis")

        explanation = d.pop("explanation")

        get_reconciliation_report_response_200_reports_item_buckets_additional_property = cls(
            count=count,
            basis=basis,
            explanation=explanation,
        )

        get_reconciliation_report_response_200_reports_item_buckets_additional_property.additional_properties = d
        return get_reconciliation_report_response_200_reports_item_buckets_additional_property

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
