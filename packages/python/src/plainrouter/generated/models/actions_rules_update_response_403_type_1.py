from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_rules_update_response_403_type_1_error import ActionsRulesUpdateResponse403Type1Error

T = TypeVar("T", bound="ActionsRulesUpdateResponse403Type1")


@_attrs_define
class ActionsRulesUpdateResponse403Type1:
    """
    Attributes:
        error (ActionsRulesUpdateResponse403Type1Error):
        error_description (str):
    """

    error: ActionsRulesUpdateResponse403Type1Error
    error_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

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
        error = ActionsRulesUpdateResponse403Type1Error(d.pop("error"))

        error_description = d.pop("error_description")

        actions_rules_update_response_403_type_1 = cls(
            error=error,
            error_description=error_description,
        )

        actions_rules_update_response_403_type_1.additional_properties = d
        return actions_rules_update_response_403_type_1

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
