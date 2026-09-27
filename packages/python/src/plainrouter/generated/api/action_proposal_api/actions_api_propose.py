from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_api_propose_body import ActionsApiProposeBody
from ...models.actions_api_propose_response_200 import ActionsApiProposeResponse200
from ...models.actions_api_propose_response_201 import ActionsApiProposeResponse201
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    *,
    body: ActionsApiProposeBody,
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
) -> ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = ActionsApiProposeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ActionsApiProposeResponse201.from_dict(response.json())

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
) -> Response[ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError]:
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
    body: ActionsApiProposeBody,
) -> Response[ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError]:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionsApiProposeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError]
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
    body: ActionsApiProposeBody,
) -> ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError | None:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionsApiProposeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError
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
    body: ActionsApiProposeBody,
) -> Response[ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError]:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionsApiProposeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError]
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
    body: ActionsApiProposeBody,
) -> ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError | None:
    """Propose actions

     Submit a governed proposal for an advertising account available to this workspace key. A matching
    idempotency key returns the saved batch.

    Args:
        workspace (int):
        body (ActionsApiProposeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsApiProposeResponse200 | ActionsApiProposeResponse201 | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
