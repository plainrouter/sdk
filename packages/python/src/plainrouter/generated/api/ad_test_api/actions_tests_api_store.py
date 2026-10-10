from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_tests_api_store_body import ActionsTestsApiStoreBody
from ...models.ad_test_create_read import AdTestCreateRead
from ...models.agent_credential_error import AgentCredentialError
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    *,
    body: ActionsTestsApiStoreBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agent/workspaces/{workspace}/tests".format(
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
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    if response.status_code == 201:
        response_201 = AdTestCreateRead.from_dict(response.json())

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

        def _parse_response_404(data: object) -> ApiRouteNotFound | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = ApiRouteNotFound.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = ErrorMessage.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
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
    body: ActionsTestsApiStoreBody,
) -> Response[
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
]:
    """Create a judging Test

     Creates a judging Test with frozen event, settings, axis, and 2 to 4 ads from one mirrored ad set;
    it creates no proposal or Meta write.

    Args:
        workspace (int):
        body (ActionsTestsApiStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestCreateRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError]
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
    body: ActionsTestsApiStoreBody,
) -> (
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    """Create a judging Test

     Creates a judging Test with frozen event, settings, axis, and 2 to 4 ads from one mirrored ad set;
    it creates no proposal or Meta write.

    Args:
        workspace (int):
        body (ActionsTestsApiStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestCreateRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError
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
    body: ActionsTestsApiStoreBody,
) -> Response[
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
]:
    """Create a judging Test

     Creates a judging Test with frozen event, settings, axis, and 2 to 4 ads from one mirrored ad set;
    it creates no proposal or Meta write.

    Args:
        workspace (int):
        body (ActionsTestsApiStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdTestCreateRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError]
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
    body: ActionsTestsApiStoreBody,
) -> (
    AdTestCreateRead
    | AgentCredentialError
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ErrorMessage
    | ValidationError
    | None
):
    """Create a judging Test

     Creates a judging Test with frozen event, settings, axis, and 2 to 4 ads from one mirrored ad set;
    it creates no proposal or Meta write.

    Args:
        workspace (int):
        body (ActionsTestsApiStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdTestCreateRead | AgentCredentialError | ErrorMessage | ApiRouteNotFound | ErrorMessage | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
