from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAccountInventoryResponse404")


@_attrs_define
class GetAccountInventoryResponse404:
    """
    Attributes:
        message (Literal['Account not found.']):
    """

    message: Literal["Account not found."]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = cast(Literal["Account not found."], d.pop("message"))
        if message != "Account not found.":
            raise ValueError(f"message must match const 'Account not found.', got '{message}'")

        get_account_inventory_response_404 = cls(
            message=message,
        )

        get_account_inventory_response_404.additional_properties = d
        return get_account_inventory_response_404

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
