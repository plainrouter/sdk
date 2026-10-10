from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cookie_declaration_categories import CookieDeclarationCategories


T = TypeVar("T", bound="CookieDeclaration")


@_attrs_define
class CookieDeclaration:
    """
    Attributes:
        scan_date (datetime.datetime | None): Date of the latest completed scan; null when no scan has completed.
            Blocked and failed scans do not replace it.
        categories (CookieDeclarationCategories):
    """

    scan_date: datetime.datetime | None
    categories: CookieDeclarationCategories
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_date: None | str
        if isinstance(self.scan_date, datetime.datetime):
            scan_date = self.scan_date.isoformat()
        else:
            scan_date = self.scan_date

        categories = self.categories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_date": scan_date,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cookie_declaration_categories import CookieDeclarationCategories

        d = dict(src_dict)

        def _parse_scan_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scan_date_type_0 = datetime.datetime.fromisoformat(data)

                return scan_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scan_date = _parse_scan_date(d.pop("scan_date"))

        categories = CookieDeclarationCategories.from_dict(d.pop("categories"))

        cookie_declaration = cls(
            scan_date=scan_date,
            categories=categories,
        )

        cookie_declaration.additional_properties = d
        return cookie_declaration

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
