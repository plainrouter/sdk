from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ad_test_show_read import AdTestShowRead
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...types import Response


def _get_kwargs(
    workspace: int,
    ad_test: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/tests/{ad_test}".format(
            workspace=quote(str(workspace), safe=""),
            ad_test=quote(str(ad_test), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | None:
    if response.status_code == 200:
        response_200 = AdTestShowRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:

        def _parse_response_401(data: object) -> AgentCredentialError | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_0 = AgentCredentialError.from_dict(data)

                return response_401_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_401_type_1 = ErrorMessage.from_dict(data)

            return response_401_type_1

        response_401 = _parse_response_401(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> AgentCredentialError | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = AgentCredentialError.from_dict(data)

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

        def _parse_response_404(data: object) -> ApiRouteNotFound | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = ApiRouteNotFound.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = ErrorMessage.from_dict(data)

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
) -> Response[AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    ad_test: str,
    *,
    client: AuthenticatedClient,
) -> Response[AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage]:
    """Read a Test, verdict, and pause candidates

     Reads a scoped Test, its stored daily facts and verdict, and loser pause candidate status and
    reason; recorded counts rank members only within this Test.

    Args:
        workspace (int):
        ad_test (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        ad_test=ad_test,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    ad_test: str,
    *,
    client: AuthenticatedClient,
) -> AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | None:
    """Read a Test, verdict, and pause candidates

     Reads a scoped Test, its stored daily facts and verdict, and loser pause candidate status and
    reason; recorded counts rank members only within this Test.

    Args:
        workspace (int):
        ad_test (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage
    """

    return sync_detailed(
        workspace=workspace,
        ad_test=ad_test,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    ad_test: str,
    *,
    client: AuthenticatedClient,
) -> Response[AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage]:
    """Read a Test, verdict, and pause candidates

     Reads a scoped Test, its stored daily facts and verdict, and loser pause candidate status and
    reason; recorded counts rank members only within this Test.

    Args:
        workspace (int):
        ad_test (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        ad_test=ad_test,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    ad_test: str,
    *,
    client: AuthenticatedClient,
) -> AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | None:
    """Read a Test, verdict, and pause candidates

     Reads a scoped Test, its stored daily facts and verdict, and loser pause candidate status and
    reason; recorded counts rank members only within this Test.

    Args:
        workspace (int):
        ad_test (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestShowRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            ad_test=ad_test,
            client=client,
        )
    ).parsed
