from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.launch_intent_read_intent import LaunchIntentReadIntent


T = TypeVar("T", bound="LaunchIntentRead")


@_attrs_define
class LaunchIntentRead:
    """
    Attributes:
        intent (LaunchIntentReadIntent):
    """

    intent: LaunchIntentReadIntent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intent = self.intent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intent": intent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_intent_read_intent import LaunchIntentReadIntent

        d = dict(src_dict)
        intent = LaunchIntentReadIntent.from_dict(d.pop("intent"))

        launch_intent_read = cls(
            intent=intent,
        )

        launch_intent_read.additional_properties = d
        return launch_intent_read

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
