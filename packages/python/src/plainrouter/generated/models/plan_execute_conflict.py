from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan_execute_conflict_error import PlanExecuteConflictError


T = TypeVar("T", bound="PlanExecuteConflict")


@_attrs_define
class PlanExecuteConflict:
    """
    Attributes:
        error (PlanExecuteConflictError):
    """

    error: PlanExecuteConflictError
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_execute_conflict_error import PlanExecuteConflictError

        d = dict(src_dict)
        error = PlanExecuteConflictError.from_dict(d.pop("error"))

        plan_execute_conflict = cls(
            error=error,
        )

        plan_execute_conflict.additional_properties = d
        return plan_execute_conflict

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
