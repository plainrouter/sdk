from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ad_test_list_read import AdTestListRead
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/tests".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = AdTestListRead.from_dict(response.json())

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
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
]:
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
]:
    """List Tests and observed conversion event choices

     Lists scoped Tests, their loser pause candidate status and reasons, and observed conversion event
    choices with last-30-day recorded counts.

    Args:
        workspace (int):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestListRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    """List Tests and observed conversion event choices

     Lists scoped Tests, their loser pause candidate status and reasons, and observed conversion event
    choices with last-30-day recorded counts.

    Args:
        workspace (int):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestListRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
]:
    """List Tests and observed conversion event choices

     Lists scoped Tests, their loser pause candidate status and reasons, and observed conversion event
    choices with last-30-day recorded counts.

    Args:
        workspace (int):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestListRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    AdTestListRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    """List Tests and observed conversion event choices

     Lists scoped Tests, their loser pause candidate status and reasons, and observed conversion event
    choices with last-30-day recorded counts.

    Args:
        workspace (int):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestListRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
