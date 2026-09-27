from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_api_propose_body_target_source import ActionsApiProposeBodyTargetSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actions_api_propose_body_evidence_item import ActionsApiProposeBodyEvidenceItem


T = TypeVar("T", bound="ActionsApiProposeBody")


@_attrs_define
class ActionsApiProposeBody:
    """
    Attributes:
        actions (list[str]):
        rationale (str):
        idempotency_key (str):
        evidence (list[ActionsApiProposeBodyEvidenceItem]):
        target_source (ActionsApiProposeBodyTargetSource):
        account_id (int | Unset):
    """

    actions: list[str]
    rationale: str
    idempotency_key: str
    evidence: list[ActionsApiProposeBodyEvidenceItem]
    target_source: ActionsApiProposeBodyTargetSource
    account_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = self.actions

        rationale = self.rationale

        idempotency_key = self.idempotency_key

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        target_source = self.target_source.value

        account_id = self.account_id

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actions_api_propose_body_evidence_item import ActionsApiProposeBodyEvidenceItem

        d = dict(src_dict)
        actions = cast(list[str], d.pop("actions"))

        rationale = d.pop("rationale")

        idempotency_key = d.pop("idempotency_key")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = ActionsApiProposeBodyEvidenceItem.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        target_source = ActionsApiProposeBodyTargetSource(d.pop("target_source"))

        account_id = d.pop("account_id", UNSET)

        actions_api_propose_body = cls(
            actions=actions,
            rationale=rationale,
            idempotency_key=idempotency_key,
            evidence=evidence,
            target_source=target_source,
            account_id=account_id,
        )

        actions_api_propose_body.additional_properties = d
        return actions_api_propose_body

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
