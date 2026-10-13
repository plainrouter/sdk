"""Copy facade retaining generated transport settings and decoding known retry codes."""

from http import HTTPStatus
from typing import Any, cast

import httpx

from .generated import AuthenticatedClient
from .generated.api.deployment_plan import launch_plans_copy as generated_copy
from .generated.models import (
    ApiRouteNotFound,
    ErrorMessage,
    PlanCopyForbidden,
    PlanCopyNotFound,
    PlanCopyRead,
    PlanCopyRejected,
    ProposalUnavailable,
    WorkspaceLockTimeout,
)
from .generated.types import Response
from .proposal_errors import is_retryable_proposal_error

PlanCopyResponse = (
    ApiRouteNotFound
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyNotFound
    | PlanCopyRead
    | PlanCopyRejected
    | ProposalUnavailable
    | WorkspaceLockTimeout
)


class _RecordingClient:
    """Forward the generated client's calls without changing the caller's HTTP clients."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self.client = client
        self.response: httpx.Response | None = None

    def __getattr__(self, name: str) -> Any:
        return getattr(self.client, name)

    def get_httpx_client(self) -> httpx.Client:
        return cast(httpx.Client, _SyncRecorder(self))

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        return cast(httpx.AsyncClient, _AsyncRecorder(self))


class _SyncRecorder:
    def __init__(self, recorder: _RecordingClient) -> None:
        self.recorder = recorder

    def request(self, *args: Any, **kwargs: Any) -> httpx.Response:
        response = self.recorder.client.get_httpx_client().request(*args, **kwargs)
        self.recorder.response = response
        return response


class _AsyncRecorder:
    def __init__(self, recorder: _RecordingClient) -> None:
        self.recorder = recorder

    async def request(self, *args: Any, **kwargs: Any) -> httpx.Response:
        response = await self.recorder.client.get_async_httpx_client().request(*args, **kwargs)
        self.recorder.response = response
        return response


def _retry_response(response: httpx.Response | None) -> Response[PlanCopyResponse] | None:
    if response is None or not is_retryable_proposal_error(response.status_code, response):
        return None
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=ProposalUnavailable.from_dict(response.json()),
    )


def sync_detailed(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> Response[PlanCopyResponse]:
    """Delegate copy and only recover a known retry envelope rejected by the generated parser."""
    recorder = _RecordingClient(client)
    try:
        result = generated_copy.sync_detailed(workspace, deployment_plan, client=cast(AuthenticatedClient, recorder))
    except ValueError:
        recovered = _retry_response(recorder.response)
        if recovered is None:
            raise
        return recovered
    return cast(Response[PlanCopyResponse], result)


def sync(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> PlanCopyResponse | None:
    return sync_detailed(workspace, deployment_plan, client=client).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[PlanCopyResponse]:
    """Delegate asynchronous copy; preserve every failure outside the known retry envelope."""
    recorder = _RecordingClient(client)
    try:
        result = await generated_copy.asyncio_detailed(
            workspace, deployment_plan, client=cast(AuthenticatedClient, recorder)
        )
    except ValueError:
        recovered = _retry_response(recorder.response)
        if recovered is None:
            raise
        return recovered
    return cast(Response[PlanCopyResponse], result)


async def asyncio(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> PlanCopyResponse | None:
    return (await asyncio_detailed(workspace, deployment_plan, client=client)).parsed
