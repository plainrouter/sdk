from __future__ import annotations

from typing import TypeVar

import httpx
import pytest

from plainrouter import create_client, is_retryable_proposal_error, launch_plans_copy
from plainrouter.generated.api.action_proposal_api import actions_api_propose
from plainrouter.generated.api.deployment_plan import launch_plans_execute
from plainrouter.generated.models import (
    ActionProposalInput,
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
