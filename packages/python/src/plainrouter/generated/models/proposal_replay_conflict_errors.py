from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposal_replay_conflict_errors_idempotency_key_item import ProposalReplayConflictErrorsIdempotencyKeyItem

T = TypeVar("T", bound="ProposalReplayConflictErrors")


@_attrs_define
class ProposalReplayConflictErrors:
    """
    Attributes:
        idempotency_key (list[ProposalReplayConflictErrorsIdempotencyKeyItem]):
    """

    idempotency_key: list[ProposalReplayConflictErrorsIdempotencyKeyItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = []
        for idempotency_key_item_data in self.idempotency_key:
            idempotency_key_item = idempotency_key_item_data.value
            idempotency_key.append(idempotency_key_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idempotency_key = []
        _idempotency_key = d.pop("idempotency_key")
        for idempotency_key_item_data in _idempotency_key:
            idempotency_key_item = ProposalReplayConflictErrorsIdempotencyKeyItem(idempotency_key_item_data)

            idempotency_key.append(idempotency_key_item)

        proposal_replay_conflict_errors = cls(
            idempotency_key=idempotency_key,
        )

        proposal_replay_conflict_errors.additional_properties = d
        return proposal_replay_conflict_errors

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
