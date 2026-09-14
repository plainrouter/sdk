from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingestion_warning_code import IngestionWarningCode

T = TypeVar("T", bound="CreateEventResponse202WarningsItem")


@_attrs_define
class CreateEventResponse202WarningsItem:
    """
    Attributes:
        code (IngestionWarningCode): The closed set of non-rejection warnings returned by authenticated ingestion.
        field (Literal['consent.captured_at']):
        message (str):
    """

    code: IngestionWarningCode
    field: Literal["consent.captured_at"]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "field": field,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = IngestionWarningCode(d.pop("code"))

        field = cast(Literal["consent.captured_at"], d.pop("field"))
        if field != "consent.captured_at":
            raise ValueError(f"field must match const 'consent.captured_at', got '{field}'")

        message = d.pop("message")

        create_event_response_202_warnings_item = cls(
            code=code,
            field=field,
            message=message,
        )

        create_event_response_202_warnings_item.additional_properties = d
        return create_event_response_202_warnings_item

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
