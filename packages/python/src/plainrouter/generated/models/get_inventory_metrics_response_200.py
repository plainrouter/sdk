from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_inventory_metrics_response_200_account import GetInventoryMetricsResponse200Account
    from ..models.get_inventory_metrics_response_200_changes_item import GetInventoryMetricsResponse200ChangesItem
    from ..models.get_inventory_metrics_response_200_effective_range_type_0 import (
        GetInventoryMetricsResponse200EffectiveRangeType0,
    )
    from ..models.get_inventory_metrics_response_200_metrics_item import GetInventoryMetricsResponse200MetricsItem
    from ..models.get_inventory_metrics_response_200_object_metrics_item import (
        GetInventoryMetricsResponse200ObjectMetricsItem,
    )
    from ..models.get_inventory_metrics_response_200_staleness import GetInventoryMetricsResponse200Staleness
    from ..models.get_inventory_metrics_response_200_sync import GetInventoryMetricsResponse200Sync


T = TypeVar("T", bound="GetInventoryMetricsResponse200")


@_attrs_define
class GetInventoryMetricsResponse200:
    """
    Attributes:
        account (GetInventoryMetricsResponse200Account):
        sync (GetInventoryMetricsResponse200Sync):
        staleness (GetInventoryMetricsResponse200Staleness):
        metrics (list[GetInventoryMetricsResponse200MetricsItem]):
        changes (list[GetInventoryMetricsResponse200ChangesItem]):
        effective_range (GetInventoryMetricsResponse200EffectiveRangeType0 | None):
        object_metrics (list[GetInventoryMetricsResponse200ObjectMetricsItem]):
        unmatched_arrivals (int | None):
    """

    account: GetInventoryMetricsResponse200Account
    sync: GetInventoryMetricsResponse200Sync
    staleness: GetInventoryMetricsResponse200Staleness
    metrics: list[GetInventoryMetricsResponse200MetricsItem]
    changes: list[GetInventoryMetricsResponse200ChangesItem]
    effective_range: GetInventoryMetricsResponse200EffectiveRangeType0 | None
    object_metrics: list[GetInventoryMetricsResponse200ObjectMetricsItem]
    unmatched_arrivals: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_inventory_metrics_response_200_effective_range_type_0 import (
            GetInventoryMetricsResponse200EffectiveRangeType0,
        )

        account = self.account.to_dict()

        sync = self.sync.to_dict()

        staleness = self.staleness.to_dict()

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        effective_range: dict[str, Any] | None
        if isinstance(self.effective_range, GetInventoryMetricsResponse200EffectiveRangeType0):
            effective_range = self.effective_range.to_dict()
        else:
            effective_range = self.effective_range

        object_metrics = []
        for object_metrics_item_data in self.object_metrics:
            object_metrics_item = object_metrics_item_data.to_dict()
            object_metrics.append(object_metrics_item)

        unmatched_arrivals: int | None
        unmatched_arrivals = self.unmatched_arrivals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "sync": sync,
                "staleness": staleness,
                "metrics": metrics,
                "changes": changes,
                "effective_range": effective_range,
                "object_metrics": object_metrics,
                "unmatched_arrivals": unmatched_arrivals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inventory_metrics_response_200_account import GetInventoryMetricsResponse200Account
        from ..models.get_inventory_metrics_response_200_changes_item import GetInventoryMetricsResponse200ChangesItem
        from ..models.get_inventory_metrics_response_200_effective_range_type_0 import (
            GetInventoryMetricsResponse200EffectiveRangeType0,
        )
        from ..models.get_inventory_metrics_response_200_metrics_item import GetInventoryMetricsResponse200MetricsItem
        from ..models.get_inventory_metrics_response_200_object_metrics_item import (
            GetInventoryMetricsResponse200ObjectMetricsItem,
        )
        from ..models.get_inventory_metrics_response_200_staleness import GetInventoryMetricsResponse200Staleness
        from ..models.get_inventory_metrics_response_200_sync import GetInventoryMetricsResponse200Sync

        d = dict(src_dict)
        account = GetInventoryMetricsResponse200Account.from_dict(d.pop("account"))

        sync = GetInventoryMetricsResponse200Sync.from_dict(d.pop("sync"))

        staleness = GetInventoryMetricsResponse200Staleness.from_dict(d.pop("staleness"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = GetInventoryMetricsResponse200MetricsItem.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = GetInventoryMetricsResponse200ChangesItem.from_dict(changes_item_data)

            changes.append(changes_item)

        def _parse_effective_range(data: object) -> GetInventoryMetricsResponse200EffectiveRangeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_range_type_0 = GetInventoryMetricsResponse200EffectiveRangeType0.from_dict(data)

                return effective_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetInventoryMetricsResponse200EffectiveRangeType0 | None, data)

        effective_range = _parse_effective_range(d.pop("effective_range"))

        object_metrics = []
        _object_metrics = d.pop("object_metrics")
        for object_metrics_item_data in _object_metrics:
            object_metrics_item = GetInventoryMetricsResponse200ObjectMetricsItem.from_dict(object_metrics_item_data)

            object_metrics.append(object_metrics_item)

        def _parse_unmatched_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        unmatched_arrivals = _parse_unmatched_arrivals(d.pop("unmatched_arrivals"))

        get_inventory_metrics_response_200 = cls(
            account=account,
            sync=sync,
            staleness=staleness,
            metrics=metrics,
            changes=changes,
            effective_range=effective_range,
            object_metrics=object_metrics,
            unmatched_arrivals=unmatched_arrivals,
        )

        get_inventory_metrics_response_200.additional_properties = d
        return get_inventory_metrics_response_200

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
