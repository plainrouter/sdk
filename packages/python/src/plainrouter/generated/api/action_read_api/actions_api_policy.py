from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_policy_read import ActionPolicyRead
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    account_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/actions/policy".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActionPolicyRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ActionPolicyRead.from_dict(response.json())

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
    ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
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
    account_id: int | Unset = UNSET,
) -> Response[
    ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
]:
    """Get action policy

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> (
    ActionPolicyRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    """Get action policy

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> Response[
    ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
]:
    """Get action policy

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> (
    ActionPolicyRead
    | AgentCredentialError
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ValidationError
    | None
):
    """Get action policy

     Read persisted Actions data for the authorized account. Unbound keys require exactly one active
    account; account_id cannot select among multiple accounts.

    Args:
        workspace (int):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionPolicyRead | AgentCredentialError | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            account_id=account_id,
        )
    ).parsed
