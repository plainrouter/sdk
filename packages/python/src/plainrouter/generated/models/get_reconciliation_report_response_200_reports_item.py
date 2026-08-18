from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_reconciliation_report_response_200_reports_item_buckets import (
        GetReconciliationReportResponse200ReportsItemBuckets,
    )
    from ..models.get_reconciliation_report_response_200_reports_item_destination import (
        GetReconciliationReportResponse200ReportsItemDestination,
    )
    from ..models.get_reconciliation_report_response_200_reports_item_event_counts import (
        GetReconciliationReportResponse200ReportsItemEventCounts,
    )


T = TypeVar("T", bound="GetReconciliationReportResponse200ReportsItem")


@_attrs_define
class GetReconciliationReportResponse200ReportsItem:
    """
    Attributes:
        id (int):
        signal_tracker_id (str):
        destination_id (str):
        report_date (str):
        accepted_count (int):
        meta_count (int):
        observed_gap (int):
        event_counts (GetReconciliationReportResponse200ReportsItemEventCounts):
        buckets (GetReconciliationReportResponse200ReportsItemBuckets):
        unexplained_residual (int):
        status (str):
        created_at (None | str):
        updated_at (None | str):
        destination (GetReconciliationReportResponse200ReportsItemDestination):
    """

    id: int
    signal_tracker_id: str
    destination_id: str
    report_date: str
    accepted_count: int
    meta_count: int
    observed_gap: int
    event_counts: GetReconciliationReportResponse200ReportsItemEventCounts
    buckets: GetReconciliationReportResponse200ReportsItemBuckets
    unexplained_residual: int
    status: str
    created_at: None | str
    updated_at: None | str
    destination: GetReconciliationReportResponse200ReportsItemDestination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signal_tracker_id = self.signal_tracker_id

        destination_id = self.destination_id

        report_date = self.report_date

        accepted_count = self.accepted_count

        meta_count = self.meta_count

        observed_gap = self.observed_gap

        event_counts = self.event_counts.to_dict()

        buckets = self.buckets.to_dict()

        unexplained_residual = self.unexplained_residual

        status = self.status

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        destination = self.destination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "destination_id": destination_id,
                "report_date": report_date,
                "accepted_count": accepted_count,
                "meta_count": meta_count,
                "observed_gap": observed_gap,
                "event_counts": event_counts,
                "buckets": buckets,
                "unexplained_residual": unexplained_residual,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "destination": destination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_reconciliation_report_response_200_reports_item_buckets import (
            GetReconciliationReportResponse200ReportsItemBuckets,
        )
        from ..models.get_reconciliation_report_response_200_reports_item_destination import (
            GetReconciliationReportResponse200ReportsItemDestination,
        )
        from ..models.get_reconciliation_report_response_200_reports_item_event_counts import (
            GetReconciliationReportResponse200ReportsItemEventCounts,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        destination_id = d.pop("destination_id")

        report_date = d.pop("report_date")

        accepted_count = d.pop("accepted_count")

        meta_count = d.pop("meta_count")

        observed_gap = d.pop("observed_gap")

        event_counts = GetReconciliationReportResponse200ReportsItemEventCounts.from_dict(d.pop("event_counts"))

        buckets = GetReconciliationReportResponse200ReportsItemBuckets.from_dict(d.pop("buckets"))

        unexplained_residual = d.pop("unexplained_residual")

        status = d.pop("status")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        destination = GetReconciliationReportResponse200ReportsItemDestination.from_dict(d.pop("destination"))

        get_reconciliation_report_response_200_reports_item = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            destination_id=destination_id,
            report_date=report_date,
            accepted_count=accepted_count,
            meta_count=meta_count,
            observed_gap=observed_gap,
            event_counts=event_counts,
            buckets=buckets,
            unexplained_residual=unexplained_residual,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            destination=destination,
        )

        get_reconciliation_report_response_200_reports_item.additional_properties = d
        return get_reconciliation_report_response_200_reports_item

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
