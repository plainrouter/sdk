from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActionReadItemEvidenceType2")


@_attrs_define
class ActionReadItemEvidenceType2:
    """System evidence from a completed Test cites its Test, verdict and selected winner member.

    Attributes:
        test_id (str):
        verdict_id (str):
        winner_member_id (str):
    """

    test_id: str
    verdict_id: str
    winner_member_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_id = self.test_id

        verdict_id = self.verdict_id

        winner_member_id = self.winner_member_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_id": test_id,
                "verdict_id": verdict_id,
                "winner_member_id": winner_member_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_id = d.pop("test_id")

        verdict_id = d.pop("verdict_id")

        winner_member_id = d.pop("winner_member_id")

        action_read_item_evidence_type_2 = cls(
            test_id=test_id,
            verdict_id=verdict_id,
            winner_member_id=winner_member_id,
        )

        action_read_item_evidence_type_2.additional_properties = d
        return action_read_item_evidence_type_2

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
