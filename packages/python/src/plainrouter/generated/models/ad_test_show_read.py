from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ad_test_show_read_test import AdTestShowReadTest


T = TypeVar("T", bound="AdTestShowRead")


@_attrs_define
class AdTestShowRead:
    """
    Attributes:
        test (AdTestShowReadTest):
    """

    test: AdTestShowReadTest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test = self.test.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test": test,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_test_show_read_test import AdTestShowReadTest

        d = dict(src_dict)
        test = AdTestShowReadTest.from_dict(d.pop("test"))

        ad_test_show_read = cls(
            test=test,
        )

        ad_test_show_read.additional_properties = d
        return ad_test_show_read

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
