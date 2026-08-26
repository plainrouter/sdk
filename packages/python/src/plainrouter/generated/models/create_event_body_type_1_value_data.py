from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEventBodyType1ValueData")


@_attrs_define
class CreateEventBodyType1ValueData:
    """Optional commerce data. Contents accepts at most 50 items and 16 KB serialized.

    Attributes:
        value (str | Unset):
        currency (str | Unset):
        order_id (str | Unset):
        contents (list[Any] | Unset):
        num_items (int | Unset):
    """

    value: str | Unset = UNSET
    currency: str | Unset = UNSET
    order_id: str | Unset = UNSET
    contents: list[Any] | Unset = UNSET
    num_items: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        order_id = self.order_id

        contents: list[Any] | Unset = UNSET
        if not isinstance(self.contents, Unset):
            contents = self.contents

        num_items = self.num_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if currency is not UNSET:
            field_dict["currency"] = currency
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if contents is not UNSET:
            field_dict["contents"] = contents
        if num_items is not UNSET:
            field_dict["num_items"] = num_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        currency = d.pop("currency", UNSET)

        order_id = d.pop("order_id", UNSET)

        contents = cast(list[Any], d.pop("contents", UNSET))

        num_items = d.pop("num_items", UNSET)

        create_event_body_type_1_value_data = cls(
            value=value,
            currency=currency,
            order_id=order_id,
            contents=contents,
            num_items=num_items,
        )

        create_event_body_type_1_value_data.additional_properties = d
        return create_event_body_type_1_value_data

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
