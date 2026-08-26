from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSandboxResponse200TryBodyValueData")


@_attrs_define
class GetSandboxResponse200TryBodyValueData:
    """
    Attributes:
        value (str):
        currency (str):
        order_id (str):
    """

    value: str
    currency: str
    order_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        order_id = self.order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "currency": currency,
                "order_id": order_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        currency = d.pop("currency")

        order_id = d.pop("order_id")

        get_sandbox_response_200_try_body_value_data = cls(
            value=value,
            currency=currency,
            order_id=order_id,
        )

        get_sandbox_response_200_try_body_value_data.additional_properties = d
        return get_sandbox_response_200_try_body_value_data

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
