from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_proposal_input_target_source import ActionProposalInputTargetSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_proposal_input_actions_item_type_0 import ActionProposalInputActionsItemType0
    from ..models.action_proposal_input_actions_item_type_1 import ActionProposalInputActionsItemType1
    from ..models.action_proposal_input_actions_item_type_2 import ActionProposalInputActionsItemType2
    from ..models.action_proposal_input_actions_item_type_3 import ActionProposalInputActionsItemType3
    from ..models.action_proposal_input_actions_item_type_4 import ActionProposalInputActionsItemType4
    from ..models.action_proposal_input_actions_item_type_5 import ActionProposalInputActionsItemType5
    from ..models.action_proposal_input_actions_item_type_6 import ActionProposalInputActionsItemType6
    from ..models.action_proposal_input_actions_item_type_7 import ActionProposalInputActionsItemType7
    from ..models.action_proposal_input_actions_item_type_8 import ActionProposalInputActionsItemType8
    from ..models.action_proposal_input_actions_item_type_9 import ActionProposalInputActionsItemType9
    from ..models.action_proposal_input_actions_item_type_10 import ActionProposalInputActionsItemType10
    from ..models.action_proposal_input_actions_item_type_11 import ActionProposalInputActionsItemType11
    from ..models.action_proposal_input_actions_item_type_12 import ActionProposalInputActionsItemType12
    from ..models.action_proposal_input_actions_item_type_13 import ActionProposalInputActionsItemType13
    from ..models.action_proposal_input_evidence_item import ActionProposalInputEvidenceItem


T = TypeVar("T", bound="ActionProposalInput")


