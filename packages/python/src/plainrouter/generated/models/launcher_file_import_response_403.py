from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LauncherFileImportResponse403")


@_attrs_define
class LauncherFileImportResponse403:
    """
    Attributes:
        error (Literal['insufficient_scope']):
        error_description (Literal['File import requires at least the workspace write execution tier.']):
    """

    error: Literal["insufficient_scope"]
    error_description: Literal["File import requires at least the workspace write execution tier."]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_description = self.error_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "error_description": error_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = cast(Literal["insufficient_scope"], d.pop("error"))
        if error != "insufficient_scope":
            raise ValueError(f"error must match const 'insufficient_scope', got '{error}'")

        error_description = cast(
            Literal["File import requires at least the workspace write execution tier."], d.pop("error_description")
        )
        if error_description != "File import requires at least the workspace write execution tier.":
            raise ValueError(
                f"error_description must match const 'File import requires at least the workspace write execution tier.', got '{error_description}'"
            )

        launcher_file_import_response_403 = cls(
            error=error,
            error_description=error_description,
        )

        launcher_file_import_response_403.additional_properties = d
        return launcher_file_import_response_403

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
