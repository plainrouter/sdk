from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan_copy_read_plan import PlanCopyReadPlan


T = TypeVar("T", bound="PlanCopyRead")


@_attrs_define
class PlanCopyRead:
    """
    Attributes:
        plan (PlanCopyReadPlan):
    """

    plan: PlanCopyReadPlan
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_copy_read_plan import PlanCopyReadPlan

        d = dict(src_dict)
        plan = PlanCopyReadPlan.from_dict(d.pop("plan"))

        plan_copy_read = cls(
            plan=plan,
        )

        plan_copy_read.additional_properties = d
        return plan_copy_read

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
