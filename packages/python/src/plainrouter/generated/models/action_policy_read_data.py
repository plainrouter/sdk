from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_policy_read_data_execution_mode import ActionPolicyReadDataExecutionMode

T = TypeVar("T", bound="ActionPolicyReadData")


@_attrs_define
class ActionPolicyReadData:
    """
    Attributes:
        id (int | None):
        workspace_id (int):
        execution_mode (ActionPolicyReadDataExecutionMode):
        outcome_check_after_hours (int):
        anomaly_threshold_percent (str):
    """

    id: int | None
    workspace_id: int
    execution_mode: ActionPolicyReadDataExecutionMode
    outcome_check_after_hours: int
    anomaly_threshold_percent: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None
        id = self.id

        workspace_id = self.workspace_id

        execution_mode = self.execution_mode.value

        outcome_check_after_hours = self.outcome_check_after_hours

        anomaly_threshold_percent = self.anomaly_threshold_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "execution_mode": execution_mode,
                "outcome_check_after_hours": outcome_check_after_hours,
                "anomaly_threshold_percent": anomaly_threshold_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        id = _parse_id(d.pop("id"))

        workspace_id = d.pop("workspace_id")

        execution_mode = ActionPolicyReadDataExecutionMode(d.pop("execution_mode"))

        outcome_check_after_hours = d.pop("outcome_check_after_hours")

        anomaly_threshold_percent = d.pop("anomaly_threshold_percent")

        action_policy_read_data = cls(
            id=id,
            workspace_id=workspace_id,
            execution_mode=execution_mode,
            outcome_check_after_hours=outcome_check_after_hours,
            anomaly_threshold_percent=anomaly_threshold_percent,
        )

        action_policy_read_data.additional_properties = d
        return action_policy_read_data

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
