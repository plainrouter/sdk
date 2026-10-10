from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_inventory_metrics_response_200_object_metrics_item_level import (
    GetInventoryMetricsResponse200ObjectMetricsItemLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_inventory_metrics_response_200_object_metrics_item_meta_type_0 import (
        GetInventoryMetricsResponse200ObjectMetricsItemMetaType0,
    )


T = TypeVar("T", bound="GetInventoryMetricsResponse200ObjectMetricsItem")


@_attrs_define
class GetInventoryMetricsResponse200ObjectMetricsItem:
    """
    Attributes:
        level (GetInventoryMetricsResponse200ObjectMetricsItemLevel):
        external_id (str):
        date (str):
        meta (GetInventoryMetricsResponse200ObjectMetricsItemMetaType0 | None):
        arrivals (int | None):
        creative_id (None | str | Unset):
        generator (None | str | Unset):
        generator_job (None | str | Unset):
        parent_creative (None | str | Unset):
    """

    level: GetInventoryMetricsResponse200ObjectMetricsItemLevel
    external_id: str
    date: str
    meta: GetInventoryMetricsResponse200ObjectMetricsItemMetaType0 | None
    arrivals: int | None
    creative_id: None | str | Unset = UNSET
    generator: None | str | Unset = UNSET
    generator_job: None | str | Unset = UNSET
    parent_creative: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_inventory_metrics_response_200_object_metrics_item_meta_type_0 import (
            GetInventoryMetricsResponse200ObjectMetricsItemMetaType0,
        )

        level = self.level.value

        external_id = self.external_id

        date = self.date

        meta: dict[str, Any] | None
        if isinstance(self.meta, GetInventoryMetricsResponse200ObjectMetricsItemMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        arrivals: int | None
        arrivals = self.arrivals

        creative_id: None | str | Unset
        if isinstance(self.creative_id, Unset):
            creative_id = UNSET
        else:
            creative_id = self.creative_id

        generator: None | str | Unset
        if isinstance(self.generator, Unset):
            generator = UNSET
        else:
            generator = self.generator

        generator_job: None | str | Unset
        if isinstance(self.generator_job, Unset):
            generator_job = UNSET
        else:
            generator_job = self.generator_job

        parent_creative: None | str | Unset
        if isinstance(self.parent_creative, Unset):
            parent_creative = UNSET
        else:
            parent_creative = self.parent_creative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "external_id": external_id,
                "date": date,
                "meta": meta,
                "arrivals": arrivals,
            }
        )
        if creative_id is not UNSET:
            field_dict["creative_id"] = creative_id
        if generator is not UNSET:
            field_dict["generator"] = generator
        if generator_job is not UNSET:
            field_dict["generator_job"] = generator_job
        if parent_creative is not UNSET:
            field_dict["parent_creative"] = parent_creative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inventory_metrics_response_200_object_metrics_item_meta_type_0 import (
            GetInventoryMetricsResponse200ObjectMetricsItemMetaType0,
        )

        d = dict(src_dict)
        level = GetInventoryMetricsResponse200ObjectMetricsItemLevel(d.pop("level"))

        external_id = d.pop("external_id")

        date = d.pop("date")

        def _parse_meta(data: object) -> GetInventoryMetricsResponse200ObjectMetricsItemMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = GetInventoryMetricsResponse200ObjectMetricsItemMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetInventoryMetricsResponse200ObjectMetricsItemMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        def _parse_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        arrivals = _parse_arrivals(d.pop("arrivals"))

        def _parse_creative_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creative_id = _parse_creative_id(d.pop("creative_id", UNSET))

        def _parse_generator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generator = _parse_generator(d.pop("generator", UNSET))

        def _parse_generator_job(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generator_job = _parse_generator_job(d.pop("generator_job", UNSET))

        def _parse_parent_creative(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_creative = _parse_parent_creative(d.pop("parent_creative", UNSET))

        get_inventory_metrics_response_200_object_metrics_item = cls(
            level=level,
            external_id=external_id,
            date=date,
            meta=meta,
            arrivals=arrivals,
            creative_id=creative_id,
            generator=generator,
            generator_job=generator_job,
            parent_creative=parent_creative,
        )

        get_inventory_metrics_response_200_object_metrics_item.additional_properties = d
        return get_inventory_metrics_response_200_object_metrics_item

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
