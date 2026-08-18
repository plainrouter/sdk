from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_emq_report_response_200_snapshots_item_platform_response_type_0 import (
        GetEmqReportResponse200SnapshotsItemPlatformResponseType0,
    )


T = TypeVar("T", bound="GetEmqReportResponse200SnapshotsItem")


@_attrs_define
class GetEmqReportResponse200SnapshotsItem:
    """
    Attributes:
        id (int):
        signal_tracker_id (str):
        destination_id (str):
        score (float):
        week_over_week_change (float | None):
        alerted (bool):
        platform_response (GetEmqReportResponse200SnapshotsItemPlatformResponseType0 | list[Any] | None):
        measured_at (str):
        created_at (None | str):
        updated_at (None | str):
    """

    id: int
    signal_tracker_id: str
    destination_id: str
    score: float
    week_over_week_change: float | None
    alerted: bool
    platform_response: GetEmqReportResponse200SnapshotsItemPlatformResponseType0 | list[Any] | None
    measured_at: str
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_emq_report_response_200_snapshots_item_platform_response_type_0 import (
            GetEmqReportResponse200SnapshotsItemPlatformResponseType0,
        )

        id = self.id

        signal_tracker_id = self.signal_tracker_id

        destination_id = self.destination_id

        score = self.score

        week_over_week_change: float | None
        week_over_week_change = self.week_over_week_change

        alerted = self.alerted

        platform_response: dict[str, Any] | list[Any] | None
        if isinstance(self.platform_response, GetEmqReportResponse200SnapshotsItemPlatformResponseType0):
            platform_response = self.platform_response.to_dict()
        elif isinstance(self.platform_response, list):
            platform_response = self.platform_response

        else:
            platform_response = self.platform_response

        measured_at = self.measured_at

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "destination_id": destination_id,
                "score": score,
                "week_over_week_change": week_over_week_change,
                "alerted": alerted,
                "platform_response": platform_response,
                "measured_at": measured_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_emq_report_response_200_snapshots_item_platform_response_type_0 import (
            GetEmqReportResponse200SnapshotsItemPlatformResponseType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        destination_id = d.pop("destination_id")

        score = d.pop("score")

        def _parse_week_over_week_change(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        week_over_week_change = _parse_week_over_week_change(d.pop("week_over_week_change"))

        alerted = d.pop("alerted")

        def _parse_platform_response(
            data: object,
        ) -> GetEmqReportResponse200SnapshotsItemPlatformResponseType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_response_type_0 = GetEmqReportResponse200SnapshotsItemPlatformResponseType0.from_dict(data)

                return platform_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platform_response_type_1 = cast(list[Any], data)

                return platform_response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEmqReportResponse200SnapshotsItemPlatformResponseType0 | list[Any] | None, data)

        platform_response = _parse_platform_response(d.pop("platform_response"))

        measured_at = d.pop("measured_at")

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

        get_emq_report_response_200_snapshots_item = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            destination_id=destination_id,
            score=score,
            week_over_week_change=week_over_week_change,
            alerted=alerted,
            platform_response=platform_response,
            measured_at=measured_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_emq_report_response_200_snapshots_item.additional_properties = d
        return get_emq_report_response_200_snapshots_item

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
