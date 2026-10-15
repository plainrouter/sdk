from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any, TypeVar

import httpx
import pytest

from plainrouter import create_client, is_retryable_proposal_error, launch_plans_copy
from plainrouter.closed_objects import ClosedRequestKeyError
from plainrouter.generated.api.action_proposal_api import actions_api_propose
from plainrouter.generated.api.action_rule_api import actions_rules_store
from plainrouter.generated.api.deployment_plan import launch_plans_execute
from plainrouter.generated.client import AuthenticatedClient as GeneratedAuthenticatedClient
from plainrouter.generated.client import Client as GeneratedClient
from plainrouter.generated.models import (
    ActionProposalInput,
    ActionProposalInputActionsItemType0Params,
    ActionProposalInputActionsItemType2Params,
    ActionProposalInputActionsItemType12Params,
    ActionProposalInputActionsItemType12ParamsStatus,
    ActionProposalInputActionsItemType13Params,
    ActionProposalInputActionsItemType13ParamsStatus,
    ActionProposalInputEvidenceItem,
    ActionProposalInputEvidenceItemSourceTool,
    ActionProposalInputTargetSource,
    ExecuteDeploymentPlanRequest,
    ProposalUnavailable,
    ProposalUnavailableErrorCode,
    WorkspaceLockTimeout,
)
from plainrouter.generated.types import Response

T = TypeVar("T")


@pytest.mark.parametrize("code", ["proposal_not_recorded", "workspace_lock_timeout"])
@pytest.mark.parametrize("operation", ["propose", "execute"])
@pytest.mark.asyncio
async def test_proposal_refusal_is_typed_retryable_and_retains_retry_after(code: str, operation: str) -> None:
    requests: list[httpx.Request] = []
    envelope = {"error": {"code": code, "message": "Retry the proposal."}}

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(503, json=envelope, headers={"Retry-After": "1"})

    client = create_client("proposal-test-token", base_url="https://example.test/api/v1")
    transport = httpx.MockTransport(handle)
    client.set_httpx_client(httpx.Client(transport=transport, base_url="https://example.test/api/v1"))
    client.set_async_httpx_client(httpx.AsyncClient(transport=transport, base_url="https://example.test/api/v1"))
    if operation == "propose":
        proposal = ActionProposalInput(
            actions=[],
            evidence=[],
            rationale="Pause the ad.",
            idempotency_key="retry-test",
            target_source=ActionProposalInputTargetSource.HUMAN_SUPPLIED,
        )
        proposal_responses = [
            actions_api_propose.sync_detailed(1, client=client, body=proposal),
            await actions_api_propose.asyncio_detailed(1, client=client, body=proposal),
        ]
        for response in proposal_responses:
            assert_refusal(response, code, envelope)
        if code == "proposal_not_recorded":
            await _assert_closed_request_behavior()
    else:
        plan = ExecuteDeploymentPlanRequest(review_version="review-test")
        plan_responses = [
            launch_plans_execute.sync_detailed(1, "plan-test", client=client, body=plan),
            await launch_plans_execute.asyncio_detailed(1, "plan-test", client=client, body=plan),
        ]
        for plan_response in plan_responses:
            assert_refusal(plan_response, code, envelope)
    assert len(requests) == 2
    await client.get_async_httpx_client().aclose()
    client.get_httpx_client().close()


def assert_refusal(response: Response[T], code: str, envelope: dict[str, dict[str, str]]) -> None:
    assert response.status_code == 503
    assert isinstance(response.parsed, ProposalUnavailable)
    assert response.parsed.error.code == ProposalUnavailableErrorCode(code)
    assert response.parsed.to_dict() == envelope
    assert response.headers["Retry-After"] == "1"
    assert is_retryable_proposal_error(response.status_code, response.parsed)


def test_unrelated_errors_are_not_retryable_proposal_refusals() -> None:
    error = ProposalUnavailable.from_dict({"error": {"code": "proposal_not_recorded", "message": "Retry."}})
    assert not is_retryable_proposal_error(422, error)
    assert not is_retryable_proposal_error(503, {"error": {"code": "proposal_not_recorded", "message": "Retry."}})


