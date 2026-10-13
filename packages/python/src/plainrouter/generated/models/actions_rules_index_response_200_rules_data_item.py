from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_rules_index_response_200_rules_data_item_status import (
    ActionsRulesIndexResponse200RulesDataItemStatus,
)

if TYPE_CHECKING:
    from ..models.actions_rules_index_response_200_rules_data_item_account import (
        ActionsRulesIndexResponse200RulesDataItemAccount,
    )
    from ..models.actions_rules_index_response_200_rules_data_item_counts import (
        ActionsRulesIndexResponse200RulesDataItemCounts,
    )
    from ..models.actions_rules_index_response_200_rules_data_item_current_revision import (
        ActionsRulesIndexResponse200RulesDataItemCurrentRevision,
    )


T = TypeVar("T", bound="ActionsRulesIndexResponse200RulesDataItem")


@_attrs_define
class ActionsRulesIndexResponse200RulesDataItem:
    """
    Attributes:
        id (str):
        name (str):
        status (ActionsRulesIndexResponse200RulesDataItemStatus):
        account (ActionsRulesIndexResponse200RulesDataItemAccount):
        current_revision (ActionsRulesIndexResponse200RulesDataItemCurrentRevision):
        last_run_status (None | str):
        last_run_at (None | str):
        counts (ActionsRulesIndexResponse200RulesDataItemCounts):
    """

    id: str
    name: str
    status: ActionsRulesIndexResponse200RulesDataItemStatus
    account: ActionsRulesIndexResponse200RulesDataItemAccount
    current_revision: ActionsRulesIndexResponse200RulesDataItemCurrentRevision
    last_run_status: None | str
    last_run_at: None | str
    counts: ActionsRulesIndexResponse200RulesDataItemCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        account = self.account.to_dict()

        current_revision = self.current_revision.to_dict()

        last_run_status: None | str
        last_run_status = self.last_run_status

        last_run_at: None | str
        last_run_at = self.last_run_at

        counts = self.counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "account": account,
                "current_revision": current_revision,
                "last_run_status": last_run_status,
                "last_run_at": last_run_at,
                "counts": counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actions_rules_index_response_200_rules_data_item_account import (
            ActionsRulesIndexResponse200RulesDataItemAccount,
        )
        from ..models.actions_rules_index_response_200_rules_data_item_counts import (
            ActionsRulesIndexResponse200RulesDataItemCounts,
        )
        from ..models.actions_rules_index_response_200_rules_data_item_current_revision import (
            ActionsRulesIndexResponse200RulesDataItemCurrentRevision,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = ActionsRulesIndexResponse200RulesDataItemStatus(d.pop("status"))

        account = ActionsRulesIndexResponse200RulesDataItemAccount.from_dict(d.pop("account"))

        current_revision = ActionsRulesIndexResponse200RulesDataItemCurrentRevision.from_dict(d.pop("current_revision"))

        def _parse_last_run_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_run_status = _parse_last_run_status(d.pop("last_run_status"))

        def _parse_last_run_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_run_at = _parse_last_run_at(d.pop("last_run_at"))

        counts = ActionsRulesIndexResponse200RulesDataItemCounts.from_dict(d.pop("counts"))

        actions_rules_index_response_200_rules_data_item = cls(
            id=id,
            name=name,
            status=status,
            account=account,
            current_revision=current_revision,
            last_run_status=last_run_status,
            last_run_at=last_run_at,
            counts=counts,
        )

        actions_rules_index_response_200_rules_data_item.additional_properties = d
        return actions_rules_index_response_200_rules_data_item

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
