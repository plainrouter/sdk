from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.action_proposal_input_actions_item_type_13_params_status import (
    ActionProposalInputActionsItemType13ParamsStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionProposalInputActionsItemType13Params")


@_attrs_define
class ActionProposalInputActionsItemType13Params:
    """
    Attributes:
        asset_id (str):
        status (ActionProposalInputActionsItemType13ParamsStatus):
        name_suffix (None | str | Unset):
    """

    asset_id: str
    status: ActionProposalInputActionsItemType13ParamsStatus
    name_suffix: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        status = self.status.value

        name_suffix: None | str | Unset
        if isinstance(self.name_suffix, Unset):
            name_suffix = UNSET
        else:
            name_suffix = self.name_suffix

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asset_id": asset_id,
                "status": status,
            }
        )
        if name_suffix is not UNSET:
            field_dict["name_suffix"] = name_suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        status = ActionProposalInputActionsItemType13ParamsStatus(d.pop("status"))

        def _parse_name_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_suffix = _parse_name_suffix(d.pop("name_suffix", UNSET))

        action_proposal_input_actions_item_type_13_params = cls(
            asset_id=asset_id,
            status=status,
            name_suffix=name_suffix,
        )

        return action_proposal_input_actions_item_type_13_params
