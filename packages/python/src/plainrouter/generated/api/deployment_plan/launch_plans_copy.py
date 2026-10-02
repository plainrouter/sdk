from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.plan_copy_error import PlanCopyError
from ...models.plan_copy_read import PlanCopyRead
from ...types import Response


def _get_kwargs(
    workspace: int,
    deployment_plan: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/admin/plans/{deployment_plan}/copy".format(
            workspace=quote(str(workspace), safe=""),
            deployment_plan=quote(str(deployment_plan), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | PlanCopyError | PlanCopyRead | None:
    if response.status_code == 201:
        response_201 = PlanCopyRead.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PlanCopyError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PlanCopyError.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PlanCopyError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorMessage | PlanCopyError | PlanCopyRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorMessage | PlanCopyError | PlanCopyRead]:
    """Copy a failed plan to a new draft

     Copy failed plan content and stored integer budgets into a fresh draft. History stays unchanged;
    validate budgets and submit again with a new intent.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PlanCopyError | PlanCopyRead]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> ErrorMessage | PlanCopyError | PlanCopyRead | None:
    """Copy a failed plan to a new draft

     Copy failed plan content and stored integer budgets into a fresh draft. History stays unchanged;
    validate budgets and submit again with a new intent.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PlanCopyError | PlanCopyRead
    """

    return sync_detailed(
        workspace=workspace,
        deployment_plan=deployment_plan,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorMessage | PlanCopyError | PlanCopyRead]:
    """Copy a failed plan to a new draft

     Copy failed plan content and stored integer budgets into a fresh draft. History stays unchanged;
    validate budgets and submit again with a new intent.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PlanCopyError | PlanCopyRead]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> ErrorMessage | PlanCopyError | PlanCopyRead | None:
    """Copy a failed plan to a new draft

     Copy failed plan content and stored integer budgets into a fresh draft. History stays unchanged;
    validate budgets and submit again with a new intent.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PlanCopyError | PlanCopyRead
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
        )
    ).parsed
