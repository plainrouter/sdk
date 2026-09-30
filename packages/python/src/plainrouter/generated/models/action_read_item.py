from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_read_item_batch_status import ActionReadItemBatchStatus
from ..models.action_read_item_policy_decision_type_1 import ActionReadItemPolicyDecisionType1
from ..models.action_read_item_policy_decision_type_2_type_1 import ActionReadItemPolicyDecisionType2Type1
from ..models.action_read_item_policy_decision_type_3_type_1 import ActionReadItemPolicyDecisionType3Type1
from ..models.action_read_item_status import ActionReadItemStatus
from ..models.action_read_item_type import ActionReadItemType

if TYPE_CHECKING:
    from ..models.action_current_disposition import ActionCurrentDisposition
    from ..models.action_read_item_params_type_0 import ActionReadItemParamsType0


T = TypeVar("T", bound="ActionReadItem")


@_attrs_define
class ActionReadItem:
    """
    Attributes:
        id (str):
        batch_id (str):
        workspace_id (int):
        type_ (ActionReadItemType):
        target_entity_type (str):
        target_entity_id (str):
        target_entity_name (None | str):
        params (ActionReadItemParamsType0 | list[Any]):
        rationale (str):
        status (ActionReadItemStatus):
        batch_status (ActionReadItemBatchStatus):
        disposition (ActionCurrentDisposition):
        policy_decision (ActionReadItemPolicyDecisionType1 | ActionReadItemPolicyDecisionType2Type1 |
            ActionReadItemPolicyDecisionType3Type1 | None):
        policy_reasons (list[str]):
    """

    id: str
    batch_id: str
    workspace_id: int
    type_: ActionReadItemType
    target_entity_type: str
    target_entity_id: str
    target_entity_name: None | str
    params: ActionReadItemParamsType0 | list[Any]
    rationale: str
    status: ActionReadItemStatus
    batch_status: ActionReadItemBatchStatus
    disposition: ActionCurrentDisposition
    policy_decision: (
        ActionReadItemPolicyDecisionType1
        | ActionReadItemPolicyDecisionType2Type1
        | ActionReadItemPolicyDecisionType3Type1
        | None
    )
    policy_reasons: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_read_item_params_type_0 import ActionReadItemParamsType0

        id = self.id

        batch_id = self.batch_id

        workspace_id = self.workspace_id

        type_ = self.type_.value

        target_entity_type = self.target_entity_type

        target_entity_id = self.target_entity_id

        target_entity_name: None | str
        target_entity_name = self.target_entity_name

        params: dict[str, Any] | list[Any]
        if isinstance(self.params, ActionReadItemParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        rationale = self.rationale

        status = self.status.value

        batch_status = self.batch_status.value

        disposition = self.disposition.to_dict()

        policy_decision: None | str
        if isinstance(self.policy_decision, ActionReadItemPolicyDecisionType1):
            policy_decision = self.policy_decision.value
        elif isinstance(self.policy_decision, ActionReadItemPolicyDecisionType2Type1):
            policy_decision = self.policy_decision.value
        elif isinstance(self.policy_decision, ActionReadItemPolicyDecisionType3Type1):
            policy_decision = self.policy_decision.value
        else:
            policy_decision = self.policy_decision

        policy_reasons = self.policy_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "batch_id": batch_id,
                "workspace_id": workspace_id,
                "type": type_,
                "target_entity_type": target_entity_type,
                "target_entity_id": target_entity_id,
                "target_entity_name": target_entity_name,
                "params": params,
                "rationale": rationale,
                "status": status,
                "batch_status": batch_status,
                "disposition": disposition,
                "policy_decision": policy_decision,
                "policy_reasons": policy_reasons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_current_disposition import ActionCurrentDisposition
        from ..models.action_read_item_params_type_0 import ActionReadItemParamsType0

        d = dict(src_dict)
        id = d.pop("id")

        batch_id = d.pop("batch_id")

        workspace_id = d.pop("workspace_id")

        type_ = ActionReadItemType(d.pop("type"))

        target_entity_type = d.pop("target_entity_type")

        target_entity_id = d.pop("target_entity_id")

        def _parse_target_entity_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_entity_name = _parse_target_entity_name(d.pop("target_entity_name"))

        def _parse_params(data: object) -> ActionReadItemParamsType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ActionReadItemParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            params_type_1 = cast(list[Any], data)

            return params_type_1

        params = _parse_params(d.pop("params"))

        rationale = d.pop("rationale")

        status = ActionReadItemStatus(d.pop("status"))

        batch_status = ActionReadItemBatchStatus(d.pop("batch_status"))

        disposition = ActionCurrentDisposition.from_dict(d.pop("disposition"))

        def _parse_policy_decision(
            data: object,
        ) -> (
            ActionReadItemPolicyDecisionType1
            | ActionReadItemPolicyDecisionType2Type1
            | ActionReadItemPolicyDecisionType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_decision_type_1 = ActionReadItemPolicyDecisionType1(data)

                return policy_decision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_decision_type_2_type_1 = ActionReadItemPolicyDecisionType2Type1(data)

                return policy_decision_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_decision_type_3_type_1 = ActionReadItemPolicyDecisionType3Type1(data)

                return policy_decision_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ActionReadItemPolicyDecisionType1
                | ActionReadItemPolicyDecisionType2Type1
                | ActionReadItemPolicyDecisionType3Type1
                | None,
                data,
            )

        policy_decision = _parse_policy_decision(d.pop("policy_decision"))

        policy_reasons = cast(list[str], d.pop("policy_reasons"))

        action_read_item = cls(
            id=id,
            batch_id=batch_id,
            workspace_id=workspace_id,
            type_=type_,
            target_entity_type=target_entity_type,
            target_entity_id=target_entity_id,
            target_entity_name=target_entity_name,
            params=params,
            rationale=rationale,
            status=status,
            batch_status=batch_status,
            disposition=disposition,
            policy_decision=policy_decision,
            policy_reasons=policy_reasons,
        )

        action_read_item.additional_properties = d
        return action_read_item

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
