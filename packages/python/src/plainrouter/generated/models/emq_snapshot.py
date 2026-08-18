from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmqSnapshot")


@_attrs_define
class EmqSnapshot:
    """
    Attributes:
        id (int):
        signal_tracker_id (str):
        destination_id (str):
        score (float):
        week_over_week_change (float | None):
        alerted (bool):
        platform_response (list[Any] | None):
        measured_at (datetime.datetime):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
    """

    id: int
    signal_tracker_id: str
    destination_id: str
    score: float
    week_over_week_change: float | None
    alerted: bool
    platform_response: list[Any] | None
    measured_at: datetime.datetime
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signal_tracker_id = self.signal_tracker_id

        destination_id = self.destination_id

        score = self.score

        week_over_week_change: float | None
        week_over_week_change = self.week_over_week_change

        alerted = self.alerted

        platform_response: list[Any] | None
        if isinstance(self.platform_response, list):
            platform_response = self.platform_response

        else:
            platform_response = self.platform_response

        measured_at = self.measured_at.isoformat()

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

        def _parse_platform_response(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platform_response_type_0 = cast(list[Any], data)

                return platform_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        platform_response = _parse_platform_response(d.pop("platform_response"))

        measured_at = datetime.datetime.fromisoformat(d.pop("measured_at"))

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

        emq_snapshot = cls(
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

        emq_snapshot.additional_properties = d
        return emq_snapshot

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
