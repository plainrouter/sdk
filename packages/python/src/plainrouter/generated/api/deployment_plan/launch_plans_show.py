from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_plans_show_response_200 import LaunchPlansShowResponse200
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    deployment_plan: str,
    *,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 5,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/plans/{deployment_plan}".format(
            workspace=quote(str(workspace), safe=""),
            deployment_plan=quote(str(deployment_plan), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchPlansShowResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError]:
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
    cursor: int | Unset = UNSET,
    limit: int | Unset = 5,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError]:
    """Read a deployment plan

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        deployment_plan (str):
        cursor (int | Unset):
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
        cursor=cursor,
        limit=limit,
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
    cursor: int | Unset = UNSET,
    limit: int | Unset = 5,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError | None:
    """Read a deployment plan

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        deployment_plan (str):
        cursor (int | Unset):
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        deployment_plan=deployment_plan,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 5,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError]:
    """Read a deployment plan

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        deployment_plan (str):
        cursor (int | Unset):
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 5,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError | None:
    """Read a deployment plan

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        deployment_plan (str):
        cursor (int | Unset):
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansShowResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
