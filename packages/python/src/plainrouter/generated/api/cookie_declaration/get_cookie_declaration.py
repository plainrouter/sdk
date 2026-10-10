from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.cookie_declaration import CookieDeclaration
from ...models.error_message import ErrorMessage
from ...types import Response


def _get_kwargs(
    publishable_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cookie-declarations/{publishable_key}".format(
            publishable_key=quote(str(publishable_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage | None:
    if response.status_code == 200:
        response_200 = CookieDeclaration.from_dict(response.json())

        return response_200

    if response.status_code == 404:

        def _parse_response_404(data: object) -> ApiRouteNotFound | list[str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_404_type_0 = cast(list[str], data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = ApiRouteNotFound.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publishable_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage]:
    """Read the public cookie declaration

     Public on every plan. Returns latest completed scan metadata, never values. Invalid keys return 404
    before the 300/minute per-key limiter.

    Args:
        publishable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage]
    """

    kwargs = _get_kwargs(
        publishable_key=publishable_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publishable_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage | None:
    """Read the public cookie declaration

     Public on every plan. Returns latest completed scan metadata, never values. Invalid keys return 404
    before the 300/minute per-key limiter.

    Args:
        publishable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage
    """

    return sync_detailed(
        publishable_key=publishable_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    publishable_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage]:
    """Read the public cookie declaration

     Public on every plan. Returns latest completed scan metadata, never values. Invalid keys return 404
    before the 300/minute per-key limiter.

    Args:
        publishable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage]
    """

    kwargs = _get_kwargs(
        publishable_key=publishable_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publishable_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage | None:
    """Read the public cookie declaration

     Public on every plan. Returns latest completed scan metadata, never values. Invalid keys return 404
    before the 300/minute per-key limiter.

    Args:
        publishable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | list[str] | CookieDeclaration | ErrorMessage
    """

    return (
        await asyncio_detailed(
            publishable_key=publishable_key,
            client=client,
        )
    ).parsed
