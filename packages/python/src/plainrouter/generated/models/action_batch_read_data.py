from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_batch_read_data_batch_status import ActionBatchReadDataBatchStatus
from ..models.action_batch_read_data_restoration_summary_type_1 import ActionBatchReadDataRestorationSummaryType1
from ..models.action_batch_read_data_restoration_summary_type_2_type_1 import (
    ActionBatchReadDataRestorationSummaryType2Type1,
)
from ..models.action_batch_read_data_restoration_summary_type_3_type_1 import (
    ActionBatchReadDataRestorationSummaryType3Type1,
)
from ..models.action_batch_read_data_status import ActionBatchReadDataStatus

if TYPE_CHECKING:
    from ..models.action_read_item import ActionReadItem


T = TypeVar("T", bound="ActionBatchReadData")


@_attrs_define
class ActionBatchReadData:
    """
    Attributes:
        status (ActionBatchReadDataStatus):
        batch_status (ActionBatchReadDataBatchStatus):
        restoration_summary (ActionBatchReadDataRestorationSummaryType1 |
            ActionBatchReadDataRestorationSummaryType2Type1 | ActionBatchReadDataRestorationSummaryType3Type1 | None):
        actions (list[ActionReadItem]):
    """

    status: ActionBatchReadDataStatus
    batch_status: ActionBatchReadDataBatchStatus
    restoration_summary: (
        ActionBatchReadDataRestorationSummaryType1
        | ActionBatchReadDataRestorationSummaryType2Type1
        | ActionBatchReadDataRestorationSummaryType3Type1
        | None
    )
    actions: list[ActionReadItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        batch_status = self.batch_status.value

        restoration_summary: None | str
        if isinstance(self.restoration_summary, ActionBatchReadDataRestorationSummaryType1):
            restoration_summary = self.restoration_summary.value
        elif isinstance(self.restoration_summary, ActionBatchReadDataRestorationSummaryType2Type1):
            restoration_summary = self.restoration_summary.value
        elif isinstance(self.restoration_summary, ActionBatchReadDataRestorationSummaryType3Type1):
            restoration_summary = self.restoration_summary.value
        else:
            restoration_summary = self.restoration_summary

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "batch_status": batch_status,
                "restoration_summary": restoration_summary,
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_read_item import ActionReadItem

        d = dict(src_dict)
        status = ActionBatchReadDataStatus(d.pop("status"))

        batch_status = ActionBatchReadDataBatchStatus(d.pop("batch_status"))

        def _parse_restoration_summary(
            data: object,
        ) -> (
            ActionBatchReadDataRestorationSummaryType1
            | ActionBatchReadDataRestorationSummaryType2Type1
            | ActionBatchReadDataRestorationSummaryType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restoration_summary_type_1 = ActionBatchReadDataRestorationSummaryType1(data)

                return restoration_summary_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restoration_summary_type_2_type_1 = ActionBatchReadDataRestorationSummaryType2Type1(data)

                return restoration_summary_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restoration_summary_type_3_type_1 = ActionBatchReadDataRestorationSummaryType3Type1(data)

                return restoration_summary_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ActionBatchReadDataRestorationSummaryType1
                | ActionBatchReadDataRestorationSummaryType2Type1
                | ActionBatchReadDataRestorationSummaryType3Type1
                | None,
                data,
            )

        restoration_summary = _parse_restoration_summary(d.pop("restoration_summary"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = ActionReadItem.from_dict(actions_item_data)

            actions.append(actions_item)

        action_batch_read_data = cls(
            status=status,
            batch_status=batch_status,
            restoration_summary=restoration_summary,
            actions=actions,
        )

        action_batch_read_data.additional_properties = d
        return action_batch_read_data

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
