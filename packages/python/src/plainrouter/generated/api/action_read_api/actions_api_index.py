from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_list_read import ActionListRead
from ...models.actions_api_index_status import ActionsApiIndexStatus
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["page"] = page

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
) -> ActionListRead | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = ActionListRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())

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
) -> Response[ActionListRead | ErrorMessage | ValidationError]:
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
) -> Response[ActionListRead | ErrorMessage | ValidationError]:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        status=status,
        page=page,
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
) -> ActionListRead | ErrorMessage | ValidationError | None:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListRead | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        status=status,
        page=page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[ActionListRead | ErrorMessage | ValidationError]:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        status=status,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    status: ActionsApiIndexStatus | Unset = UNSET,
    page: int | Unset = UNSET,
) -> ActionListRead | ErrorMessage | ValidationError | None:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        status (ActionsApiIndexStatus | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListRead | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            status=status,
            page=page,
        )
    ).parsed
