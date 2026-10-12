from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionListReadMeta")


@_attrs_define
class ActionListReadMeta:
    """Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP representations. Defaults are
    bounded. Follow next_cursor with the same scope and filters. One oversized row is explicitly refused; fields are
    never silently clipped.

        Attributes:
            current_page (int):
            last_page (int):
            per_page (int):
            total (int):
            next_cursor (int | None | Unset):
            truncated (bool | Unset):
            continuation (str | Unset):
    """

    current_page: int
    last_page: int
    per_page: int
    total: int
    next_cursor: int | None | Unset = UNSET
    truncated: bool | Unset = UNSET
    continuation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        total = self.total

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        truncated = self.truncated

        continuation = self.continuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "last_page": last_page,
                "per_page": per_page,
                "total": total,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if continuation is not UNSET:
            field_dict["continuation"] = continuation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page")

        last_page = d.pop("last_page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        truncated = d.pop("truncated", UNSET)

        continuation = d.pop("continuation", UNSET)

        action_list_read_meta = cls(
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            total=total,
            next_cursor=next_cursor,
            truncated=truncated,
            continuation=continuation,
        )

        action_list_read_meta.additional_properties = d
        return action_list_read_meta

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
