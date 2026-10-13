from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.launch_creatives_index_response_200_creatives import LaunchCreativesIndexResponse200Creatives


T = TypeVar("T", bound="LaunchCreativesIndexResponse200")


@_attrs_define
class LaunchCreativesIndexResponse200:
    """
    Attributes:
        creatives (LaunchCreativesIndexResponse200Creatives): Complete projection rows are paged within 80,000 JSON
            bytes, accounting for both MCP representations. Defaults are bounded. Follow next_cursor with the same scope and
            filters. One oversized row is explicitly refused; fields are never silently clipped.
    """

    creatives: LaunchCreativesIndexResponse200Creatives
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creatives = self.creatives.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creatives": creatives,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_creatives_index_response_200_creatives import LaunchCreativesIndexResponse200Creatives

        d = dict(src_dict)
        creatives = LaunchCreativesIndexResponse200Creatives.from_dict(d.pop("creatives"))

        launch_creatives_index_response_200 = cls(
            creatives=creatives,
        )

        launch_creatives_index_response_200.additional_properties = d
        return launch_creatives_index_response_200

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
