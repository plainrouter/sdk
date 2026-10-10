from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteDeploymentPlanRequest")


@_attrs_define
class ExecuteDeploymentPlanRequest:
    """
    Attributes:
        review_version (str):
        intent_key (None | str | Unset):
    """

    review_version: str
    intent_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        review_version = self.review_version

        intent_key: None | str | Unset
        if isinstance(self.intent_key, Unset):
            intent_key = UNSET
        else:
            intent_key = self.intent_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "review_version": review_version,
            }
        )
        if intent_key is not UNSET:
            field_dict["intent_key"] = intent_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        review_version = d.pop("review_version")

        def _parse_intent_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intent_key = _parse_intent_key(d.pop("intent_key", UNSET))

        execute_deployment_plan_request = cls(
            review_version=review_version,
            intent_key=intent_key,
        )

        execute_deployment_plan_request.additional_properties = d
        return execute_deployment_plan_request

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
