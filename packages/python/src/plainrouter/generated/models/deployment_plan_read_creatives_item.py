from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deployment_plan_read_creatives_item_copy_type_0 import DeploymentPlanReadCreativesItemCopyType0
    from ..models.deployment_plan_read_creatives_item_resolved_copy_type_0 import (
        DeploymentPlanReadCreativesItemResolvedCopyType0,
    )


T = TypeVar("T", bound="DeploymentPlanReadCreativesItem")


@_attrs_define
class DeploymentPlanReadCreativesItem:
    """
    Attributes:
        id (str):
        position (int):
        copy (DeploymentPlanReadCreativesItemCopyType0 | None): Optional complete per-ad copy override; null uses the
            plan copy.
        landing_page (None | str): Optional per-ad HTTPS landing URL override; null uses the plan landing URL.
        resolved_copy (DeploymentPlanReadCreativesItemResolvedCopyType0 | None):
        resolved_landing_page (str):
        copy_differs (bool):
        landing_page_differs (bool):
    """

    id: str
    position: int
    copy: DeploymentPlanReadCreativesItemCopyType0 | None
    landing_page: None | str
    resolved_copy: DeploymentPlanReadCreativesItemResolvedCopyType0 | None
    resolved_landing_page: str
    copy_differs: bool
    landing_page_differs: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deployment_plan_read_creatives_item_copy_type_0 import DeploymentPlanReadCreativesItemCopyType0
        from ..models.deployment_plan_read_creatives_item_resolved_copy_type_0 import (
            DeploymentPlanReadCreativesItemResolvedCopyType0,
        )

        id = self.id

        position = self.position

        copy: dict[str, Any] | None
        if isinstance(self.copy, DeploymentPlanReadCreativesItemCopyType0):
            copy = self.copy.to_dict()
        else:
            copy = self.copy

        landing_page: None | str
        landing_page = self.landing_page

        resolved_copy: dict[str, Any] | None
        if isinstance(self.resolved_copy, DeploymentPlanReadCreativesItemResolvedCopyType0):
            resolved_copy = self.resolved_copy.to_dict()
        else:
            resolved_copy = self.resolved_copy

        resolved_landing_page = self.resolved_landing_page

        copy_differs = self.copy_differs

        landing_page_differs = self.landing_page_differs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "copy": copy,
                "landing_page": landing_page,
                "resolved_copy": resolved_copy,
                "resolved_landing_page": resolved_landing_page,
                "copy_differs": copy_differs,
                "landing_page_differs": landing_page_differs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_plan_read_creatives_item_copy_type_0 import DeploymentPlanReadCreativesItemCopyType0
        from ..models.deployment_plan_read_creatives_item_resolved_copy_type_0 import (
            DeploymentPlanReadCreativesItemResolvedCopyType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        position = d.pop("position")

        def _parse_copy(data: object) -> DeploymentPlanReadCreativesItemCopyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                copy_type_0 = DeploymentPlanReadCreativesItemCopyType0.from_dict(data)

                return copy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeploymentPlanReadCreativesItemCopyType0 | None, data)

        copy = _parse_copy(d.pop("copy"))

        def _parse_landing_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        landing_page = _parse_landing_page(d.pop("landing_page"))

        def _parse_resolved_copy(data: object) -> DeploymentPlanReadCreativesItemResolvedCopyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_copy_type_0 = DeploymentPlanReadCreativesItemResolvedCopyType0.from_dict(data)

                return resolved_copy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeploymentPlanReadCreativesItemResolvedCopyType0 | None, data)

        resolved_copy = _parse_resolved_copy(d.pop("resolved_copy"))

        resolved_landing_page = d.pop("resolved_landing_page")

        copy_differs = d.pop("copy_differs")

        landing_page_differs = d.pop("landing_page_differs")

        deployment_plan_read_creatives_item = cls(
            id=id,
            position=position,
            copy=copy,
            landing_page=landing_page,
            resolved_copy=resolved_copy,
            resolved_landing_page=resolved_landing_page,
            copy_differs=copy_differs,
            landing_page_differs=landing_page_differs,
        )

        deployment_plan_read_creatives_item.additional_properties = d
        return deployment_plan_read_creatives_item

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
