from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_dry_run_read import ActionDryRunRead
from ...models.action_proposal_input import ActionProposalInput
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
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
        "url": "/agent/workspaces/{workspace}/actions/dry-run".format(
            workspace=quote(str(workspace), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = ActionDryRunRead.from_dict(response.json())

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
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = ErrorMessage.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
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
    body: ActionProposalInput,
) -> Response[
    ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
]:
    """Preview actions

     Preview policy decisions and execution diffs for the approved account without saving a proposal. A
    kill switch returns blocked policy decisions.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
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
) -> ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | None:
    """Preview actions

     Preview policy decisions and execution diffs for the approved account without saving a proposal. A
    kill switch returns blocked policy decisions.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
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
) -> Response[
    ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
]:
    """Preview actions

     Preview policy decisions and execution diffs for the approved account without saving a proposal. A
    kill switch returns blocked policy decisions.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
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
) -> ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | None:
    """Preview actions

     Preview policy decisions and execution diffs for the approved account without saving a proposal. A
    kill switch returns blocked policy decisions.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDryRunRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
