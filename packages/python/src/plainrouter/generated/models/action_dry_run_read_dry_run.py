from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_dry_run_read_dry_run_actions_item_type_0 import ActionDryRunReadDryRunActionsItemType0
    from ..models.action_dry_run_read_dry_run_actions_item_type_1 import ActionDryRunReadDryRunActionsItemType1


T = TypeVar("T", bound="ActionDryRunReadDryRun")


@_attrs_define
class ActionDryRunReadDryRun:
    """Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP representations. Defaults are
    bounded. Follow next_cursor with the same scope and filters. One oversized row is explicitly refused; fields are
    never silently clipped.

        Attributes:
            actions (list[ActionDryRunReadDryRunActionsItemType0 | ActionDryRunReadDryRunActionsItemType1]):
            next_cursor (int | None | Unset):
            truncated (bool | Unset):
            continuation (str | Unset):
            total (int | Unset):
    """

    actions: list[ActionDryRunReadDryRunActionsItemType0 | ActionDryRunReadDryRunActionsItemType1]
    next_cursor: int | None | Unset = UNSET
    truncated: bool | Unset = UNSET
    continuation: str | Unset = UNSET
    total: int | Unset = UNSET
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

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        truncated = self.truncated

        continuation = self.continuation

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if continuation is not UNSET:
            field_dict["continuation"] = continuation
        if total is not UNSET:
            field_dict["total"] = total

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

        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        truncated = d.pop("truncated", UNSET)

        continuation = d.pop("continuation", UNSET)

        total = d.pop("total", UNSET)

        action_dry_run_read_dry_run = cls(
            actions=actions,
            next_cursor=next_cursor,
            truncated=truncated,
            continuation=continuation,
            total=total,
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
