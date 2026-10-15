from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deployment_plan_read import DeploymentPlanRead


T = TypeVar("T", bound="LaunchPlansValidateResponse200")


@_attrs_define
class LaunchPlansValidateResponse200:
    """
    Attributes:
        plan (DeploymentPlanRead): Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP
            representations. Defaults are bounded. Follow next_cursor with the same scope and filters. One oversized row is
            explicitly refused; fields are never silently clipped.
    """

    plan: DeploymentPlanRead
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
        from ..models.deployment_plan_read import DeploymentPlanRead

        d = dict(src_dict)
        plan = DeploymentPlanRead.from_dict(d.pop("plan"))

        launch_plans_validate_response_200 = cls(
            plan=plan,
        )

        launch_plans_validate_response_200.additional_properties = d
        return launch_plans_validate_response_200

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
