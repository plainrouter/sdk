from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_proposal_input import ActionProposalInput
from ...models.action_proposal_read import ActionProposalRead
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.proposal_replay_conflict import ProposalReplayConflict
from ...models.validation_error import ValidationError
from ...models.workspace_lock_timeout import WorkspaceLockTimeout
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
) -> (
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    if response.status_code == 200:
        response_200 = ActionProposalRead.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ActionProposalRead.from_dict(response.json())

        return response_201

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

    if response.status_code == 409:
        response_409 = ProposalReplayConflict.from_dict(response.json())

        return response_409

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

    if response.status_code == 503:
        response_503 = WorkspaceLockTimeout.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
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
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Propose actions

     Submit or replay a governed proposal for an account available to this key. A kill switch saves a
    blocked proposal without executing provider writes.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionProposalRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ProposalReplayConflict | ValidationError | WorkspaceLockTimeout]
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
) -> (
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Propose actions

     Submit or replay a governed proposal for an account available to this key. A kill switch saves a
    blocked proposal without executing provider writes.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionProposalRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ProposalReplayConflict | ValidationError | WorkspaceLockTimeout
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
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Propose actions

     Submit or replay a governed proposal for an account available to this key. A kill switch saves a
    blocked proposal without executing provider writes.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionProposalRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ProposalReplayConflict | ValidationError | WorkspaceLockTimeout]
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
) -> (
    ActionProposalRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ProposalReplayConflict
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Propose actions

     Submit or replay a governed proposal for an account available to this key. A kill switch saves a
    blocked proposal without executing provider writes.

    Args:
        workspace (int):
        body (ActionProposalInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionProposalRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ProposalReplayConflict | ValidationError | WorkspaceLockTimeout
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
