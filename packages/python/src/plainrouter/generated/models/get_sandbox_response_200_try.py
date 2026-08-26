from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sandbox_response_200_try_body import GetSandboxResponse200TryBody


T = TypeVar("T", bound="GetSandboxResponse200Try")


@_attrs_define
class GetSandboxResponse200Try:
    """
    Attributes:
        method (str):
        url (str):
        content_type (str):
        body (GetSandboxResponse200TryBody):
    """

    method: str
    url: str
    content_type: str
    body: GetSandboxResponse200TryBody
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        content_type = self.content_type

        body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
                "content_type": content_type,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sandbox_response_200_try_body import GetSandboxResponse200TryBody

        d = dict(src_dict)
        method = d.pop("method")

        url = d.pop("url")

        content_type = d.pop("content_type")

        body = GetSandboxResponse200TryBody.from_dict(d.pop("body"))

        get_sandbox_response_200_try = cls(
            method=method,
            url=url,
            content_type=content_type,
            body=body,
        )

        get_sandbox_response_200_try.additional_properties = d
        return get_sandbox_response_200_try

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
