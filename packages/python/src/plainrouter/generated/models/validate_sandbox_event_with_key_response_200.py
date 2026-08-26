from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidateSandboxEventWithKeyResponse200")


@_attrs_define
class ValidateSandboxEventWithKeyResponse200:
    """
    Attributes:
        sandbox (bool):
        accepted (bool):
        event_id (str):
        status (str):
        persisted (bool):
        provider_delivery (bool):
        message (str):
    """

    sandbox: bool
    accepted: bool
    event_id: str
    status: str
    persisted: bool
    provider_delivery: bool
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox = self.sandbox

        accepted = self.accepted

        event_id = self.event_id

        status = self.status

        persisted = self.persisted

        provider_delivery = self.provider_delivery

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox": sandbox,
                "accepted": accepted,
                "event_id": event_id,
                "status": status,
                "persisted": persisted,
                "provider_delivery": provider_delivery,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox = d.pop("sandbox")

        accepted = d.pop("accepted")

        event_id = d.pop("event_id")

        status = d.pop("status")

        persisted = d.pop("persisted")

        provider_delivery = d.pop("provider_delivery")

        message = d.pop("message")

        validate_sandbox_event_with_key_response_200 = cls(
            sandbox=sandbox,
            accepted=accepted,
            event_id=event_id,
            status=status,
            persisted=persisted,
            provider_delivery=provider_delivery,
            message=message,
        )

        validate_sandbox_event_with_key_response_200.additional_properties = d
        return validate_sandbox_event_with_key_response_200

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
