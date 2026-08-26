from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sandbox_response_200_self_serve_key import GetSandboxResponse200SelfServeKey
    from ..models.get_sandbox_response_200_try import GetSandboxResponse200Try


T = TypeVar("T", bound="GetSandboxResponse200")


@_attrs_define
class GetSandboxResponse200:
    """
    Attributes:
        environment (str):
        authentication_required (bool):
        account_required (bool):
        production_data (bool):
        persists_data (bool):
        provider_delivery (bool):
        description (str):
        self_serve_key (GetSandboxResponse200SelfServeKey):
        try_ (GetSandboxResponse200Try):
    """

    environment: str
    authentication_required: bool
    account_required: bool
    production_data: bool
    persists_data: bool
    provider_delivery: bool
    description: str
    self_serve_key: GetSandboxResponse200SelfServeKey
    try_: GetSandboxResponse200Try
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment

        authentication_required = self.authentication_required

        account_required = self.account_required

        production_data = self.production_data

        persists_data = self.persists_data

        provider_delivery = self.provider_delivery

        description = self.description

        self_serve_key = self.self_serve_key.to_dict()

        try_ = self.try_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "authentication_required": authentication_required,
                "account_required": account_required,
                "production_data": production_data,
                "persists_data": persists_data,
                "provider_delivery": provider_delivery,
                "description": description,
                "self_serve_key": self_serve_key,
                "try": try_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sandbox_response_200_self_serve_key import GetSandboxResponse200SelfServeKey
        from ..models.get_sandbox_response_200_try import GetSandboxResponse200Try

        d = dict(src_dict)
        environment = d.pop("environment")

        authentication_required = d.pop("authentication_required")

        account_required = d.pop("account_required")

        production_data = d.pop("production_data")

        persists_data = d.pop("persists_data")

        provider_delivery = d.pop("provider_delivery")

        description = d.pop("description")

        self_serve_key = GetSandboxResponse200SelfServeKey.from_dict(d.pop("self_serve_key"))

        try_ = GetSandboxResponse200Try.from_dict(d.pop("try"))

        get_sandbox_response_200 = cls(
            environment=environment,
            authentication_required=authentication_required,
            account_required=account_required,
            production_data=production_data,
            persists_data=persists_data,
            provider_delivery=provider_delivery,
            description=description,
            self_serve_key=self_serve_key,
            try_=try_,
        )

        get_sandbox_response_200.additional_properties = d
        return get_sandbox_response_200

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
