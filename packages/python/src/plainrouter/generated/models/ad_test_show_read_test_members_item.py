from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdTestShowReadTestMembersItem")


@_attrs_define
class AdTestShowReadTestMembersItem:
    """
    Attributes:
        ad_id (str):
        position (int):
        baseline_host (None | str | Unset): Immutable normalized landing host once the member has a baseline.
        baseline_path (None | str | Unset): Immutable normalized landing path once the member has a baseline.
    """

    ad_id: str
    position: int
    baseline_host: None | str | Unset = UNSET
    baseline_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_id = self.ad_id

        position = self.position

        baseline_host: None | str | Unset
        if isinstance(self.baseline_host, Unset):
            baseline_host = UNSET
        else:
            baseline_host = self.baseline_host

        baseline_path: None | str | Unset
        if isinstance(self.baseline_path, Unset):
            baseline_path = UNSET
        else:
            baseline_path = self.baseline_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ad_id": ad_id,
                "position": position,
            }
        )
        if baseline_host is not UNSET:
            field_dict["baseline_host"] = baseline_host
        if baseline_path is not UNSET:
            field_dict["baseline_path"] = baseline_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_id = d.pop("ad_id")

        position = d.pop("position")

        def _parse_baseline_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        baseline_host = _parse_baseline_host(d.pop("baseline_host", UNSET))

        def _parse_baseline_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        baseline_path = _parse_baseline_path(d.pop("baseline_path", UNSET))

        ad_test_show_read_test_members_item = cls(
            ad_id=ad_id,
            position=position,
            baseline_host=baseline_host,
            baseline_path=baseline_path,
        )

        ad_test_show_read_test_members_item.additional_properties = d
        return ad_test_show_read_test_members_item

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
