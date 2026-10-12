from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.launch_creatives_index_response_200 import LaunchCreativesIndexResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    page: int | Unset = 1,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/creatives".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | LaunchCreativesIndexResponse200 | None:
    if response.status_code == 200:
        response_200 = LaunchCreativesIndexResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorMessage | LaunchCreativesIndexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[ErrorMessage | LaunchCreativesIndexResponse200]:
    """List workspace creatives

     Read complete workspace creative rows within the shared MCP byte budget. Continue with next_cursor
    as cursor in the same workspace.

    Args:
        workspace (int):
        page (int | Unset):  Default: 1.
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | LaunchCreativesIndexResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> ErrorMessage | LaunchCreativesIndexResponse200 | None:
    """List workspace creatives

     Read complete workspace creative rows within the shared MCP byte budget. Continue with next_cursor
    as cursor in the same workspace.

    Args:
        workspace (int):
        page (int | Unset):  Default: 1.
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | LaunchCreativesIndexResponse200
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        page=page,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[ErrorMessage | LaunchCreativesIndexResponse200]:
    """List workspace creatives

     Read complete workspace creative rows within the shared MCP byte budget. Continue with next_cursor
    as cursor in the same workspace.

    Args:
        workspace (int):
        page (int | Unset):  Default: 1.
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | LaunchCreativesIndexResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> ErrorMessage | LaunchCreativesIndexResponse200 | None:
    """List workspace creatives

     Read complete workspace creative rows within the shared MCP byte budget. Continue with next_cursor
    as cursor in the same workspace.

    Args:
        workspace (int):
        page (int | Unset):  Default: 1.
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | LaunchCreativesIndexResponse200
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            page=page,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
