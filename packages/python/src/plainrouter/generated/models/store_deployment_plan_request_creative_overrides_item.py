from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.store_deployment_plan_request_creative_overrides_item_copy import (
        StoreDeploymentPlanRequestCreativeOverridesItemCopy,
    )


T = TypeVar("T", bound="StoreDeploymentPlanRequestCreativeOverridesItem")


@_attrs_define
class StoreDeploymentPlanRequestCreativeOverridesItem:
    """
    Attributes:
        creative_id (str):
        copy (StoreDeploymentPlanRequestCreativeOverridesItemCopy):
        landing_page (None | str):
    """

    creative_id: str
    copy: StoreDeploymentPlanRequestCreativeOverridesItemCopy
    landing_page: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creative_id = self.creative_id

        copy = self.copy.to_dict()

        landing_page: None | str
        landing_page = self.landing_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creative_id": creative_id,
                "copy": copy,
                "landing_page": landing_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_deployment_plan_request_creative_overrides_item_copy import (
            StoreDeploymentPlanRequestCreativeOverridesItemCopy,
        )

        d = dict(src_dict)
        creative_id = d.pop("creative_id")

        copy = StoreDeploymentPlanRequestCreativeOverridesItemCopy.from_dict(d.pop("copy"))

        def _parse_landing_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        landing_page = _parse_landing_page(d.pop("landing_page"))

        store_deployment_plan_request_creative_overrides_item = cls(
            creative_id=creative_id,
            copy=copy,
            landing_page=landing_page,
        )

        store_deployment_plan_request_creative_overrides_item.additional_properties = d
        return store_deployment_plan_request_creative_overrides_item

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
