from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cookie_declaration_item import CookieDeclarationItem


T = TypeVar("T", bound="CookieDeclarationCategoriesFunctional")


@_attrs_define
class CookieDeclarationCategoriesFunctional:
    """
    Attributes:
        cookies (list[CookieDeclarationItem]):
        storage_keys (list[CookieDeclarationItem]):
    """

    cookies: list[CookieDeclarationItem]
    storage_keys: list[CookieDeclarationItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cookies = []
        for cookies_item_data in self.cookies:
            cookies_item = cookies_item_data.to_dict()
            cookies.append(cookies_item)

        storage_keys = []
        for storage_keys_item_data in self.storage_keys:
            storage_keys_item = storage_keys_item_data.to_dict()
            storage_keys.append(storage_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cookies": cookies,
                "storage_keys": storage_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cookie_declaration_item import CookieDeclarationItem

        d = dict(src_dict)
        cookies = []
        _cookies = d.pop("cookies")
        for cookies_item_data in _cookies:
            cookies_item = CookieDeclarationItem.from_dict(cookies_item_data)

            cookies.append(cookies_item)

        storage_keys = []
        _storage_keys = d.pop("storage_keys")
        for storage_keys_item_data in _storage_keys:
            storage_keys_item = CookieDeclarationItem.from_dict(storage_keys_item_data)

            storage_keys.append(storage_keys_item)

        cookie_declaration_categories_functional = cls(
            cookies=cookies,
            storage_keys=storage_keys,
        )

        cookie_declaration_categories_functional.additional_properties = d
        return cookie_declaration_categories_functional

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
