from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateSandboxEventWithKeyBodyValueData")


@_attrs_define
class ValidateSandboxEventWithKeyBodyValueData:
    """Optional synthetic commerce data.

    Attributes:
        value (str | Unset):
        currency (str | Unset):
        order_id (str | Unset):
    """

    value: str | Unset = UNSET
    currency: str | Unset = UNSET
    order_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        order_id = self.order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if currency is not UNSET:
            field_dict["currency"] = currency
        if order_id is not UNSET:
            field_dict["order_id"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        currency = d.pop("currency", UNSET)

        order_id = d.pop("order_id", UNSET)

        validate_sandbox_event_with_key_body_value_data = cls(
            value=value,
            currency=currency,
            order_id=order_id,
        )

        validate_sandbox_event_with_key_body_value_data.additional_properties = d
        return validate_sandbox_event_with_key_body_value_data

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
