from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_dry_run_read_dry_run_actions_item_type_0 import ActionDryRunReadDryRunActionsItemType0
    from ..models.action_dry_run_read_dry_run_actions_item_type_1 import ActionDryRunReadDryRunActionsItemType1


T = TypeVar("T", bound="ActionDryRunReadDryRun")


@_attrs_define
class ActionDryRunReadDryRun:
    """
    Attributes:
        actions (list[ActionDryRunReadDryRunActionsItemType0 | ActionDryRunReadDryRunActionsItemType1]):
    """

    actions: list[ActionDryRunReadDryRunActionsItemType0 | ActionDryRunReadDryRunActionsItemType1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_dry_run_read_dry_run_actions_item_type_0 import ActionDryRunReadDryRunActionsItemType0

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, ActionDryRunReadDryRunActionsItemType0):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dry_run_read_dry_run_actions_item_type_0 import ActionDryRunReadDryRunActionsItemType0
        from ..models.action_dry_run_read_dry_run_actions_item_type_1 import ActionDryRunReadDryRunActionsItemType1

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> ActionDryRunReadDryRunActionsItemType0 | ActionDryRunReadDryRunActionsItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = ActionDryRunReadDryRunActionsItemType0.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_1 = ActionDryRunReadDryRunActionsItemType1.from_dict(data)

                return actions_item_type_1

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        action_dry_run_read_dry_run = cls(
            actions=actions,
        )

        action_dry_run_read_dry_run.additional_properties = d
        return action_dry_run_read_dry_run

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
