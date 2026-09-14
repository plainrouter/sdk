from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sandbox_response_200_self_serve_key_issued_key import GetSandboxResponse200SelfServeKeyIssuedKey


T = TypeVar("T", bound="GetSandboxResponse200SelfServeKey")


@_attrs_define
class GetSandboxResponse200SelfServeKey:
    """
    Attributes:
        method (str):
        url (str):
        authentication_required (bool):
        description (str):
        issued_key (GetSandboxResponse200SelfServeKeyIssuedKey):
    """

    method: str
    url: str
    authentication_required: bool
    description: str
    issued_key: GetSandboxResponse200SelfServeKeyIssuedKey
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        authentication_required = self.authentication_required

        description = self.description

        issued_key = self.issued_key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
                "authentication_required": authentication_required,
                "description": description,
                "issued_key": issued_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sandbox_response_200_self_serve_key_issued_key import (
            GetSandboxResponse200SelfServeKeyIssuedKey,
        )

        d = dict(src_dict)
        method = d.pop("method")

        url = d.pop("url")

        authentication_required = d.pop("authentication_required")

        description = d.pop("description")

        issued_key = GetSandboxResponse200SelfServeKeyIssuedKey.from_dict(d.pop("issued_key"))

        get_sandbox_response_200_self_serve_key = cls(
            method=method,
            url=url,
            authentication_required=authentication_required,
            description=description,
            issued_key=issued_key,
        )

        get_sandbox_response_200_self_serve_key.additional_properties = d
        return get_sandbox_response_200_self_serve_key

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
