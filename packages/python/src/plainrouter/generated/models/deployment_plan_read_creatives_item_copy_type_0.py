from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_plan_read_creatives_item_copy_type_0_cta import DeploymentPlanReadCreativesItemCopyType0Cta

T = TypeVar("T", bound="DeploymentPlanReadCreativesItemCopyType0")


@_attrs_define
class DeploymentPlanReadCreativesItemCopyType0:
    """Optional complete per-ad copy override; null uses the plan copy.

    Attributes:
        primary_text (str):
        headline (str):
        description (str):
        cta (DeploymentPlanReadCreativesItemCopyType0Cta):
    """

    primary_text: str
    headline: str
    description: str
    cta: DeploymentPlanReadCreativesItemCopyType0Cta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_text = self.primary_text

        headline = self.headline

        description = self.description

        cta = self.cta.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primary_text": primary_text,
                "headline": headline,
                "description": description,
                "cta": cta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        primary_text = d.pop("primary_text")

        headline = d.pop("headline")

        description = d.pop("description")

        cta = DeploymentPlanReadCreativesItemCopyType0Cta(d.pop("cta"))

        deployment_plan_read_creatives_item_copy_type_0 = cls(
            primary_text=primary_text,
            headline=headline,
            description=description,
            cta=cta,
        )

        deployment_plan_read_creatives_item_copy_type_0.additional_properties = d
        return deployment_plan_read_creatives_item_copy_type_0

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
