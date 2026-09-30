from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.action_proposal_input_evidence_item_source_tool import ActionProposalInputEvidenceItemSourceTool
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionProposalInputEvidenceItem")


@_attrs_define
class ActionProposalInputEvidenceItem:
    """
    Attributes:
        source_tool (ActionProposalInputEvidenceItemSourceTool):
        fields_used (list[str]):
        action_index (int | Unset):
    """

    source_tool: ActionProposalInputEvidenceItemSourceTool
    fields_used: list[str]
    action_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_tool = self.source_tool.value

        fields_used = self.fields_used

        action_index = self.action_index

        field_dict: dict[str, Any] = {}

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
        source_tool = ActionProposalInputEvidenceItemSourceTool(d.pop("source_tool"))

        fields_used = cast(list[str], d.pop("fields_used"))

        action_index = d.pop("action_index", UNSET)

        action_proposal_input_evidence_item = cls(
            source_tool=source_tool,
            fields_used=fields_used,
            action_index=action_index,
        )

        return action_proposal_input_evidence_item
