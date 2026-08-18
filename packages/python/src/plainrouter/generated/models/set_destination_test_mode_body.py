from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetDestinationTestModeBody")


@_attrs_define
class SetDestinationTestModeBody:
    """
    Attributes:
        enabled (bool):
        test_event_code (None | str | Unset):
    """

    enabled: bool
    test_event_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        test_event_code: None | str | Unset
        if isinstance(self.test_event_code, Unset):
            test_event_code = UNSET
        else:
            test_event_code = self.test_event_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if test_event_code is not UNSET:
            field_dict["test_event_code"] = test_event_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_test_event_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_event_code = _parse_test_event_code(d.pop("test_event_code", UNSET))

        set_destination_test_mode_body = cls(
            enabled=enabled,
            test_event_code=test_event_code,
        )

        set_destination_test_mode_body.additional_properties = d
        return set_destination_test_mode_body

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
