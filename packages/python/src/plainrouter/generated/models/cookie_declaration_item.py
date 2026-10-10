from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cookie_declaration_item_party import CookieDeclarationItemParty

T = TypeVar("T", bound="CookieDeclarationItem")


@_attrs_define
class CookieDeclarationItem:
    """
    Attributes:
        name (str):
        provider_domain (str):
        party (CookieDeclarationItemParty):
        expiry (str): Observed UTC expiry date, Session, or Until removed.
        purpose (None | str): Purpose from the Open Cookie Database, where available.
    """

    name: str
    provider_domain: str
    party: CookieDeclarationItemParty
    expiry: str
    purpose: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_domain = self.provider_domain

        party = self.party.value

        expiry = self.expiry

        purpose: None | str
        purpose = self.purpose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "provider_domain": provider_domain,
                "party": party,
                "expiry": expiry,
                "purpose": purpose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        provider_domain = d.pop("provider_domain")

        party = CookieDeclarationItemParty(d.pop("party"))

        expiry = d.pop("expiry")

        def _parse_purpose(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purpose = _parse_purpose(d.pop("purpose"))

        cookie_declaration_item = cls(
            name=name,
            provider_domain=provider_domain,
            party=party,
            expiry=expiry,
            purpose=purpose,
        )

        cookie_declaration_item.additional_properties = d
        return cookie_declaration_item

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
