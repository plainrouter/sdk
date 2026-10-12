from __future__ import annotations

from typing import TypeVar

import httpx
import pytest

from plainrouter import create_client, is_retryable_proposal_error
from plainrouter.generated.api.action_proposal_api import actions_api_propose
from plainrouter.generated.api.deployment_plan import launch_plans_execute
from plainrouter.generated.models import (
    ActionProposalInput,
    ActionProposalInputTargetSource,
    ExecuteDeploymentPlanRequest,
    ProposalUnavailable,
    ProposalUnavailableErrorCode,
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
