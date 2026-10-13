from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionReadItemCountedEvidenceType0MetaReported")


@_attrs_define
class ActionReadItemCountedEvidenceType0MetaReported:
    """
    Attributes:
        inline_link_clicks (int | None):
        purchase_count (int | None):
        purchase_value (None | str):
        spend (None | str):
        impressions (int | None):
    """

    inline_link_clicks: int | None
    purchase_count: int | None
    purchase_value: None | str
    spend: None | str
    impressions: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inline_link_clicks: int | None
        inline_link_clicks = self.inline_link_clicks

        purchase_count: int | None
        purchase_count = self.purchase_count

        purchase_value: None | str
        purchase_value = self.purchase_value

        spend: None | str
        spend = self.spend

        impressions: int | None
        impressions = self.impressions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inline_link_clicks": inline_link_clicks,
                "purchase_count": purchase_count,
                "purchase_value": purchase_value,
                "spend": spend,
                "impressions": impressions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_inline_link_clicks(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        inline_link_clicks = _parse_inline_link_clicks(d.pop("inline_link_clicks"))

        def _parse_purchase_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_count = _parse_purchase_count(d.pop("purchase_count"))

        def _parse_purchase_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_value = _parse_purchase_value(d.pop("purchase_value"))

        def _parse_spend(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        spend = _parse_spend(d.pop("spend"))

        def _parse_impressions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        impressions = _parse_impressions(d.pop("impressions"))

        action_read_item_counted_evidence_type_0_meta_reported = cls(
            inline_link_clicks=inline_link_clicks,
            purchase_count=purchase_count,
            purchase_value=purchase_value,
            spend=spend,
            impressions=impressions,
        )

        action_read_item_counted_evidence_type_0_meta_reported.additional_properties = d
        return action_read_item_counted_evidence_type_0_meta_reported

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