@pytest.mark.parametrize("code", ["workspace_lock_timeout", "proposal_not_recorded"])
@pytest.mark.parametrize("retry_after", ["1", "Wed, 14 Oct 2026 12:00:00 GMT", None])
@pytest.mark.asyncio
async def test_copy_classifies_both_codes_and_preserves_retry_after(code: str, retry_after: str | None) -> None:
    envelope = {"error": {"code": code, "message": "Retry the proposal."}}
    calls: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        assert request.method == "POST"
        assert request.url.path == "/api/v1/workspaces/1/admin/plans/failed-plan/copy"
        assert request.headers["Authorization"] == "Bearer proposal-test-token"
        assert request.read() == b""
        return httpx.Response(503, json=envelope, headers={} if retry_after is None else {"Retry-After": retry_after})

    client = create_client("proposal-test-token", base_url="https://example.test/api/v1")
    transport = httpx.MockTransport(handle)
    client.set_httpx_client(
        httpx.Client(
            transport=transport,
            base_url="https://example.test/api/v1",
            headers={"Authorization": "Bearer proposal-test-token"},
        )
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(
            transport=transport,
            base_url="https://example.test/api/v1",
            headers={"Authorization": "Bearer proposal-test-token"},
        )
    )
    responses = [
        launch_plans_copy.sync_detailed(1, "failed-plan", client=client),
        await launch_plans_copy.asyncio_detailed(1, "failed-plan", client=client),
    ]
    for response in responses:
        assert response.status_code == 503
        assert isinstance(
            response.parsed, WorkspaceLockTimeout if code == "workspace_lock_timeout" else ProposalUnavailable
        )
        assert response.parsed.to_dict() == envelope
        assert response.headers.get("Retry-After") == retry_after
        assert is_retryable_proposal_error(response.status_code, response.parsed)
    assert len(calls) == 2
    client.get_httpx_client().close()
    await client.get_async_httpx_client().aclose()


@pytest.mark.parametrize("code", ["workspace_lock_timeout", "proposal_not_recorded"])
def test_undocumented_503_is_retryable_from_response_or_raw_body(code: str) -> None:
    from plainrouter.generated.api.creative import store_creative_from_url
    from plainrouter.generated.models import StoreCreativeFromUrlBody

    envelope = {"error": {"code": code, "message": "Retry."}}
    client = create_client("test-token", base_url="https://example.test/api/v1")
    client.set_httpx_client(
        httpx.Client(
            base_url="https://example.test/api/v1",
            transport=httpx.MockTransport(
                lambda request: httpx.Response(503, json=envelope, headers={"Retry-After": "1"})
            ),
        )
    )
    response = store_creative_from_url.sync_detailed(
        1, client=client, body=StoreCreativeFromUrlBody(url="https://example.test/a.jpg")
    )
    assert response.parsed is None
    assert is_retryable_proposal_error(response.status_code, response)
    assert is_retryable_proposal_error(response.status_code, response.content)
    assert response.headers["Retry-After"] == "1"
    client.get_httpx_client().close()


@pytest.mark.parametrize("body", [b"[" * 5000 + b"0" + b"]" * 5000, b"\xff", b"<html>503</html>", b"", b"null"])
def test_retry_helper_never_raises_on_malformed_body(body: bytes) -> None:
    assert is_retryable_proposal_error(503, body) is False


def test_retry_helper_never_raises_from_unread_response_or_model_adapter() -> None:
    class BrokenModel:
        def to_dict(self) -> object:
            raise RecursionError("nested model")

    assert is_retryable_proposal_error(503, BrokenModel()) is False
    response = httpx.Response(503, stream=httpx.ByteStream(b"nested"))
    assert is_retryable_proposal_error(503, response) is False




