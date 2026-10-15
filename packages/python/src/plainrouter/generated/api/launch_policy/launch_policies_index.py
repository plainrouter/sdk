from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_policies_index_response_200 import LaunchPoliciesIndexResponse200
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/policies".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchPoliciesIndexResponse200.from_dict(response.json())

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
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError]:
    """List Launch policies

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError | None:
    """List Launch policies

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError]:
    """List Launch policies

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError | None:
    """List Launch policies

     Read or maintain versioned naming and UTM policies in the authorized workspace. Policies apply to
    plans without submitting provider writes.

    Args:
        workspace (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPoliciesIndexResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
