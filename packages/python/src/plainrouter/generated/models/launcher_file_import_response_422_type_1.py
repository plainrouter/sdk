from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.launcher_file_import_response_422_type_1_error import LauncherFileImportResponse422Type1Error

if TYPE_CHECKING:
    from ..models.launcher_file_import_response_422_type_1_syntactic_row_failures_item import (
        LauncherFileImportResponse422Type1SyntacticRowFailuresItem,
    )


T = TypeVar("T", bound="LauncherFileImportResponse422Type1")


@_attrs_define
class LauncherFileImportResponse422Type1:
    """
    Attributes:
        error (LauncherFileImportResponse422Type1Error):
        reason_code (str):
        syntactic_row_failures (list[LauncherFileImportResponse422Type1SyntacticRowFailuresItem]):
    """

    error: LauncherFileImportResponse422Type1Error
    reason_code: str
    syntactic_row_failures: list[LauncherFileImportResponse422Type1SyntacticRowFailuresItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        reason_code = self.reason_code

        syntactic_row_failures = []
        for syntactic_row_failures_item_data in self.syntactic_row_failures:
            syntactic_row_failures_item = syntactic_row_failures_item_data.to_dict()
            syntactic_row_failures.append(syntactic_row_failures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "reason_code": reason_code,
                "syntactic_row_failures": syntactic_row_failures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launcher_file_import_response_422_type_1_syntactic_row_failures_item import (
            LauncherFileImportResponse422Type1SyntacticRowFailuresItem,
        )

        d = dict(src_dict)
        error = LauncherFileImportResponse422Type1Error(d.pop("error"))

        reason_code = d.pop("reason_code")

        syntactic_row_failures = []
        _syntactic_row_failures = d.pop("syntactic_row_failures")
        for syntactic_row_failures_item_data in _syntactic_row_failures:
            syntactic_row_failures_item = LauncherFileImportResponse422Type1SyntacticRowFailuresItem.from_dict(
                syntactic_row_failures_item_data
            )

            syntactic_row_failures.append(syntactic_row_failures_item)

        launcher_file_import_response_422_type_1 = cls(
            error=error,
            reason_code=reason_code,
            syntactic_row_failures=syntactic_row_failures,
        )

        launcher_file_import_response_422_type_1.additional_properties = d
        return launcher_file_import_response_422_type_1

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
