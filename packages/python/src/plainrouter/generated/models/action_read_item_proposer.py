from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_read_item_proposer_type import ActionReadItemProposerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionReadItemProposer")


@_attrs_define
class ActionReadItemProposer:
    """
    Attributes:
        type_ (ActionReadItemProposerType):
        name (str | Unset): PlainRouter for a system proposer; omitted for people and agents.
    """

    type_: ActionReadItemProposerType
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ActionReadItemProposerType(d.pop("type"))

        name = d.pop("name", UNSET)

        action_read_item_proposer = cls(
            type_=type_,
            name=name,
        )

        action_read_item_proposer.additional_properties = d
        return action_read_item_proposer

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
