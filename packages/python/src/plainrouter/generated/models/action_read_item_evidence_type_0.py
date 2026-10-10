from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_read_item_evidence_type_0_outcome import ActionReadItemEvidenceType0Outcome


T = TypeVar("T", bound="ActionReadItemEvidenceType0")


@_attrs_define
class ActionReadItemEvidenceType0:
    """
    Attributes:
        original_action_id (str):
        outcome (ActionReadItemEvidenceType0Outcome): Write-once outcome. Management comparisons use PlainRouter counted
            arrivals and Inventory spend. Resume compares the target after the change with the rest of the same account over
            those same days. Pause is not judged. Missing data never yields a verdict. Other action types retain their
            existing payloads.
    """

    original_action_id: str
    outcome: ActionReadItemEvidenceType0Outcome
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_action_id = self.original_action_id

        outcome = self.outcome.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "original_action_id": original_action_id,
                "outcome": outcome,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_read_item_evidence_type_0_outcome import ActionReadItemEvidenceType0Outcome

        d = dict(src_dict)
        original_action_id = d.pop("original_action_id")

        outcome = ActionReadItemEvidenceType0Outcome.from_dict(d.pop("outcome"))

        action_read_item_evidence_type_0 = cls(
            original_action_id=original_action_id,
            outcome=outcome,
        )

        action_read_item_evidence_type_0.additional_properties = d
        return action_read_item_evidence_type_0

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
