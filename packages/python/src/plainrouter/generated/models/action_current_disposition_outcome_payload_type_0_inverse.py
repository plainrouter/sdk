from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_current_disposition_outcome_payload_type_0_inverse_status import (
    ActionCurrentDispositionOutcomePayloadType0InverseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionCurrentDispositionOutcomePayloadType0Inverse")


@_attrs_define
class ActionCurrentDispositionOutcomePayloadType0Inverse:
    """
    Attributes:
        status (ActionCurrentDispositionOutcomePayloadType0InverseStatus):
        batch_id (str | Unset):
        reason_code (str | Unset):
    """

    status: ActionCurrentDispositionOutcomePayloadType0InverseStatus
    batch_id: str | Unset = UNSET
    reason_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        batch_id = self.batch_id

        reason_code = self.reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ActionCurrentDispositionOutcomePayloadType0InverseStatus(d.pop("status"))

        batch_id = d.pop("batch_id", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        action_current_disposition_outcome_payload_type_0_inverse = cls(
            status=status,
            batch_id=batch_id,
            reason_code=reason_code,
        )

        action_current_disposition_outcome_payload_type_0_inverse.additional_properties = d
        return action_current_disposition_outcome_payload_type_0_inverse

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
