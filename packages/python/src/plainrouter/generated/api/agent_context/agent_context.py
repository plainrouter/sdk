from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_context_auth_error import AgentContextAuthError
from ...models.agent_context_response_200 import AgentContextResponse200
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: int | Unset = UNSET,
    workspace_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["workspace_id"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/context",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentContextAuthError
    | ErrorMessage
    | AgentContextResponse200
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = AgentContextResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400

    if response.status_code == 401:

        def _parse_response_401(data: object) -> AgentContextAuthError | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_0 = AgentContextAuthError.from_dict(data)

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

        def _parse_response_403(data: object) -> AgentContextAuthError | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = AgentContextAuthError.from_dict(data)

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
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
    workspace_id: int | Unset = UNSET,
) -> Response[
    AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError
]:
    """Get agent context

     Read the authenticated agent and authorized account. With no active account, returns null and
    connection next steps.

    Args:
        account_id (int | Unset):
        workspace_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
    workspace_id: int | Unset = UNSET,
) -> (
    AgentContextAuthError
    | ErrorMessage
    | AgentContextResponse200
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """Get agent context

     Read the authenticated agent and authorized account. With no active account, returns null and
    connection next steps.

    Args:
        account_id (int | Unset):
        workspace_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
    workspace_id: int | Unset = UNSET,
) -> Response[
    AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError
]:
    """Get agent context

     Read the authenticated agent and authorized account. With no active account, returns null and
    connection next steps.

    Args:
        account_id (int | Unset):
        workspace_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
    workspace_id: int | Unset = UNSET,
) -> (
    AgentContextAuthError
    | ErrorMessage
    | AgentContextResponse200
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """Get agent context

     Read the authenticated agent and authorized account. With no active account, returns null and
    connection next steps.

    Args:
        account_id (int | Unset):
        workspace_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentContextAuthError | ErrorMessage | AgentContextResponse200 | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            workspace_id=workspace_id,
        )
    ).parsed
