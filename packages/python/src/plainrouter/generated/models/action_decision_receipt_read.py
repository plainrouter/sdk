from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_current_disposition import ActionCurrentDisposition
    from ..models.action_decision_receipt_read_chain_entry import ActionDecisionReceiptReadChainEntry
    from ..models.action_decision_receipt_read_document import ActionDecisionReceiptReadDocument


T = TypeVar("T", bound="ActionDecisionReceiptRead")


@_attrs_define
class ActionDecisionReceiptRead:
    """
    Attributes:
        document (ActionDecisionReceiptReadDocument):
        document_sha256 (str):
        chain_entry (ActionDecisionReceiptReadChainEntry):
        disposition (ActionCurrentDisposition):
    """

    document: ActionDecisionReceiptReadDocument
    document_sha256: str
    chain_entry: ActionDecisionReceiptReadChainEntry
    disposition: ActionCurrentDisposition
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document = self.document.to_dict()

        document_sha256 = self.document_sha256

        chain_entry = self.chain_entry.to_dict()

        disposition = self.disposition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
                "document_sha256": document_sha256,
                "chain_entry": chain_entry,
                "disposition": disposition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_current_disposition import ActionCurrentDisposition
        from ..models.action_decision_receipt_read_chain_entry import ActionDecisionReceiptReadChainEntry
        from ..models.action_decision_receipt_read_document import ActionDecisionReceiptReadDocument

        d = dict(src_dict)
        document = ActionDecisionReceiptReadDocument.from_dict(d.pop("document"))

        document_sha256 = d.pop("document_sha256")

        chain_entry = ActionDecisionReceiptReadChainEntry.from_dict(d.pop("chain_entry"))

        disposition = ActionCurrentDisposition.from_dict(d.pop("disposition"))

        action_decision_receipt_read = cls(
            document=document,
            document_sha256=document_sha256,
            chain_entry=chain_entry,
            disposition=disposition,
        )

        action_decision_receipt_read.additional_properties = d
        return action_decision_receipt_read

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
