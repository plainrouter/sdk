from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LauncherFileImportResponse422Type1SyntacticRowFailuresItem")


@_attrs_define
class LauncherFileImportResponse422Type1SyntacticRowFailuresItem:
    """
    Attributes:
        import_row_number (int):
        reason_code (str):
    """

    import_row_number: int
    reason_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_row_number = self.import_row_number

        reason_code = self.reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_row_number": import_row_number,
                "reason_code": reason_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        import_row_number = d.pop("import_row_number")

        reason_code = d.pop("reason_code")

        launcher_file_import_response_422_type_1_syntactic_row_failures_item = cls(
            import_row_number=import_row_number,
            reason_code=reason_code,
        )

        launcher_file_import_response_422_type_1_syntactic_row_failures_item.additional_properties = d
        return launcher_file_import_response_422_type_1_syntactic_row_failures_item

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
