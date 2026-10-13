"""Copy facade retaining generated transport settings and decoding known retry codes."""

from http import HTTPStatus

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


def _build_response(client: AuthenticatedClient, response: httpx.Response) -> Response[PlanCopyResponse]:
    parsed: PlanCopyResponse | None
    if response.status_code == 503:
        data = response.json()
        error = data.get("error") if isinstance(data, dict) else None
        if isinstance(error, dict) and error.get("code") == "proposal_not_recorded":
            parsed = ProposalUnavailable.from_dict(data)
        else:
            parsed = generated_copy._parse_response(client=client, response=response)
    else:
        parsed = generated_copy._parse_response(client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> Response[PlanCopyResponse]:
    """Copy a failed plan; retain WorkspaceLockTimeout and recognize proposal_not_recorded."""
    response = client.get_httpx_client().request(
        **generated_copy._get_kwargs(workspace=workspace, deployment_plan=deployment_plan)
    )
    return _build_response(client, response)


def sync(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> PlanCopyResponse | None:
    return sync_detailed(workspace, deployment_plan, client=client).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[PlanCopyResponse]:
    """Copy asynchronously with the same retry decoding and unchanged generated request."""
    response = await client.get_async_httpx_client().request(
        **generated_copy._get_kwargs(workspace=workspace, deployment_plan=deployment_plan)
    )
    return _build_response(client, response)


async def asyncio(workspace: int, deployment_plan: str, *, client: AuthenticatedClient) -> PlanCopyResponse | None:
    return (await asyncio_detailed(workspace, deployment_plan, client=client)).parsed
