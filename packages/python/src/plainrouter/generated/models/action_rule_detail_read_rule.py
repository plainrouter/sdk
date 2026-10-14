from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_rule_detail_read_rule_current_revision import ActionRuleDetailReadRuleCurrentRevision
    from ..models.action_rule_detail_read_rule_revisions_item import ActionRuleDetailReadRuleRevisionsItem
    from ..models.action_rule_detail_read_rule_runs_item import ActionRuleDetailReadRuleRunsItem
    from ..models.action_rule_detail_read_rule_window import ActionRuleDetailReadRuleWindow


T = TypeVar("T", bound="ActionRuleDetailReadRule")


@_attrs_define
class ActionRuleDetailReadRule:
    """
    Attributes:
        id (str):
        workspace_id (int):
        platform_ad_account_id (int):
        name (str):
        enabled (bool):
        suspended_at (datetime.datetime | None):
        suspended_reason (None | str):
        window (ActionRuleDetailReadRuleWindow):
        current_revision (ActionRuleDetailReadRuleCurrentRevision):
        revisions (list[ActionRuleDetailReadRuleRevisionsItem]): Present on show and write responses.
        runs (list[ActionRuleDetailReadRuleRunsItem]): Show only; at most five recent runs, each with at most 100
            decisions.
    """

    id: str
    workspace_id: int
    platform_ad_account_id: int
    name: str
    enabled: bool
    suspended_at: datetime.datetime | None
    suspended_reason: None | str
    window: ActionRuleDetailReadRuleWindow
    current_revision: ActionRuleDetailReadRuleCurrentRevision
    revisions: list[ActionRuleDetailReadRuleRevisionsItem]
    runs: list[ActionRuleDetailReadRuleRunsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        platform_ad_account_id = self.platform_ad_account_id

        name = self.name

        enabled = self.enabled

        suspended_at: None | str
        if isinstance(self.suspended_at, datetime.datetime):
            suspended_at = self.suspended_at.isoformat()
        else:
            suspended_at = self.suspended_at

        suspended_reason: None | str
        suspended_reason = self.suspended_reason

        window = self.window.to_dict()

        current_revision = self.current_revision.to_dict()

        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "platform_ad_account_id": platform_ad_account_id,
                "name": name,
                "enabled": enabled,
                "suspended_at": suspended_at,
                "suspended_reason": suspended_reason,
                "window": window,
                "current_revision": current_revision,
                "revisions": revisions,
                "runs": runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_rule_detail_read_rule_current_revision import ActionRuleDetailReadRuleCurrentRevision
        from ..models.action_rule_detail_read_rule_revisions_item import ActionRuleDetailReadRuleRevisionsItem
        from ..models.action_rule_detail_read_rule_runs_item import ActionRuleDetailReadRuleRunsItem
        from ..models.action_rule_detail_read_rule_window import ActionRuleDetailReadRuleWindow

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        def _parse_suspended_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_at_type_0 = datetime.datetime.fromisoformat(data)

                return suspended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        suspended_at = _parse_suspended_at(d.pop("suspended_at"))

        def _parse_suspended_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        suspended_reason = _parse_suspended_reason(d.pop("suspended_reason"))

        window = ActionRuleDetailReadRuleWindow.from_dict(d.pop("window"))

        current_revision = ActionRuleDetailReadRuleCurrentRevision.from_dict(d.pop("current_revision"))

        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = ActionRuleDetailReadRuleRevisionsItem.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        runs = []
        _runs = d.pop("runs")
        for runs_item_data in _runs:
            runs_item = ActionRuleDetailReadRuleRunsItem.from_dict(runs_item_data)

            runs.append(runs_item)

        action_rule_detail_read_rule = cls(
            id=id,
            workspace_id=workspace_id,
            platform_ad_account_id=platform_ad_account_id,
            name=name,
            enabled=enabled,
            suspended_at=suspended_at,
            suspended_reason=suspended_reason,
            window=window,
            current_revision=current_revision,
            revisions=revisions,
            runs=runs,
        )

        action_rule_detail_read_rule.additional_properties = d
        return action_rule_detail_read_rule

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
