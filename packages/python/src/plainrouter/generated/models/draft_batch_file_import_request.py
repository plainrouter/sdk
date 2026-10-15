from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.draft_batch_mode import DraftBatchMode
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="DraftBatchFileImportRequest")


@_attrs_define
class DraftBatchFileImportRequest:
    """
    Attributes:
        file (File):
        source_adset_id (str):
        source_ad_id (str):
        mode (DraftBatchMode):
        folder_to_adset (bool | Unset):
        grouping_enabled (bool | Unset):
        account_id (int | Unset):
        workspace_id (int | Unset):
    """

    file: File
    source_adset_id: str
    source_ad_id: str
    mode: DraftBatchMode
    folder_to_adset: bool | Unset = UNSET
    grouping_enabled: bool | Unset = UNSET
    account_id: int | Unset = UNSET
    workspace_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        source_adset_id = self.source_adset_id

        source_ad_id = self.source_ad_id

        mode = self.mode.value

        folder_to_adset = self.folder_to_adset

        grouping_enabled = self.grouping_enabled

        account_id = self.account_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "source_adset_id": source_adset_id,
                "source_ad_id": source_ad_id,
                "mode": mode,
            }
        )
        if folder_to_adset is not UNSET:
            field_dict["folder_to_adset"] = folder_to_adset
        if grouping_enabled is not UNSET:
            field_dict["grouping_enabled"] = grouping_enabled
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("source_adset_id", (None, str(self.source_adset_id).encode(), "text/plain")))

        files.append(("source_ad_id", (None, str(self.source_ad_id).encode(), "text/plain")))

        files.append(("mode", (None, str(self.mode.value).encode(), "text/plain")))

        if not isinstance(self.folder_to_adset, Unset):
            files.append(("folder_to_adset", (None, str(self.folder_to_adset).encode(), "text/plain")))

        if not isinstance(self.grouping_enabled, Unset):
            files.append(("grouping_enabled", (None, str(self.grouping_enabled).encode(), "text/plain")))

        if not isinstance(self.account_id, Unset):
            files.append(("account_id", (None, str(self.account_id).encode(), "text/plain")))

        if not isinstance(self.workspace_id, Unset):
            files.append(("workspace_id", (None, str(self.workspace_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        source_adset_id = d.pop("source_adset_id")

        source_ad_id = d.pop("source_ad_id")

        mode = DraftBatchMode(d.pop("mode"))

        folder_to_adset = d.pop("folder_to_adset", UNSET)

        grouping_enabled = d.pop("grouping_enabled", UNSET)

        account_id = d.pop("account_id", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        draft_batch_file_import_request = cls(
            file=file,
            source_adset_id=source_adset_id,
            source_ad_id=source_ad_id,
            mode=mode,
            folder_to_adset=folder_to_adset,
            grouping_enabled=grouping_enabled,
            account_id=account_id,
            workspace_id=workspace_id,
        )

        draft_batch_file_import_request.additional_properties = d
        return draft_batch_file_import_request

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
