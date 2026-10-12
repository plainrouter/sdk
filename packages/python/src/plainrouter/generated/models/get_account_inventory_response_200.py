from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_account_inventory_response_200_account import GetAccountInventoryResponse200Account
    from ..models.get_account_inventory_response_200_objects_item import GetAccountInventoryResponse200ObjectsItem
    from ..models.get_account_inventory_response_200_staleness import GetAccountInventoryResponse200Staleness
    from ..models.get_account_inventory_response_200_summary import GetAccountInventoryResponse200Summary
    from ..models.get_account_inventory_response_200_sync import GetAccountInventoryResponse200Sync


T = TypeVar("T", bound="GetAccountInventoryResponse200")


@_attrs_define
class GetAccountInventoryResponse200:
    """Complete projection rows are paged within 80,000 JSON bytes, accounting for both MCP representations. Defaults are
    bounded. Follow next_cursor with the same scope and filters. One oversized row is explicitly refused; fields are
    never silently clipped.

        Attributes:
            account (GetAccountInventoryResponse200Account):
            sync (GetAccountInventoryResponse200Sync):
            staleness (GetAccountInventoryResponse200Staleness):
            summary (GetAccountInventoryResponse200Summary):
            objects (list[GetAccountInventoryResponse200ObjectsItem]):
            next_cursor (int | None):
            truncated (bool):
            continuation (str):
    """

    account: GetAccountInventoryResponse200Account
    sync: GetAccountInventoryResponse200Sync
    staleness: GetAccountInventoryResponse200Staleness
    summary: GetAccountInventoryResponse200Summary
    objects: list[GetAccountInventoryResponse200ObjectsItem]
    next_cursor: int | None
    truncated: bool
    continuation: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        sync = self.sync.to_dict()

        staleness = self.staleness.to_dict()

        summary = self.summary.to_dict()

        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        next_cursor: int | None
        next_cursor = self.next_cursor

        truncated = self.truncated

        continuation = self.continuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "sync": sync,
                "staleness": staleness,
                "summary": summary,
                "objects": objects,
                "next_cursor": next_cursor,
                "truncated": truncated,
                "continuation": continuation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_account_inventory_response_200_account import GetAccountInventoryResponse200Account
        from ..models.get_account_inventory_response_200_objects_item import GetAccountInventoryResponse200ObjectsItem
        from ..models.get_account_inventory_response_200_staleness import GetAccountInventoryResponse200Staleness
        from ..models.get_account_inventory_response_200_summary import GetAccountInventoryResponse200Summary
        from ..models.get_account_inventory_response_200_sync import GetAccountInventoryResponse200Sync

        d = dict(src_dict)
        account = GetAccountInventoryResponse200Account.from_dict(d.pop("account"))

        sync = GetAccountInventoryResponse200Sync.from_dict(d.pop("sync"))

        staleness = GetAccountInventoryResponse200Staleness.from_dict(d.pop("staleness"))

        summary = GetAccountInventoryResponse200Summary.from_dict(d.pop("summary"))

        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = GetAccountInventoryResponse200ObjectsItem.from_dict(objects_item_data)

            objects.append(objects_item)

        def _parse_next_cursor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        truncated = d.pop("truncated")

        continuation = d.pop("continuation")

        get_account_inventory_response_200 = cls(
            account=account,
            sync=sync,
            staleness=staleness,
            summary=summary,
            objects=objects,
            next_cursor=next_cursor,
            truncated=truncated,
            continuation=continuation,
        )

        get_account_inventory_response_200.additional_properties = d
        return get_account_inventory_response_200

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
