from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_api_propose_body_evidence_item_source_tool import ActionsApiProposeBodyEvidenceItemSourceTool
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsApiProposeBodyEvidenceItem")


@_attrs_define
class ActionsApiProposeBodyEvidenceItem:
    """
    Attributes:
        source_tool (ActionsApiProposeBodyEvidenceItemSourceTool):
        fields_used (list[str]):
        action_index (int | Unset):
    """

    source_tool: ActionsApiProposeBodyEvidenceItemSourceTool
    fields_used: list[str]
    action_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_tool = self.source_tool.value

        fields_used = self.fields_used

        action_index = self.action_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_tool": source_tool,
                "fields_used": fields_used,
            }
        )
        if action_index is not UNSET:
            field_dict["action_index"] = action_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_tool = ActionsApiProposeBodyEvidenceItemSourceTool(d.pop("source_tool"))

        fields_used = cast(list[str], d.pop("fields_used"))

        action_index = d.pop("action_index", UNSET)

        actions_api_propose_body_evidence_item = cls(
            source_tool=source_tool,
            fields_used=fields_used,
            action_index=action_index,
        )

        actions_api_propose_body_evidence_item.additional_properties = d
        return actions_api_propose_body_evidence_item

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
