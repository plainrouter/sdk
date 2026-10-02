from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiRouteNotFoundResources")


@_attrs_define
class ApiRouteNotFoundResources:
    """
    Attributes:
        documentation (str):
        openapi (str):
    """

    documentation: str
    openapi: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documentation = self.documentation

        openapi = self.openapi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentation": documentation,
                "openapi": openapi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        documentation = d.pop("documentation")

        openapi = d.pop("openapi")

        api_route_not_found_resources = cls(
            documentation=documentation,
            openapi=openapi,
        )

        api_route_not_found_resources.additional_properties = d
        return api_route_not_found_resources

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
