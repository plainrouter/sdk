from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_decision_receipt_read import ActionDecisionReceiptRead
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    action: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/actions/{action}/decision-receipt".format(
            workspace=quote(str(workspace), safe=""),
            action=quote(str(action), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionDecisionReceiptRead | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = ActionDecisionReceiptRead.from_dict(response.json())

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
) -> Response[ActionDecisionReceiptRead | ErrorMessage | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    action: str,
    *,
    client: AuthenticatedClient,
) -> Response[ActionDecisionReceiptRead | ErrorMessage | ValidationError]:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        action (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDecisionReceiptRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    action: str,
    *,
    client: AuthenticatedClient,
) -> ActionDecisionReceiptRead | ErrorMessage | ValidationError | None:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        action (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDecisionReceiptRead | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        action=action,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    action: str,
    *,
    client: AuthenticatedClient,
) -> Response[ActionDecisionReceiptRead | ErrorMessage | ValidationError]:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        action (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDecisionReceiptRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    action: str,
    *,
    client: AuthenticatedClient,
) -> ActionDecisionReceiptRead | ErrorMessage | ValidationError | None:
    """Read Actions data

     Read persisted Actions data for an account available to this workspace key. An unbound key selects
    account_id; a bound key stays limited to its own account.

    Args:
        workspace (int):
        action (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDecisionReceiptRead | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            action=action,
            client=client,
        )
    ).parsed
