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
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_current_disposition import ActionCurrentDisposition
    from ..models.action_policy_result import ActionPolicyResult
    from ..models.action_read_item_evidence_type_0 import ActionReadItemEvidenceType0
    from ..models.action_read_item_evidence_type_1 import ActionReadItemEvidenceType1
    from ..models.action_read_item_evidence_type_2 import ActionReadItemEvidenceType2
    from ..models.action_read_item_params_type_0 import ActionReadItemParamsType0
    from ..models.action_read_item_proposer import ActionReadItemProposer


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
        policy_result (ActionPolicyResult | None):
        policy_results (list[ActionPolicyResult]):
        proposer (ActionReadItemProposer | Unset):
        evidence (ActionReadItemEvidenceType0 | ActionReadItemEvidenceType1 | ActionReadItemEvidenceType2 | Unset):
            System evidence cites either the original action and its counted outcome or the rule, revision, run and
            decision.
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
    policy_result: ActionPolicyResult | None
    policy_results: list[ActionPolicyResult]
    proposer: ActionReadItemProposer | Unset = UNSET
    evidence: ActionReadItemEvidenceType0 | ActionReadItemEvidenceType1 | ActionReadItemEvidenceType2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_policy_result import ActionPolicyResult
        from ..models.action_read_item_evidence_type_0 import ActionReadItemEvidenceType0
        from ..models.action_read_item_evidence_type_1 import ActionReadItemEvidenceType1
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

        policy_result: dict[str, Any] | None
        if isinstance(self.policy_result, ActionPolicyResult):
            policy_result = self.policy_result.to_dict()
        else:
            policy_result = self.policy_result

        policy_results = []
        for policy_results_item_data in self.policy_results:
            policy_results_item = policy_results_item_data.to_dict()
            policy_results.append(policy_results_item)

        proposer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proposer, Unset):
            proposer = self.proposer.to_dict()

        evidence: dict[str, Any] | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, ActionReadItemEvidenceType0):
            evidence = self.evidence.to_dict()
        elif isinstance(self.evidence, ActionReadItemEvidenceType1):
            evidence = self.evidence.to_dict()
        else:
            evidence = self.evidence.to_dict()

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
                "policy_result": policy_result,
                "policy_results": policy_results,
            }
        )
        if proposer is not UNSET:
            field_dict["proposer"] = proposer
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_current_disposition import ActionCurrentDisposition
        from ..models.action_policy_result import ActionPolicyResult
        from ..models.action_read_item_evidence_type_0 import ActionReadItemEvidenceType0
        from ..models.action_read_item_evidence_type_1 import ActionReadItemEvidenceType1
        from ..models.action_read_item_evidence_type_2 import ActionReadItemEvidenceType2
        from ..models.action_read_item_params_type_0 import ActionReadItemParamsType0
        from ..models.action_read_item_proposer import ActionReadItemProposer

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

        def _parse_policy_result(data: object) -> ActionPolicyResult | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_result_type_0 = ActionPolicyResult.from_dict(data)

                return policy_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionPolicyResult | None, data)

        policy_result = _parse_policy_result(d.pop("policy_result"))

        policy_results = []
        _policy_results = d.pop("policy_results")
        for policy_results_item_data in _policy_results:
            policy_results_item = ActionPolicyResult.from_dict(policy_results_item_data)

            policy_results.append(policy_results_item)

        _proposer = d.pop("proposer", UNSET)
        proposer: ActionReadItemProposer | Unset
        if isinstance(_proposer, Unset):
            proposer = UNSET
        else:
            proposer = ActionReadItemProposer.from_dict(_proposer)

        def _parse_evidence(
            data: object,
        ) -> ActionReadItemEvidenceType0 | ActionReadItemEvidenceType1 | ActionReadItemEvidenceType2 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evidence_type_0 = ActionReadItemEvidenceType0.from_dict(data)

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evidence_type_1 = ActionReadItemEvidenceType1.from_dict(data)

                return evidence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            evidence_type_2 = ActionReadItemEvidenceType2.from_dict(data)

            return evidence_type_2

        evidence = _parse_evidence(d.pop("evidence", UNSET))

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
            policy_result=policy_result,
            policy_results=policy_results,
            proposer=proposer,
            evidence=evidence,
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
