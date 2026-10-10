from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200ChangesItem")


@_attrs_define
class GetInventoryMetricsResponse200ChangesItem:
    """
    Attributes:
        id (int):
        platform_ad_account_id (int):
        level (str):
        external_id (str):
        field (str):
        old_value (None | str):
        new_value (None | str):
        observed_at (None | str):
    """

    id: int
    platform_ad_account_id: int
    level: str
    external_id: str
    field: str
    old_value: None | str
    new_value: None | str
    observed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform_ad_account_id = self.platform_ad_account_id

        level = self.level

        external_id = self.external_id

        field = self.field

        old_value: None | str
        old_value = self.old_value

        new_value: None | str
        new_value = self.new_value

        observed_at: None | str
        observed_at = self.observed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform_ad_account_id": platform_ad_account_id,
                "level": level,
                "external_id": external_id,
                "field": field,
                "old_value": old_value,
                "new_value": new_value,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        level = d.pop("level")

        external_id = d.pop("external_id")

        field = d.pop("field")

        def _parse_old_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        old_value = _parse_old_value(d.pop("old_value"))

        def _parse_new_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        new_value = _parse_new_value(d.pop("new_value"))

        def _parse_observed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        observed_at = _parse_observed_at(d.pop("observed_at"))

        get_inventory_metrics_response_200_changes_item = cls(
            id=id,
            platform_ad_account_id=platform_ad_account_id,
            level=level,
            external_id=external_id,
            field=field,
            old_value=old_value,
            new_value=new_value,
            observed_at=observed_at,
        )

        get_inventory_metrics_response_200_changes_item.additional_properties = d
        return get_inventory_metrics_response_200_changes_item

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
