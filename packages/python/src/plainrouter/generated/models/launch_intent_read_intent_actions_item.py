from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.launch_intent_read_intent_actions_item_type import LaunchIntentReadIntentActionsItemType

T = TypeVar("T", bound="LaunchIntentReadIntentActionsItem")


@_attrs_define
class LaunchIntentReadIntentActionsItem:
    """
    Attributes:
        id (str):
        type_ (LaunchIntentReadIntentActionsItemType):
        verification_result (None | str):
        external_ids (Any):
    """

    id: str
    type_: LaunchIntentReadIntentActionsItemType
    verification_result: None | str
    external_ids: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        verification_result: None | str
        verification_result = self.verification_result

        external_ids = self.external_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "verification_result": verification_result,
                "external_ids": external_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = LaunchIntentReadIntentActionsItemType(d.pop("type"))

        def _parse_verification_result(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verification_result = _parse_verification_result(d.pop("verification_result"))

        external_ids = d.pop("external_ids")

        launch_intent_read_intent_actions_item = cls(
            id=id,
            type_=type_,
            verification_result=verification_result,
            external_ids=external_ids,
        )

        launch_intent_read_intent_actions_item.additional_properties = d
        return launch_intent_read_intent_actions_item

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