@_attrs_define
class ActionProposalInput:
    """
    Attributes:
        actions (list[ActionProposalInputActionsItemType0 | ActionProposalInputActionsItemType1 |
            ActionProposalInputActionsItemType10 | ActionProposalInputActionsItemType11 |
            ActionProposalInputActionsItemType12 | ActionProposalInputActionsItemType13 |
            ActionProposalInputActionsItemType2 | ActionProposalInputActionsItemType3 | ActionProposalInputActionsItemType4
            | ActionProposalInputActionsItemType5 | ActionProposalInputActionsItemType6 |
            ActionProposalInputActionsItemType7 | ActionProposalInputActionsItemType8 |
            ActionProposalInputActionsItemType9]):
        rationale (str):
        idempotency_key (str):
        evidence (list[ActionProposalInputEvidenceItem]):
        target_source (ActionProposalInputTargetSource):
        account_id (int | Unset):
        workspace_id (int | Unset):
    """

    actions: list[
        ActionProposalInputActionsItemType0
        | ActionProposalInputActionsItemType1
        | ActionProposalInputActionsItemType10
        | ActionProposalInputActionsItemType11
        | ActionProposalInputActionsItemType12
        | ActionProposalInputActionsItemType13
        | ActionProposalInputActionsItemType2
        | ActionProposalInputActionsItemType3
        | ActionProposalInputActionsItemType4
        | ActionProposalInputActionsItemType5
        | ActionProposalInputActionsItemType6
        | ActionProposalInputActionsItemType7
        | ActionProposalInputActionsItemType8
        | ActionProposalInputActionsItemType9
    ]
    rationale: str
    idempotency_key: str
    evidence: list[ActionProposalInputEvidenceItem]
    target_source: ActionProposalInputTargetSource
    account_id: int | Unset = UNSET
    workspace_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_proposal_input_actions_item_type_0 import ActionProposalInputActionsItemType0
        from ..models.action_proposal_input_actions_item_type_1 import ActionProposalInputActionsItemType1
        from ..models.action_proposal_input_actions_item_type_2 import ActionProposalInputActionsItemType2
        from ..models.action_proposal_input_actions_item_type_3 import ActionProposalInputActionsItemType3
        from ..models.action_proposal_input_actions_item_type_4 import ActionProposalInputActionsItemType4
        from ..models.action_proposal_input_actions_item_type_5 import ActionProposalInputActionsItemType5
        from ..models.action_proposal_input_actions_item_type_6 import ActionProposalInputActionsItemType6
        from ..models.action_proposal_input_actions_item_type_7 import ActionProposalInputActionsItemType7
        from ..models.action_proposal_input_actions_item_type_8 import ActionProposalInputActionsItemType8
        from ..models.action_proposal_input_actions_item_type_9 import ActionProposalInputActionsItemType9
        from ..models.action_proposal_input_actions_item_type_10 import ActionProposalInputActionsItemType10
        from ..models.action_proposal_input_actions_item_type_11 import ActionProposalInputActionsItemType11
        from ..models.action_proposal_input_actions_item_type_12 import ActionProposalInputActionsItemType12

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, ActionProposalInputActionsItemType0):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType1):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType2):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType3):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType4):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType5):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType6):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType7):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType8):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType9):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType10):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType11):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ActionProposalInputActionsItemType12):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        rationale = self.rationale

        idempotency_key = self.idempotency_key

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        target_source = self.target_source.value

        account_id = self.account_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "rationale": rationale,
                "idempotency_key": idempotency_key,
                "evidence": evidence,
                "target_source": target_source,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_proposal_input_actions_item_type_0 import ActionProposalInputActionsItemType0
        from ..models.action_proposal_input_actions_item_type_1 import ActionProposalInputActionsItemType1
        from ..models.action_proposal_input_actions_item_type_2 import ActionProposalInputActionsItemType2
        from ..models.action_proposal_input_actions_item_type_3 import ActionProposalInputActionsItemType3
        from ..models.action_proposal_input_actions_item_type_4 import ActionProposalInputActionsItemType4
        from ..models.action_proposal_input_actions_item_type_5 import ActionProposalInputActionsItemType5
        from ..models.action_proposal_input_actions_item_type_6 import ActionProposalInputActionsItemType6
        from ..models.action_proposal_input_actions_item_type_7 import ActionProposalInputActionsItemType7
        from ..models.action_proposal_input_actions_item_type_8 import ActionProposalInputActionsItemType8
        from ..models.action_proposal_input_actions_item_type_9 import ActionProposalInputActionsItemType9
        from ..models.action_proposal_input_actions_item_type_10 import ActionProposalInputActionsItemType10
        from ..models.action_proposal_input_actions_item_type_11 import ActionProposalInputActionsItemType11
        from ..models.action_proposal_input_actions_item_type_12 import ActionProposalInputActionsItemType12
        from ..models.action_proposal_input_actions_item_type_13 import ActionProposalInputActionsItemType13
        from ..models.action_proposal_input_evidence_item import ActionProposalInputEvidenceItem

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> (
                ActionProposalInputActionsItemType0
                | ActionProposalInputActionsItemType1
                | ActionProposalInputActionsItemType10
                | ActionProposalInputActionsItemType11
                | ActionProposalInputActionsItemType12
                | ActionProposalInputActionsItemType13
                | ActionProposalInputActionsItemType2
                | ActionProposalInputActionsItemType3
                | ActionProposalInputActionsItemType4
                | ActionProposalInputActionsItemType5
                | ActionProposalInputActionsItemType6
                | ActionProposalInputActionsItemType7
                | ActionProposalInputActionsItemType8
                | ActionProposalInputActionsItemType9
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = ActionProposalInputActionsItemType0.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = ActionProposalInputActionsItemType1.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_2 = ActionProposalInputActionsItemType2.from_dict(data)

                    return actions_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_3 = ActionProposalInputActionsItemType3.from_dict(data)

                    return actions_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_4 = ActionProposalInputActionsItemType4.from_dict(data)

                    return actions_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_5 = ActionProposalInputActionsItemType5.from_dict(data)

                    return actions_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_6 = ActionProposalInputActionsItemType6.from_dict(data)

                    return actions_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_7 = ActionProposalInputActionsItemType7.from_dict(data)

                    return actions_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_8 = ActionProposalInputActionsItemType8.from_dict(data)

                    return actions_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_9 = ActionProposalInputActionsItemType9.from_dict(data)

                    return actions_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_10 = ActionProposalInputActionsItemType10.from_dict(data)

                    return actions_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_11 = ActionProposalInputActionsItemType11.from_dict(data)

                    return actions_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_12 = ActionProposalInputActionsItemType12.from_dict(data)

                    return actions_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_13 = ActionProposalInputActionsItemType13.from_dict(data)

                return actions_item_type_13

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        rationale = d.pop("rationale")

        idempotency_key = d.pop("idempotency_key")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = ActionProposalInputEvidenceItem.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        target_source = ActionProposalInputTargetSource(d.pop("target_source"))

        account_id = d.pop("account_id", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        action_proposal_input = cls(
            actions=actions,
            rationale=rationale,
            idempotency_key=idempotency_key,
            evidence=evidence,
            target_source=target_source,
            account_id=account_id,
            workspace_id=workspace_id,
        )

        action_proposal_input.additional_properties = d
        return action_proposal_input

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
