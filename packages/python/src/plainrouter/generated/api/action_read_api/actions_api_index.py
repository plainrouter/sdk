from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_list_read import ActionListRead
from ...models.actions_api_index_status import ActionsApiIndexStatus
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["page"] = page

    params["account_id"] = account_id

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/actions".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActionListRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ActionListRead.from_dict(response.json())

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
        response_403 = AgentCredentialError.from_dict(response.json())

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
) -> Response[
    ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
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
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[
    ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
]:
    """List actions

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):
        account_id (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        status=status,
        page=page,
        account_id=account_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> (
    ActionListRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    """List actions

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):
        account_id (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        status=status,
        page=page,
        account_id=account_id,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[
    ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
]:
    """List actions

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):
        account_id (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        status=status,
        page=page,
        account_id=account_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> (
    ActionListRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    """List actions

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):
        account_id (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            status=status,
            page=page,
            account_id=account_id,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
