from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_sandbox_event_body_value_data import ValidateSandboxEventBodyValueData


T = TypeVar("T", bound="ValidateSandboxEventBody")


@_attrs_define
class ValidateSandboxEventBody:
    """
    Attributes:
        event_name (str): Synthetic event name; maximum 100 characters.
        event_id (str | Unset): Optional synthetic idempotency key; maximum 128 characters.
        action_source (str | Unset): Synthetic action source.
        value_data (ValidateSandboxEventBodyValueData | Unset): Optional synthetic commerce data.
    """

    event_name: str
    event_id: str | Unset = UNSET
    action_source: str | Unset = UNSET
    value_data: ValidateSandboxEventBodyValueData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_id = self.event_id

        action_source = self.action_source

        value_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_data, Unset):
            value_data = self.value_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_name": event_name,
            }
        )
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if action_source is not UNSET:
            field_dict["action_source"] = action_source
        if value_data is not UNSET:
            field_dict["value_data"] = value_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_sandbox_event_body_value_data import ValidateSandboxEventBodyValueData

        d = dict(src_dict)
        event_name = d.pop("event_name")

        event_id = d.pop("event_id", UNSET)

        action_source = d.pop("action_source", UNSET)

        _value_data = d.pop("value_data", UNSET)
        value_data: ValidateSandboxEventBodyValueData | Unset
        if isinstance(_value_data, Unset):
            value_data = UNSET
        else:
            value_data = ValidateSandboxEventBodyValueData.from_dict(_value_data)

        validate_sandbox_event_body = cls(
            event_name=event_name,
            event_id=event_id,
            action_source=action_source,
            value_data=value_data,
        )

        validate_sandbox_event_body.additional_properties = d
        return validate_sandbox_event_body

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
