from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_route_not_found_error import ApiRouteNotFoundError
    from ..models.api_route_not_found_request import ApiRouteNotFoundRequest
    from ..models.api_route_not_found_resources import ApiRouteNotFoundResources


T = TypeVar("T", bound="ApiRouteNotFound")


@_attrs_define
class ApiRouteNotFound:
    """
    Attributes:
        error (ApiRouteNotFoundError):
        request (ApiRouteNotFoundRequest):
        resources (ApiRouteNotFoundResources):
    """

    error: ApiRouteNotFoundError
    request: ApiRouteNotFoundRequest
    resources: ApiRouteNotFoundResources
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        request = self.request.to_dict()

        resources = self.resources.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "request": request,
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_route_not_found_error import ApiRouteNotFoundError
        from ..models.api_route_not_found_request import ApiRouteNotFoundRequest
        from ..models.api_route_not_found_resources import ApiRouteNotFoundResources

        d = dict(src_dict)
        error = ApiRouteNotFoundError.from_dict(d.pop("error"))

        request = ApiRouteNotFoundRequest.from_dict(d.pop("request"))

        resources = ApiRouteNotFoundResources.from_dict(d.pop("resources"))

        api_route_not_found = cls(
            error=error,
            request=request,
            resources=resources,
        )

        api_route_not_found.additional_properties = d
        return api_route_not_found

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
