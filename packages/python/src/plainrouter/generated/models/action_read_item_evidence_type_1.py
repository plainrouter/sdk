from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionReadItemEvidenceType1")


@_attrs_define
class ActionReadItemEvidenceType1:
    """
    Attributes:
        rule_id (str):
        revision_id (str):
        run_id (str):
        decision_id (str):
    """

    rule_id: str
    revision_id: str
    run_id: str
    decision_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_id = self.rule_id

        revision_id = self.revision_id

        run_id = self.run_id

        decision_id = self.decision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_id": rule_id,
                "revision_id": revision_id,
                "run_id": run_id,
                "decision_id": decision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_id = d.pop("rule_id")

        revision_id = d.pop("revision_id")

        run_id = d.pop("run_id")

        decision_id = d.pop("decision_id")

        action_read_item_evidence_type_1 = cls(
            rule_id=rule_id,
            revision_id=revision_id,
            run_id=run_id,
            decision_id=decision_id,
        )

        action_read_item_evidence_type_1.additional_properties = d
        return action_read_item_evidence_type_1

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
