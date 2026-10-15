from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_creatives_status_response_200 import LaunchCreativesStatusResponse200
from ...models.update_creative_status_request import UpdateCreativeStatusRequest
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    creative: str,
    *,
    body: UpdateCreativeStatusRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/workspaces/{workspace}/admin/creatives/{creative}/status".format(
            workspace=quote(str(workspace), safe=""),
            creative=quote(str(creative), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchCreativesStatusResponse200.from_dict(response.json())

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
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    creative: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCreativeStatusRequest,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError]:
    """Update a workspace creative status

     Read a creative or change its approval status within the authorized workspace. Creative content and
    provider submission remain separate operations.

    Args:
        workspace (int):
        creative (str):
        body (UpdateCreativeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        creative=creative,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    creative: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCreativeStatusRequest,
) -> ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError | None:
    """Update a workspace creative status

     Read a creative or change its approval status within the authorized workspace. Creative content and
    provider submission remain separate operations.

    Args:
        workspace (int):
        creative (str):
        body (UpdateCreativeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        creative=creative,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    creative: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCreativeStatusRequest,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError]:
    """Update a workspace creative status

     Read a creative or change its approval status within the authorized workspace. Creative content and
    provider submission remain separate operations.

    Args:
        workspace (int):
        creative (str):
        body (UpdateCreativeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        creative=creative,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    creative: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCreativeStatusRequest,
) -> ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError | None:
    """Update a workspace creative status

     Read a creative or change its approval status within the authorized workspace. Creative content and
    provider submission remain separate operations.

    Args:
        workspace (int):
        creative (str):
        body (UpdateCreativeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchCreativesStatusResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            creative=creative,
            client=client,
            body=body,
        )
    ).parsed
