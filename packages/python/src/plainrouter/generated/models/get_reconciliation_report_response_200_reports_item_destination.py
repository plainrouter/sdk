from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.destination_credential_source import DestinationCredentialSource
from ..models.destination_status import DestinationStatus
from ..models.destination_type import DestinationType

if TYPE_CHECKING:
    from ..models.get_reconciliation_report_response_200_reports_item_destination_config_type_0 import (
        GetReconciliationReportResponse200ReportsItemDestinationConfigType0,
    )


T = TypeVar("T", bound="GetReconciliationReportResponse200ReportsItemDestination")


@_attrs_define
class GetReconciliationReportResponse200ReportsItemDestination:
    """
    Attributes:
        id (str):
        signal_tracker_id (str):
        platform_ad_account_id (int | None):
        type_ (DestinationType):
        credential_source (DestinationCredentialSource):
        config (GetReconciliationReportResponse200ReportsItemDestinationConfigType0 | list[Any] | None):
        status (DestinationStatus):
        created_at (None | str):
        updated_at (None | str):
    """

    id: str
    signal_tracker_id: str
    platform_ad_account_id: int | None
    type_: DestinationType
    credential_source: DestinationCredentialSource
    config: GetReconciliationReportResponse200ReportsItemDestinationConfigType0 | list[Any] | None
    status: DestinationStatus
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_reconciliation_report_response_200_reports_item_destination_config_type_0 import (
            GetReconciliationReportResponse200ReportsItemDestinationConfigType0,
        )

        id = self.id

        signal_tracker_id = self.signal_tracker_id

        platform_ad_account_id: int | None
        platform_ad_account_id = self.platform_ad_account_id

        type_ = self.type_.value

        credential_source = self.credential_source.value

        config: dict[str, Any] | list[Any] | None
        if isinstance(self.config, GetReconciliationReportResponse200ReportsItemDestinationConfigType0):
            config = self.config.to_dict()
        elif isinstance(self.config, list):
            config = self.config

        else:
            config = self.config

        status = self.status.value

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "platform_ad_account_id": platform_ad_account_id,
                "type": type_,
                "credential_source": credential_source,
                "config": config,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_reconciliation_report_response_200_reports_item_destination_config_type_0 import (
            GetReconciliationReportResponse200ReportsItemDestinationConfigType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_platform_ad_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        platform_ad_account_id = _parse_platform_ad_account_id(d.pop("platform_ad_account_id"))

        type_ = DestinationType(d.pop("type"))

        credential_source = DestinationCredentialSource(d.pop("credential_source"))

        def _parse_config(
            data: object,
        ) -> GetReconciliationReportResponse200ReportsItemDestinationConfigType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = GetReconciliationReportResponse200ReportsItemDestinationConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_type_1 = cast(list[Any], data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetReconciliationReportResponse200ReportsItemDestinationConfigType0 | list[Any] | None, data)

        config = _parse_config(d.pop("config"))

        status = DestinationStatus(d.pop("status"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        get_reconciliation_report_response_200_reports_item_destination = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            platform_ad_account_id=platform_ad_account_id,
            type_=type_,
            credential_source=credential_source,
            config=config,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_reconciliation_report_response_200_reports_item_destination.additional_properties = d
        return get_reconciliation_report_response_200_reports_item_destination

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
