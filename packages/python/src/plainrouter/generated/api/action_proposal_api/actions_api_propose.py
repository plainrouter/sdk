from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_proposal_input import ActionProposalInput
from ...models.action_proposal_read import ActionProposalRead
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    *,
    body: ActionProposalInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agent/workspaces/{workspace}/actions".format(
            workspace=quote(str(workspace), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionProposalRead | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = ActionProposalRead.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ActionProposalRead.from_dict(response.json())

        return response_201

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
) -> Response[ActionProposalRead | ErrorMessage | ValidationError]:
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
    body: ActionProposalInput,
) -> Response[ActionProposalRead | ErrorMessage | ValidationError]:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionProposalRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient,
    body: ActionProposalInput,
) -> ActionProposalRead | ErrorMessage | ValidationError | None:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionProposalRead | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    body: ActionProposalInput,
) -> Response[ActionProposalRead | ErrorMessage | ValidationError]:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionProposalRead | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    body: ActionProposalInput,
) -> ActionProposalRead | ErrorMessage | ValidationError | None:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionProposalRead | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
