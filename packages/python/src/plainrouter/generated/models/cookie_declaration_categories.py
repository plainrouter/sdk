from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cookie_declaration_categories_analytics import CookieDeclarationCategoriesAnalytics
    from ..models.cookie_declaration_categories_functional import CookieDeclarationCategoriesFunctional
    from ..models.cookie_declaration_categories_marketing import CookieDeclarationCategoriesMarketing
    from ..models.cookie_declaration_categories_necessary import CookieDeclarationCategoriesNecessary
    from ..models.cookie_declaration_categories_unclassified import CookieDeclarationCategoriesUnclassified


T = TypeVar("T", bound="CookieDeclarationCategories")


@_attrs_define
class CookieDeclarationCategories:
    """
    Attributes:
        necessary (CookieDeclarationCategoriesNecessary):
        functional (CookieDeclarationCategoriesFunctional):
        analytics (CookieDeclarationCategoriesAnalytics):
        marketing (CookieDeclarationCategoriesMarketing):
        unclassified (CookieDeclarationCategoriesUnclassified):
    """

    necessary: CookieDeclarationCategoriesNecessary
    functional: CookieDeclarationCategoriesFunctional
    analytics: CookieDeclarationCategoriesAnalytics
    marketing: CookieDeclarationCategoriesMarketing
    unclassified: CookieDeclarationCategoriesUnclassified
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        necessary = self.necessary.to_dict()

        functional = self.functional.to_dict()

        analytics = self.analytics.to_dict()

        marketing = self.marketing.to_dict()

        unclassified = self.unclassified.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "necessary": necessary,
                "functional": functional,
                "analytics": analytics,
                "marketing": marketing,
                "unclassified": unclassified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cookie_declaration_categories_analytics import CookieDeclarationCategoriesAnalytics
        from ..models.cookie_declaration_categories_functional import CookieDeclarationCategoriesFunctional
        from ..models.cookie_declaration_categories_marketing import CookieDeclarationCategoriesMarketing
        from ..models.cookie_declaration_categories_necessary import CookieDeclarationCategoriesNecessary
        from ..models.cookie_declaration_categories_unclassified import CookieDeclarationCategoriesUnclassified

        d = dict(src_dict)
        necessary = CookieDeclarationCategoriesNecessary.from_dict(d.pop("necessary"))

        functional = CookieDeclarationCategoriesFunctional.from_dict(d.pop("functional"))

        analytics = CookieDeclarationCategoriesAnalytics.from_dict(d.pop("analytics"))

        marketing = CookieDeclarationCategoriesMarketing.from_dict(d.pop("marketing"))

        unclassified = CookieDeclarationCategoriesUnclassified.from_dict(d.pop("unclassified"))

        cookie_declaration_categories = cls(
            necessary=necessary,
            functional=functional,
            analytics=analytics,
            marketing=marketing,
            unclassified=unclassified,
        )

        cookie_declaration_categories.additional_properties = d
        return cookie_declaration_categories

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
