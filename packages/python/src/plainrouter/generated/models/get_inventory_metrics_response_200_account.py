from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInventoryMetricsResponse200Account")


@_attrs_define
class GetInventoryMetricsResponse200Account:
    """
    Attributes:
        id (int):
        external_id (str):
        name (None | str):
        currency (None | str):
        timezone (None | str):
        status (str):
        connection_status (None | str):
    """

    id: int
    external_id: str
    name: None | str
    currency: None | str
    timezone: None | str
    status: str
    connection_status: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        name: None | str
        name = self.name

        currency: None | str
        currency = self.currency

        timezone: None | str
        timezone = self.timezone

        status = self.status

        connection_status: None | str
        connection_status = self.connection_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "name": name,
                "currency": currency,
                "timezone": timezone,
                "status": status,
                "connection_status": connection_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("external_id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        status = d.pop("status")

        def _parse_connection_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connection_status = _parse_connection_status(d.pop("connection_status"))

        get_inventory_metrics_response_200_account = cls(
            id=id,
            external_id=external_id,
            name=name,
            currency=currency,
            timezone=timezone,
            status=status,
            connection_status=connection_status,
        )

        get_inventory_metrics_response_200_account.additional_properties = d
        return get_inventory_metrics_response_200_account

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
