from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plan_copy_read_plan_status import PlanCopyReadPlanStatus

T = TypeVar("T", bound="PlanCopyReadPlan")


@_attrs_define
class PlanCopyReadPlan:
    """
    Attributes:
        id (str):
        platform_ad_account_id (int):
        status (PlanCopyReadPlanStatus):
        budget_amount_minor (int):
        validation_result (None):
        validated_at (None):
        approval_id (None):
    """

    id: str
    platform_ad_account_id: int
    status: PlanCopyReadPlanStatus
    budget_amount_minor: int
    validation_result: None
    validated_at: None
    approval_id: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform_ad_account_id = self.platform_ad_account_id

        status = self.status.value

        budget_amount_minor = self.budget_amount_minor

        validation_result = self.validation_result

        validated_at = self.validated_at

        approval_id = self.approval_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform_ad_account_id": platform_ad_account_id,
                "status": status,
                "budget_amount_minor": budget_amount_minor,
                "validation_result": validation_result,
                "validated_at": validated_at,
                "approval_id": approval_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        status = PlanCopyReadPlanStatus(d.pop("status"))

        budget_amount_minor = d.pop("budget_amount_minor")

        validation_result = d.pop("validation_result")

        validated_at = d.pop("validated_at")

        approval_id = d.pop("approval_id")

        plan_copy_read_plan = cls(
            id=id,
            platform_ad_account_id=platform_ad_account_id,
            status=status,
            budget_amount_minor=budget_amount_minor,
            validation_result=validation_result,
            validated_at=validated_at,
            approval_id=approval_id,
        )

        plan_copy_read_plan.additional_properties = d
        return plan_copy_read_plan

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
