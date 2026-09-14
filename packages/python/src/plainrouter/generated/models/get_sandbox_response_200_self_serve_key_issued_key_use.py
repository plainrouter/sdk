from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSandboxResponse200SelfServeKeyIssuedKeyUse")


@_attrs_define
class GetSandboxResponse200SelfServeKeyIssuedKeyUse:
    """
    Attributes:
        method (str):
        url (str):
        authorization (str):
    """

    method: str
    url: str
    authorization: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        authorization = self.authorization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
                "authorization": authorization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method")

        url = d.pop("url")

        authorization = d.pop("authorization")

        get_sandbox_response_200_self_serve_key_issued_key_use = cls(
            method=method,
            url=url,
            authorization=authorization,
        )

        get_sandbox_response_200_self_serve_key_issued_key_use.additional_properties = d
        return get_sandbox_response_200_self_serve_key_issued_key_use

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
