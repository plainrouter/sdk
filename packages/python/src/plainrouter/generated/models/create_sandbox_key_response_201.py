from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_sandbox_key_response_201_use import CreateSandboxKeyResponse201Use


T = TypeVar("T", bound="CreateSandboxKeyResponse201")


@_attrs_define
class CreateSandboxKeyResponse201:
    """
    Attributes:
        api_key (str):
        token_type (str):
        expires_in (int):
        expires_at (str):
        scope (str):
        production_access (bool):
        use (CreateSandboxKeyResponse201Use):
    """

    api_key: str
    token_type: str
    expires_in: int
    expires_at: str
    scope: str
    production_access: bool
    use: CreateSandboxKeyResponse201Use
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        token_type = self.token_type

        expires_in = self.expires_in

        expires_at = self.expires_at

        scope = self.scope

        production_access = self.production_access

        use = self.use.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
                "token_type": token_type,
                "expires_in": expires_in,
                "expires_at": expires_at,
                "scope": scope,
                "production_access": production_access,
                "use": use,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_sandbox_key_response_201_use import CreateSandboxKeyResponse201Use

        d = dict(src_dict)
        api_key = d.pop("api_key")

        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in")

        expires_at = d.pop("expires_at")

        scope = d.pop("scope")

        production_access = d.pop("production_access")

        use = CreateSandboxKeyResponse201Use.from_dict(d.pop("use"))

        create_sandbox_key_response_201 = cls(
            api_key=api_key,
            token_type=token_type,
            expires_in=expires_in,
            expires_at=expires_at,
            scope=scope,
            production_access=production_access,
            use=use,
        )

        create_sandbox_key_response_201.additional_properties = d
        return create_sandbox_key_response_201

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
