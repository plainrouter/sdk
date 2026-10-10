from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_plan_read_copy_type_0 import DeploymentPlanReadCopyType0
    from ..models.deployment_plan_read_creatives_item import DeploymentPlanReadCreativesItem


T = TypeVar("T", bound="DeploymentPlanRead")


@_attrs_define
class DeploymentPlanRead:
    """
    Attributes:
        id (str):
        platform_ad_account_id (int):
        review_version (str): Current review version. Pass this value when executing the plan you reviewed.
        name (None | str | Unset):
        copy (DeploymentPlanReadCopyType0 | None | Unset):
        landing_page (str | Unset):
        creatives (list[DeploymentPlanReadCreativesItem] | Unset):
    """

    id: str
    platform_ad_account_id: int
    review_version: str
    name: None | str | Unset = UNSET
    copy: DeploymentPlanReadCopyType0 | None | Unset = UNSET
    landing_page: str | Unset = UNSET
    creatives: list[DeploymentPlanReadCreativesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deployment_plan_read_copy_type_0 import DeploymentPlanReadCopyType0

        id = self.id

        platform_ad_account_id = self.platform_ad_account_id

        review_version = self.review_version

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        copy: dict[str, Any] | None | Unset
        if isinstance(self.copy, Unset):
            copy = UNSET
        elif isinstance(self.copy, DeploymentPlanReadCopyType0):
            copy = self.copy.to_dict()
        else:
            copy = self.copy

        landing_page = self.landing_page

        creatives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creatives, Unset):
            creatives = []
            for creatives_item_data in self.creatives:
                creatives_item = creatives_item_data.to_dict()
                creatives.append(creatives_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform_ad_account_id": platform_ad_account_id,
                "review_version": review_version,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if copy is not UNSET:
            field_dict["copy"] = copy
        if landing_page is not UNSET:
            field_dict["landing_page"] = landing_page
        if creatives is not UNSET:
            field_dict["creatives"] = creatives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_plan_read_copy_type_0 import DeploymentPlanReadCopyType0
        from ..models.deployment_plan_read_creatives_item import DeploymentPlanReadCreativesItem

        d = dict(src_dict)
        id = d.pop("id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        review_version = d.pop("review_version")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_copy(data: object) -> DeploymentPlanReadCopyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                copy_type_0 = DeploymentPlanReadCopyType0.from_dict(data)

                return copy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeploymentPlanReadCopyType0 | None | Unset, data)

        copy = _parse_copy(d.pop("copy", UNSET))

        landing_page = d.pop("landing_page", UNSET)

        _creatives = d.pop("creatives", UNSET)
        creatives: list[DeploymentPlanReadCreativesItem] | Unset = UNSET
        if _creatives is not UNSET:
            creatives = []
            for creatives_item_data in _creatives:
                creatives_item = DeploymentPlanReadCreativesItem.from_dict(creatives_item_data)

                creatives.append(creatives_item)

        deployment_plan_read = cls(
            id=id,
            platform_ad_account_id=platform_ad_account_id,
            review_version=review_version,
            name=name,
            copy=copy,
            landing_page=landing_page,
            creatives=creatives,
        )

        deployment_plan_read.additional_properties = d
        return deployment_plan_read

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
