from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_policies_retire_response_200 import LaunchPoliciesRetireResponse200
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    launch_policy: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/admin/policies/{launch_policy}/retire".format(
            workspace=quote(str(workspace), safe=""),
            launch_policy=quote(str(launch_policy), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchPoliciesRetireResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

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
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    launch_policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError]:
    """Retire a Launch policy

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        launch_policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        launch_policy=launch_policy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    launch_policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError | None:
    """Retire a Launch policy

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        launch_policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        launch_policy=launch_policy,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    launch_policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError]:
    """Retire a Launch policy

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        launch_policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        launch_policy=launch_policy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    launch_policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError | None:
    """Retire a Launch policy

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        launch_policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPoliciesRetireResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            launch_policy=launch_policy,
            client=client,
        )
    ).parsed
