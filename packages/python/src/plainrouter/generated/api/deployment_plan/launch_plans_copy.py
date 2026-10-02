from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.plan_copy_forbidden import PlanCopyForbidden
from ...models.plan_copy_not_found import PlanCopyNotFound
from ...models.plan_copy_read import PlanCopyRead
from ...models.plan_copy_rejected import PlanCopyRejected
from ...models.workspace_lock_timeout import WorkspaceLockTimeout
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
) -> (
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
    | None
):
    if response.status_code == 201:
        response_201 = PlanCopyRead.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> ErrorMessage | PlanCopyForbidden:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = PlanCopyForbidden.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = ErrorMessage.from_dict(data)

            return response_403_type_1

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:

        def _parse_response_404(data: object) -> ApiRouteNotFound | PlanCopyNotFound:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = PlanCopyNotFound.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = ApiRouteNotFound.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = ErrorMessage.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = PlanCopyRejected.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = WorkspaceLockTimeout.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
]:
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
) -> Response[
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
]:
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
        Response[ApiRouteNotFound | PlanCopyNotFound | ErrorMessage | ErrorMessage | PlanCopyForbidden | PlanCopyRead | PlanCopyRejected | WorkspaceLockTimeout]
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
) -> (
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
    | None
):
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
        ApiRouteNotFound | PlanCopyNotFound | ErrorMessage | ErrorMessage | PlanCopyForbidden | PlanCopyRead | PlanCopyRejected | WorkspaceLockTimeout
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
) -> Response[
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
]:
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
        Response[ApiRouteNotFound | PlanCopyNotFound | ErrorMessage | ErrorMessage | PlanCopyForbidden | PlanCopyRead | PlanCopyRejected | WorkspaceLockTimeout]
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
) -> (
    ApiRouteNotFound
    | PlanCopyNotFound
    | ErrorMessage
    | ErrorMessage
    | PlanCopyForbidden
    | PlanCopyRead
    | PlanCopyRejected
    | WorkspaceLockTimeout
    | None
):
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
        ApiRouteNotFound | PlanCopyNotFound | ErrorMessage | ErrorMessage | PlanCopyForbidden | PlanCopyRead | PlanCopyRejected | WorkspaceLockTimeout
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
        )
    ).parsed
