from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_dry_run_read_dry_run_actions_item_type_1_status import ActionDryRunReadDryRunActionsItemType1Status
from ..models.action_dry_run_read_dry_run_actions_item_type_1_type import ActionDryRunReadDryRunActionsItemType1Type

if TYPE_CHECKING:
    from ..models.action_dry_run_read_dry_run_actions_item_type_1_target_entity import (
        ActionDryRunReadDryRunActionsItemType1TargetEntity,
    )


T = TypeVar("T", bound="ActionDryRunReadDryRunActionsItemType1")


@_attrs_define
class ActionDryRunReadDryRunActionsItemType1:
    """
    Attributes:
        type_ (ActionDryRunReadDryRunActionsItemType1Type):
        target_entity (ActionDryRunReadDryRunActionsItemType1TargetEntity):
        status (ActionDryRunReadDryRunActionsItemType1Status):
        reason (str):
    """

    type_: ActionDryRunReadDryRunActionsItemType1Type
    target_entity: ActionDryRunReadDryRunActionsItemType1TargetEntity
    status: ActionDryRunReadDryRunActionsItemType1Status
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        target_entity = self.target_entity.to_dict()

        status = self.status.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "target_entity": target_entity,
                "status": status,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dry_run_read_dry_run_actions_item_type_1_target_entity import (
            ActionDryRunReadDryRunActionsItemType1TargetEntity,
        )

        d = dict(src_dict)
        type_ = ActionDryRunReadDryRunActionsItemType1Type(d.pop("type"))

        target_entity = ActionDryRunReadDryRunActionsItemType1TargetEntity.from_dict(d.pop("target_entity"))

        status = ActionDryRunReadDryRunActionsItemType1Status(d.pop("status"))

        reason = d.pop("reason")

        action_dry_run_read_dry_run_actions_item_type_1 = cls(
            type_=type_,
            target_entity=target_entity,
            status=status,
            reason=reason,
        )

        action_dry_run_read_dry_run_actions_item_type_1.additional_properties = d
        return action_dry_run_read_dry_run_actions_item_type_1

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
