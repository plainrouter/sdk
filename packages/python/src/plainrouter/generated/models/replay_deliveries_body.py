from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayDeliveriesBody")


@_attrs_define
class ReplayDeliveriesBody:
    """
    Attributes:
        delivery_ids (list[int] | Unset):
        event_name (None | str | Unset):
        limit (int | None | Unset):
    """

    delivery_ids: list[int] | Unset = UNSET
    event_name: None | str | Unset = UNSET
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_ids: list[int] | Unset = UNSET
        if not isinstance(self.delivery_ids, Unset):
            delivery_ids = self.delivery_ids

        event_name: None | str | Unset
        if isinstance(self.event_name, Unset):
            event_name = UNSET
        else:
            event_name = self.event_name

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_ids is not UNSET:
            field_dict["delivery_ids"] = delivery_ids
        if event_name is not UNSET:
            field_dict["event_name"] = event_name
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_ids = cast(list[int], d.pop("delivery_ids", UNSET))

        def _parse_event_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name = _parse_event_name(d.pop("event_name", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        replay_deliveries_body = cls(
            delivery_ids=delivery_ids,
            event_name=event_name,
            limit=limit,
        )

        replay_deliveries_body.additional_properties = d
        return replay_deliveries_body

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
