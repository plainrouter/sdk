from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_plans_index_response_200 import LaunchPlansIndexResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/plans".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200 | None:
    if response.status_code == 200:
        response_200 = LaunchPlansIndexResponse200.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 25,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200]:
    """List deployment plans

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 25,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200 | None:
    """List deployment plans

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 25,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200]:
    """List deployment plans

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 25,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200 | None:
    """List deployment plans

     Read plans for the approved ad account with their current review_version. Pass the version from the
    plan you reviewed when executing.

    Args:
        workspace (int):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansIndexResponse200
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            per_page=per_page,
        )
    ).parsed
