from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposal_replay_conflict_message import ProposalReplayConflictMessage

if TYPE_CHECKING:
    from ..models.proposal_replay_conflict_errors import ProposalReplayConflictErrors


T = TypeVar("T", bound="ProposalReplayConflict")


@_attrs_define
class ProposalReplayConflict:
    """
    Attributes:
        message (ProposalReplayConflictMessage):
        errors (ProposalReplayConflictErrors):
    """

    message: ProposalReplayConflictMessage
    errors: ProposalReplayConflictErrors
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message.value

        errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_replay_conflict_errors import ProposalReplayConflictErrors

        d = dict(src_dict)
        message = ProposalReplayConflictMessage(d.pop("message"))

        errors = ProposalReplayConflictErrors.from_dict(d.pop("errors"))

        proposal_replay_conflict = cls(
            message=message,
            errors=errors,
        )

        proposal_replay_conflict.additional_properties = d
        return proposal_replay_conflict

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
