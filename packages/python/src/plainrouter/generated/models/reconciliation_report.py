from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReconciliationReport")


@_attrs_define
class ReconciliationReport:
    """
    Attributes:
        id (int):
        signal_tracker_id (str):
        destination_id (str):
        report_date (datetime.datetime):
        accepted_count (int):
        meta_count (int):
        observed_gap (int):
        event_counts (list[Any]):
        buckets (list[Any]):
        unexplained_residual (int):
        status (str):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
        claimed_clicks (int | None):
    """

    id: int
    signal_tracker_id: str
    destination_id: str
    report_date: datetime.datetime
    accepted_count: int
    meta_count: int
    observed_gap: int
    event_counts: list[Any]
    buckets: list[Any]
    unexplained_residual: int
    status: str
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    claimed_clicks: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signal_tracker_id = self.signal_tracker_id

        destination_id = self.destination_id

        report_date = self.report_date.isoformat()

        accepted_count = self.accepted_count

        meta_count = self.meta_count

        observed_gap = self.observed_gap

        event_counts = self.event_counts

        buckets = self.buckets

        unexplained_residual = self.unexplained_residual

        status = self.status

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        claimed_clicks: int | None
        claimed_clicks = self.claimed_clicks

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
                "claimed_clicks": claimed_clicks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        destination_id = d.pop("destination_id")

        report_date = datetime.datetime.fromisoformat(d.pop("report_date"))

        accepted_count = d.pop("accepted_count")

        meta_count = d.pop("meta_count")

        observed_gap = d.pop("observed_gap")

        event_counts = cast(list[Any], d.pop("event_counts"))

        buckets = cast(list[Any], d.pop("buckets"))

        unexplained_residual = d.pop("unexplained_residual")

        status = d.pop("status")

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

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_claimed_clicks(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        claimed_clicks = _parse_claimed_clicks(d.pop("claimed_clicks"))

        reconciliation_report = cls(
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
            claimed_clicks=claimed_clicks,
        )

        reconciliation_report.additional_properties = d
        return reconciliation_report

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
