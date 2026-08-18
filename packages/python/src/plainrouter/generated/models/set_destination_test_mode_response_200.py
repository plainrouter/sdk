from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_destination_test_mode_response_200_destination import SetDestinationTestModeResponse200Destination


T = TypeVar("T", bound="SetDestinationTestModeResponse200")


@_attrs_define
class SetDestinationTestModeResponse200:
    """
    Attributes:
        destination (SetDestinationTestModeResponse200Destination):
        test_mode (bool):
    """

    destination: SetDestinationTestModeResponse200Destination
    test_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination.to_dict()

        test_mode = self.test_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "test_mode": test_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_destination_test_mode_response_200_destination import (
            SetDestinationTestModeResponse200Destination,
        )

        d = dict(src_dict)
        destination = SetDestinationTestModeResponse200Destination.from_dict(d.pop("destination"))

        test_mode = d.pop("test_mode")

        set_destination_test_mode_response_200 = cls(
            destination=destination,
            test_mode=test_mode,
        )

        set_destination_test_mode_response_200.additional_properties = d
        return set_destination_test_mode_response_200

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
