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
        max_spend_delta_percent (str):
        hard_account_daily_cap_minor (int | None):
        protected_entities (list[Any] | None):
        quiet_hours_start (None | str):
        quiet_hours_end (None | str):
        protect_learning_phase (bool):
        outcome_check_after_hours (int):
        anomaly_threshold_percent (str):
    """

    id: int | None
    workspace_id: int
    execution_mode: ActionPolicyReadDataExecutionMode
    max_spend_delta_percent: str
    hard_account_daily_cap_minor: int | None
    protected_entities: list[Any] | None
    quiet_hours_start: None | str
    quiet_hours_end: None | str
    protect_learning_phase: bool
    outcome_check_after_hours: int
    anomaly_threshold_percent: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None
        id = self.id

        workspace_id = self.workspace_id

        execution_mode = self.execution_mode.value

        max_spend_delta_percent = self.max_spend_delta_percent

        hard_account_daily_cap_minor: int | None
        hard_account_daily_cap_minor = self.hard_account_daily_cap_minor

        protected_entities: list[Any] | None
        if isinstance(self.protected_entities, list):
            protected_entities = self.protected_entities

        else:
            protected_entities = self.protected_entities

        quiet_hours_start: None | str
        quiet_hours_start = self.quiet_hours_start

        quiet_hours_end: None | str
        quiet_hours_end = self.quiet_hours_end

        protect_learning_phase = self.protect_learning_phase

        outcome_check_after_hours = self.outcome_check_after_hours

        anomaly_threshold_percent = self.anomaly_threshold_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "execution_mode": execution_mode,
                "max_spend_delta_percent": max_spend_delta_percent,
                "hard_account_daily_cap_minor": hard_account_daily_cap_minor,
                "protected_entities": protected_entities,
                "quiet_hours_start": quiet_hours_start,
                "quiet_hours_end": quiet_hours_end,
                "protect_learning_phase": protect_learning_phase,
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

        max_spend_delta_percent = d.pop("max_spend_delta_percent")

        def _parse_hard_account_daily_cap_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hard_account_daily_cap_minor = _parse_hard_account_daily_cap_minor(d.pop("hard_account_daily_cap_minor"))

        def _parse_protected_entities(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protected_entities_type_0 = cast(list[Any], data)

                return protected_entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        protected_entities = _parse_protected_entities(d.pop("protected_entities"))

        def _parse_quiet_hours_start(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quiet_hours_start = _parse_quiet_hours_start(d.pop("quiet_hours_start"))

        def _parse_quiet_hours_end(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quiet_hours_end = _parse_quiet_hours_end(d.pop("quiet_hours_end"))

        protect_learning_phase = d.pop("protect_learning_phase")

        outcome_check_after_hours = d.pop("outcome_check_after_hours")

        anomaly_threshold_percent = d.pop("anomaly_threshold_percent")

        action_policy_read_data = cls(
            id=id,
            workspace_id=workspace_id,
            execution_mode=execution_mode,
            max_spend_delta_percent=max_spend_delta_percent,
            hard_account_daily_cap_minor=hard_account_daily_cap_minor,
            protected_entities=protected_entities,
            quiet_hours_start=quiet_hours_start,
            quiet_hours_end=quiet_hours_end,
            protect_learning_phase=protect_learning_phase,
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
