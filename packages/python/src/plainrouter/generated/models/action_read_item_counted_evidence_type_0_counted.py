from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionReadItemCountedEvidenceType0Counted")


@_attrs_define
class ActionReadItemCountedEvidenceType0Counted:
    """
    Attributes:
        arrivals (int | None):
        purchase_count (int | None):
        purchase_value (None | str):
    """

    arrivals: int | None
    purchase_count: int | None
    purchase_value: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arrivals: int | None
        arrivals = self.arrivals

        purchase_count: int | None
        purchase_count = self.purchase_count

        purchase_value: None | str
        purchase_value = self.purchase_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arrivals": arrivals,
                "purchase_count": purchase_count,
                "purchase_value": purchase_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        arrivals = _parse_arrivals(d.pop("arrivals"))

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

        action_read_item_counted_evidence_type_0_counted = cls(
            arrivals=arrivals,
            purchase_count=purchase_count,
            purchase_value=purchase_value,
        )

        action_read_item_counted_evidence_type_0_counted.additional_properties = d
        return action_read_item_counted_evidence_type_0_counted

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
