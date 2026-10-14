from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deployment_plan_read import DeploymentPlanRead
    from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_0 import (
        LaunchPlansIndexResponse200PlansNextPageArgumentsType0,
    )
    from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_1 import (
        LaunchPlansIndexResponse200PlansNextPageArgumentsType1,
    )


T = TypeVar("T", bound="LaunchPlansIndexResponse200Plans")


@_attrs_define
class LaunchPlansIndexResponse200Plans:
    """
    Attributes:
        data (list[DeploymentPlanRead]):
        current_page (int):
        per_page (int):
        total (int):
        last_page (int):
        next_cursor (int | None): Always present. The next row offset, or null when the list is complete.
        truncated (bool):
        next_page_arguments (LaunchPlansIndexResponse200PlansNextPageArgumentsType0 |
            LaunchPlansIndexResponse200PlansNextPageArgumentsType1 | None): Always present. Page and per_page for aligned
            offsets, cursor and per_page after a byte-limited page, or null when complete.
        continuation (str):
    """

    data: list[DeploymentPlanRead]
    current_page: int
    per_page: int
    total: int
    last_page: int
    next_cursor: int | None
    truncated: bool
    next_page_arguments: (
        LaunchPlansIndexResponse200PlansNextPageArgumentsType0
        | LaunchPlansIndexResponse200PlansNextPageArgumentsType1
        | None
    )
    continuation: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_0 import (
            LaunchPlansIndexResponse200PlansNextPageArgumentsType0,
        )
        from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_1 import (
            LaunchPlansIndexResponse200PlansNextPageArgumentsType1,
        )

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        current_page = self.current_page

        per_page = self.per_page

        total = self.total

        last_page = self.last_page

        next_cursor: int | None
        next_cursor = self.next_cursor

        truncated = self.truncated

        next_page_arguments: dict[str, Any] | None
        if isinstance(self.next_page_arguments, LaunchPlansIndexResponse200PlansNextPageArgumentsType0):
            next_page_arguments = self.next_page_arguments.to_dict()
        elif isinstance(self.next_page_arguments, LaunchPlansIndexResponse200PlansNextPageArgumentsType1):
            next_page_arguments = self.next_page_arguments.to_dict()
        else:
            next_page_arguments = self.next_page_arguments

        continuation = self.continuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "current_page": current_page,
                "per_page": per_page,
                "total": total,
                "last_page": last_page,
                "next_cursor": next_cursor,
                "truncated": truncated,
                "next_page_arguments": next_page_arguments,
                "continuation": continuation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_plan_read import DeploymentPlanRead
        from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_0 import (
            LaunchPlansIndexResponse200PlansNextPageArgumentsType0,
        )
        from ..models.launch_plans_index_response_200_plans_next_page_arguments_type_1 import (
            LaunchPlansIndexResponse200PlansNextPageArgumentsType1,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = DeploymentPlanRead.from_dict(data_item_data)

            data.append(data_item)

        current_page = d.pop("current_page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        last_page = d.pop("last_page")

        def _parse_next_cursor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        truncated = d.pop("truncated")

        def _parse_next_page_arguments(
            data: object,
        ) -> (
            LaunchPlansIndexResponse200PlansNextPageArgumentsType0
            | LaunchPlansIndexResponse200PlansNextPageArgumentsType1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_page_arguments_type_0 = LaunchPlansIndexResponse200PlansNextPageArgumentsType0.from_dict(data)

                return next_page_arguments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_page_arguments_type_1 = LaunchPlansIndexResponse200PlansNextPageArgumentsType1.from_dict(data)

                return next_page_arguments_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LaunchPlansIndexResponse200PlansNextPageArgumentsType0
                | LaunchPlansIndexResponse200PlansNextPageArgumentsType1
                | None,
                data,
            )

        next_page_arguments = _parse_next_page_arguments(d.pop("next_page_arguments"))

        continuation = d.pop("continuation")

        launch_plans_index_response_200_plans = cls(
            data=data,
            current_page=current_page,
            per_page=per_page,
            total=total,
            last_page=last_page,
            next_cursor=next_cursor,
            truncated=truncated,
            next_page_arguments=next_page_arguments,
            continuation=continuation,
        )

        launch_plans_index_response_200_plans.additional_properties = d
        return launch_plans_index_response_200_plans

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
