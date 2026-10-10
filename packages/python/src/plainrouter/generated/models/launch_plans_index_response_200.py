from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.launch_plans_index_response_200_plans import LaunchPlansIndexResponse200Plans


T = TypeVar("T", bound="LaunchPlansIndexResponse200")


@_attrs_define
class LaunchPlansIndexResponse200:
    """
    Attributes:
        plans (LaunchPlansIndexResponse200Plans):
    """

    plans: LaunchPlansIndexResponse200Plans
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plans = self.plans.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plans": plans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_plans_index_response_200_plans import LaunchPlansIndexResponse200Plans

        d = dict(src_dict)
        plans = LaunchPlansIndexResponse200Plans.from_dict(d.pop("plans"))

        launch_plans_index_response_200 = cls(
            plans=plans,
        )

        launch_plans_index_response_200.additional_properties = d
        return launch_plans_index_response_200

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
