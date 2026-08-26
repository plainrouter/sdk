from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.list_events_by_cursor_response_200 import ListEventsByCursorResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dashboard/events/cursor",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | ListEventsByCursorResponse200 | None:
    if response.status_code == 200:
        response_200 = ListEventsByCursorResponse200.from_dict(response.json())

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
) -> Response[ErrorMessage | ListEventsByCursorResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> Response[ErrorMessage | ListEventsByCursorResponse200]:
    """List recent events by cursor

     Returns retained customer-readable events using stable cursor pagination and aggregate destination-
    delivery acceptance metrics.

    Args:
        per_page (int | Unset):  Default: 25.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ListEventsByCursorResponse200]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> ErrorMessage | ListEventsByCursorResponse200 | None:
    """List recent events by cursor

     Returns retained customer-readable events using stable cursor pagination and aggregate destination-
    delivery acceptance metrics.

    Args:
        per_page (int | Unset):  Default: 25.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ListEventsByCursorResponse200
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> Response[ErrorMessage | ListEventsByCursorResponse200]:
    """List recent events by cursor

     Returns retained customer-readable events using stable cursor pagination and aggregate destination-
    delivery acceptance metrics.

    Args:
        per_page (int | Unset):  Default: 25.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ListEventsByCursorResponse200]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 25,
    cursor: str | Unset = UNSET,
) -> ErrorMessage | ListEventsByCursorResponse200 | None:
    """List recent events by cursor

     Returns retained customer-readable events using stable cursor pagination and aggregate destination-
    delivery acceptance metrics.

    Args:
        per_page (int | Unset):  Default: 25.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ListEventsByCursorResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            cursor=cursor,
        )
    ).parsed
