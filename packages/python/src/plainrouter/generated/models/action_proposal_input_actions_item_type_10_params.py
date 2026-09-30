from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_proposal_input_actions_item_type_10_params_asset_type import (
    ActionProposalInputActionsItemType10ParamsAssetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionProposalInputActionsItemType10Params")


@_attrs_define
class ActionProposalInputActionsItemType10Params:
    """
    Attributes:
        staged_asset_id (str):
        asset_type (ActionProposalInputActionsItemType10ParamsAssetType):
        filename (str):
        content_sha256 (str):
        mime_type (None | str | Unset):
        size_bytes (int | None | Unset):
    """

    staged_asset_id: str
    asset_type: ActionProposalInputActionsItemType10ParamsAssetType
    filename: str
    content_sha256: str
    mime_type: None | str | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        staged_asset_id = self.staged_asset_id

        asset_type = self.asset_type.value

        filename = self.filename

        content_sha256 = self.content_sha256

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staged_asset_id": staged_asset_id,
                "asset_type": asset_type,
                "filename": filename,
                "content_sha256": content_sha256,
            }
        )
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        staged_asset_id = d.pop("staged_asset_id")

        asset_type = ActionProposalInputActionsItemType10ParamsAssetType(d.pop("asset_type"))

        filename = d.pop("filename")

        content_sha256 = d.pop("content_sha256")

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mime_type", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes", UNSET))

        action_proposal_input_actions_item_type_10_params = cls(
            staged_asset_id=staged_asset_id,
            asset_type=asset_type,
            filename=filename,
            content_sha256=content_sha256,
            mime_type=mime_type,
            size_bytes=size_bytes,
        )

        action_proposal_input_actions_item_type_10_params.additional_properties = d
        return action_proposal_input_actions_item_type_10_params

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
