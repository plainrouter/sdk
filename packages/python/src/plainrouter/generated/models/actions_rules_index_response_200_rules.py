from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actions_rules_index_response_200_rules_data_item import ActionsRulesIndexResponse200RulesDataItem


T = TypeVar("T", bound="ActionsRulesIndexResponse200Rules")


@_attrs_define
class ActionsRulesIndexResponse200Rules:
    """Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP representations. Defaults are
    bounded. Follow next_cursor with the same scope and filters. One oversized row is explicitly refused; fields are
    never silently clipped.

        Attributes:
            data (list[ActionsRulesIndexResponse200RulesDataItem] | Unset):
            total (int | Unset):
            per_page (int | Unset):
            next_cursor (None | str | Unset):
            truncated (bool | Unset):
            continuation (str | Unset):
    """

    data: list[ActionsRulesIndexResponse200RulesDataItem] | Unset = UNSET
    total: int | Unset = UNSET
    per_page: int | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    truncated: bool | Unset = UNSET
    continuation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total = self.total

        per_page = self.per_page

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        truncated = self.truncated

        continuation = self.continuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if continuation is not UNSET:
            field_dict["continuation"] = continuation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actions_rules_index_response_200_rules_data_item import ActionsRulesIndexResponse200RulesDataItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ActionsRulesIndexResponse200RulesDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ActionsRulesIndexResponse200RulesDataItem.from_dict(data_item_data)

                data.append(data_item)

        total = d.pop("total", UNSET)

        per_page = d.pop("per_page", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        truncated = d.pop("truncated", UNSET)

        continuation = d.pop("continuation", UNSET)

        actions_rules_index_response_200_rules = cls(
            data=data,
            total=total,
            per_page=per_page,
            next_cursor=next_cursor,
            truncated=truncated,
            continuation=continuation,
        )

        actions_rules_index_response_200_rules.additional_properties = d
        return actions_rules_index_response_200_rules

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
