from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_reconciliation_report_response_200_reports_item_event_counts_accepted_type_0 import (
        GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0,
    )
    from ..models.get_reconciliation_report_response_200_reports_item_event_counts_meta_type_0 import (
        GetReconciliationReportResponse200ReportsItemEventCountsMetaType0,
    )


T = TypeVar("T", bound="GetReconciliationReportResponse200ReportsItemEventCounts")


@_attrs_define
class GetReconciliationReportResponse200ReportsItemEventCounts:
    """
    Attributes:
        accepted (GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0 | list[Any]):
        meta (GetReconciliationReportResponse200ReportsItemEventCountsMetaType0 | list[Any]):
    """

    accepted: GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0 | list[Any]
    meta: GetReconciliationReportResponse200ReportsItemEventCountsMetaType0 | list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_reconciliation_report_response_200_reports_item_event_counts_accepted_type_0 import (
            GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0,
        )
        from ..models.get_reconciliation_report_response_200_reports_item_event_counts_meta_type_0 import (
            GetReconciliationReportResponse200ReportsItemEventCountsMetaType0,
        )

        accepted: dict[str, Any] | list[Any]
        if isinstance(self.accepted, GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0):
            accepted = self.accepted.to_dict()
        else:
            accepted = self.accepted

        meta: dict[str, Any] | list[Any]
        if isinstance(self.meta, GetReconciliationReportResponse200ReportsItemEventCountsMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_reconciliation_report_response_200_reports_item_event_counts_accepted_type_0 import (
            GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0,
        )
        from ..models.get_reconciliation_report_response_200_reports_item_event_counts_meta_type_0 import (
            GetReconciliationReportResponse200ReportsItemEventCountsMetaType0,
        )

        d = dict(src_dict)

        def _parse_accepted(
            data: object,
        ) -> GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accepted_type_0 = GetReconciliationReportResponse200ReportsItemEventCountsAcceptedType0.from_dict(data)

                return accepted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            accepted_type_1 = cast(list[Any], data)

            return accepted_type_1

        accepted = _parse_accepted(d.pop("accepted"))

        def _parse_meta(data: object) -> GetReconciliationReportResponse200ReportsItemEventCountsMetaType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = GetReconciliationReportResponse200ReportsItemEventCountsMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            meta_type_1 = cast(list[Any], data)

            return meta_type_1

        meta = _parse_meta(d.pop("meta"))

        get_reconciliation_report_response_200_reports_item_event_counts = cls(
            accepted=accepted,
            meta=meta,
        )

        get_reconciliation_report_response_200_reports_item_event_counts.additional_properties = d
        return get_reconciliation_report_response_200_reports_item_event_counts

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
