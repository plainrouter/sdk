from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.creative_intake_read import CreativeIntakeRead
from ...models.creative_intake_rejected import CreativeIntakeRejected
from ...models.error_message import ErrorMessage
from ...models.store_creative_from_url_body import StoreCreativeFromUrlBody
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    *,
    body: StoreCreativeFromUrlBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/admin/creatives/from-url".format(
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
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
    | None
):
    if response.status_code == 201:
        response_201 = CreativeIntakeRead.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> AgentCredentialError | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = ErrorMessage.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = AgentCredentialError.from_dict(data)

            return response_403_type_1

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 413:

        def _parse_response_413(data: object) -> CreativeIntakeRejected | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_413_type_0 = CreativeIntakeRejected.from_dict(data)

                return response_413_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_413_type_1 = ErrorMessage.from_dict(data)

            return response_413_type_1

        response_413 = _parse_response_413(response.json())

        return response_413

    if response.status_code == 422:

        def _parse_response_422(data: object) -> CreativeIntakeRejected | ValidationError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = CreativeIntakeRejected.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = ValidationError.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
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
    body: StoreCreativeFromUrlBody,
) -> Response[
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
]:
    """Store a creative from a URL

     Store a creative in the credential-bound workspace. Set generator, generator_job and parent_creative
    tags for output from an outside tool.

    Args:
        workspace (int):
        body (StoreCreativeFromUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCredentialError | ErrorMessage | ApiRouteNotFound | CreativeIntakeRead | CreativeIntakeRejected | ErrorMessage | CreativeIntakeRejected | ValidationError | ErrorMessage]
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
    body: StoreCreativeFromUrlBody,
) -> (
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
    | None
):
    """Store a creative from a URL

     Store a creative in the credential-bound workspace. Set generator, generator_job and parent_creative
    tags for output from an outside tool.

    Args:
        workspace (int):
        body (StoreCreativeFromUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCredentialError | ErrorMessage | ApiRouteNotFound | CreativeIntakeRead | CreativeIntakeRejected | ErrorMessage | CreativeIntakeRejected | ValidationError | ErrorMessage
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
    body: StoreCreativeFromUrlBody,
) -> Response[
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
]:
    """Store a creative from a URL

     Store a creative in the credential-bound workspace. Set generator, generator_job and parent_creative
    tags for output from an outside tool.

    Args:
        workspace (int):
        body (StoreCreativeFromUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCredentialError | ErrorMessage | ApiRouteNotFound | CreativeIntakeRead | CreativeIntakeRejected | ErrorMessage | CreativeIntakeRejected | ValidationError | ErrorMessage]
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
    body: StoreCreativeFromUrlBody,
) -> (
    AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | CreativeIntakeRead
    | CreativeIntakeRejected
    | ErrorMessage
    | CreativeIntakeRejected
    | ValidationError
    | ErrorMessage
    | None
):
    """Store a creative from a URL

     Store a creative in the credential-bound workspace. Set generator, generator_job and parent_creative
    tags for output from an outside tool.

    Args:
        workspace (int):
        body (StoreCreativeFromUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCredentialError | ErrorMessage | ApiRouteNotFound | CreativeIntakeRead | CreativeIntakeRejected | ErrorMessage | CreativeIntakeRejected | ValidationError | ErrorMessage
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