async def _assert_closed_request_behavior() -> None:
    model_cases: list[tuple[type[Any], dict[str, Any], dict[str, Any], str, str]] = [
        (
            ActionProposalInputActionsItemType0Params,
            {"new_daily_budget_minor": 100},
            {"new_daily_budget_minor": 100},
            "new_daily_budge_minor",
            "New_daily_budget_minor",
        ),
        (
            ActionProposalInputActionsItemType12Params,
            {"status": "paused"},
            {"status": ActionProposalInputActionsItemType12ParamsStatus.PAUSED},
            "state",
            "Status",
        ),
        (
            ActionProposalInputActionsItemType13Params,
            {"asset_id": "asset-1", "status": "paused", "name_suffix": " Copy"},
            {
                "asset_id": "asset-1",
                "status": ActionProposalInputActionsItemType13ParamsStatus.PAUSED,
                "name_suffix": " Copy",
            },
            "asset_idd",
            "Asset_id",
        ),
        (
            ActionProposalInputEvidenceItem,
            {"source_tool": "get_performance", "fields_used": ["clicks"], "action_index": 0},
            {
                "source_tool": ActionProposalInputEvidenceItemSourceTool.GET_PERFORMANCE,
                "fields_used": ["clicks"],
                "action_index": 0,
            },
            "field_used",
            "Fields_used",
        ),
    ]
    for model, mapping, constructor_values, misspelling, case_variant in model_cases:
        assert model.from_dict(mapping).to_dict() == mapping
        for unknown_key in (misspelling, case_variant):
            with pytest.raises(ClosedRequestKeyError) as converter_error:
                model.from_dict({**mapping, unknown_key: "unexpected"})
            assert unknown_key in str(converter_error.value)
            assert model.__name__ in str(converter_error.value)

        assert model(**constructor_values).to_dict() == constructor_values
        for unknown_key in (misspelling, case_variant):
            with pytest.raises(TypeError) as constructor_error:
                model(**{**constructor_values, unknown_key: "unexpected"})
            assert unknown_key in str(constructor_error.value)
            assert model.__name__ in str(constructor_error.value)

    assert ActionProposalInputActionsItemType2Params.from_dict({}).to_dict() == {}
    with pytest.raises(ClosedRequestKeyError, match="budget_change_percent") as nested_error:
        ActionProposalInput.from_dict(
            {
                "actions": [
                    {
                        "type": "pause",
                        "target_entity": {"type": "ad", "id": "ad-1"},
                        "params": {"budget_change_percent": 10},
                        "rationale": "Pause this ad.",
                    }
                ],
                "evidence": [],
                "rationale": "Pause this ad.",
                "idempotency_key": "unknown-key-test",
                "target_source": "human_supplied",
            }
        )
    assert "ActionProposalInputActionsItemType2Params" in str(nested_error.value)

    action_samples: list[tuple[str, dict[str, Any], str, str, str, str]] = [
        (
            "increase_budget",
            {"new_daily_budget_minor": 100},
            "new_daily_budge_minor",
            "New_daily_budget_minor",
            "ActionProposalInput.actions[].params",
            "ActionProposalInputActionsItemType0Params",
        ),
        (
            "set_status",
            {"status": "paused"},
            "state",
            "Status",
            "ActionProposalInput.actions[].params",
            "ActionProposalInputActionsItemType12Params",
        ),
        (
            "duplicate_ad_with_creative",
            {"asset_id": "asset-1", "status": "paused", "name_suffix": " Copy"},
            "asset_idd",
            "Asset_id",
            "ActionProposalInput.actions[].params",
            "ActionProposalInputActionsItemType13Params",
        ),
    ]
    invalid_bodies: list[tuple[str, dict[str, Any], str, str]] = []
    for action_type, params, misspelling, case_variant, request_object, model_name in action_samples:
        for unknown_key in (misspelling, case_variant):
            invalid_bodies.append(
                (
                    unknown_key,
                    {
                        "actions": [
                            {
                                "type": action_type,
                                "target_entity": {"type": "ad", "id": "ad-1"},
                                "params": {**params, unknown_key: "unexpected"},
                                "rationale": "Change this ad.",
                            }
                        ],
                        "evidence": [],
                        "rationale": "Change this ad.",
                        "idempotency_key": "unknown-key-test",
                        "target_source": "human_supplied",
                    },
                    request_object,
                    model_name,
                )
            )

    evidence = {"source_tool": "get_performance", "fields_used": ["clicks"], "action_index": 0}
    for unknown_key in ("field_used", "Fields_used"):
        invalid_bodies.append(
            (
                unknown_key,
                {
                    "actions": [],
                    "evidence": [{**evidence, unknown_key: "unexpected"}],
                    "rationale": "Check evidence.",
                    "idempotency_key": "unknown-key-test",
                    "target_source": "human_supplied",
                },
                "ActionProposalInput.evidence[]",
                "ActionProposalInputEvidenceItem",
            )
        )

    for unknown_key, body, request_object, model_name in invalid_bodies:
        with pytest.raises(ClosedRequestKeyError) as converter_error:
            ActionProposalInput.from_dict(body)
        assert unknown_key in str(converter_error.value)
        assert model_name in str(converter_error.value)

    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    transport = httpx.MockTransport(handle)
    url = "https://example.test/api/v1/agent/workspaces/1/actions"
    curated = create_client("test-token", base_url="https://example.test/api/v1")
    curated.set_httpx_client(httpx.Client(transport=transport))
    curated.set_async_httpx_client(httpx.AsyncClient(transport=transport))
    generated_clients = (
        GeneratedClient(base_url="https://example.test/api/v1", httpx_args={"transport": transport}),
        GeneratedAuthenticatedClient(
            base_url="https://example.test/api/v1", token="test-token", httpx_args={"transport": transport}
        ),
    )

    async def async_body(request_content: bytes) -> AsyncIterator[bytes]:
        yield request_content

    try:
        for unknown_key, body, request_object, _ in invalid_bodies:
            with pytest.raises(ClosedRequestKeyError) as operation_error:
                actions_api_propose.sync_detailed(1, client=curated, body=body)  # type: ignore[arg-type]
            assert unknown_key in str(operation_error.value)
            assert request_object in str(operation_error.value)

            body_content = json.dumps(body).encode()
            request_clients = (curated, *generated_clients)
            for request_client in request_clients:
                with pytest.raises(ClosedRequestKeyError) as sync_error:
                    request_client.get_httpx_client().post(
                        url, content=iter([body_content]), headers={"Content-Type": "application/json"}
                    )
                assert unknown_key in str(sync_error.value)
                assert request_object in str(sync_error.value)

                with pytest.raises(ClosedRequestKeyError) as async_error:
                    await request_client.get_async_httpx_client().post(
                        url, content=async_body(body_content), headers={"Content-Type": "application/json"}
                    )
                assert unknown_key in str(async_error.value)
                assert request_object in str(async_error.value)

        rule_body = {
            "name": "Pause low performers",
            "platform_ad_account_id": 1,
            "definition": {
                "target_level": "ad_set",
                "action": "pause",
                "minimum_counted_arrivals": 10,
                "cost_comparison": "at_least",
                "cost_ratio": 1.5,
                "budget_change_percent": 5,
            },
        }
        with pytest.raises(ClosedRequestKeyError, match="budget_change_percent"):
            actions_rules_store._get_kwargs(1, body=rule_body)  # type: ignore[arg-type]
        assert requests == []

        documented_body = ActionProposalInput.from_dict(
            {
                "actions": [
                    {
                        "type": "set_status",
                        "target_entity": {"type": "ad", "id": "ad-1"},
                        "params": {"status": "paused"},
                        "rationale": "Pause this ad.",
                    }
                ],
                "evidence": [],
                "rationale": "Pause the ad.",
                "idempotency_key": "documented-key-test",
                "target_source": "human_supplied",
            }
        )
        kwargs = actions_api_propose._get_kwargs(1, body=documented_body)
        assert kwargs["json"]["actions"][0]["params"] == {"status": "paused"}

        open_body = ActionProposalInput.from_dict(
            {
                "actions": [],
                "evidence": [],
                "rationale": "Keep open fields.",
                "idempotency_key": "open-body-test",
                "target_source": "human_supplied",
                "future_open_key": "retained",
            }
        )
        open_kwargs = actions_api_propose._get_kwargs(1, body=open_body)
        assert open_kwargs["json"]["future_open_key"] == "retained"
    finally:
        curated.get_httpx_client().close()
        await curated.get_async_httpx_client().aclose()
        for generated in generated_clients:
            generated.get_httpx_client().close()
            await generated.get_async_httpx_client().aclose()
