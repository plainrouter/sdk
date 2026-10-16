from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.draft_batch_file_import_request import DraftBatchFileImportRequest
from ...models.error_message import ErrorMessage
from ...models.launcher_file_import_response_200 import LauncherFileImportResponse200
from ...models.launcher_file_import_response_403 import LauncherFileImportResponse403
from ...models.launcher_file_import_response_422_type_1 import LauncherFileImportResponse422Type1
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: DraftBatchFileImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mcp/launcher/import",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = LauncherFileImportResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LauncherFileImportResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 422:

        def _parse_response_422(data: object) -> LauncherFileImportResponse422Type1 | ValidationError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ValidationError.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = LauncherFileImportResponse422Type1.from_dict(data)

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
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DraftBatchFileImportRequest,
) -> Response[
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
]:
    """Import a Launcher draft batch

     Import a CSV or spreadsheet into a governed Launcher draft batch for the workspace and account
    authorized by the execution key.

    Args:
        body (DraftBatchFileImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LauncherFileImportResponse200 | LauncherFileImportResponse403 | LauncherFileImportResponse422Type1 | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DraftBatchFileImportRequest,
) -> (
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
    | None
):
    """Import a Launcher draft batch

     Import a CSV or spreadsheet into a governed Launcher draft batch for the workspace and account
    authorized by the execution key.

    Args:
        body (DraftBatchFileImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LauncherFileImportResponse200 | LauncherFileImportResponse403 | LauncherFileImportResponse422Type1 | ValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DraftBatchFileImportRequest,
) -> Response[
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
]:
    """Import a Launcher draft batch

     Import a CSV or spreadsheet into a governed Launcher draft batch for the workspace and account
    authorized by the execution key.

    Args:
        body (DraftBatchFileImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LauncherFileImportResponse200 | LauncherFileImportResponse403 | LauncherFileImportResponse422Type1 | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DraftBatchFileImportRequest,
) -> (
    ApiRouteNotFound
    | ErrorMessage
    | LauncherFileImportResponse200
    | LauncherFileImportResponse403
    | LauncherFileImportResponse422Type1
    | ValidationError
    | None
):
    """Import a Launcher draft batch

     Import a CSV or spreadsheet into a governed Launcher draft batch for the workspace and account
    authorized by the execution key.

    Args:
        body (DraftBatchFileImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LauncherFileImportResponse200 | LauncherFileImportResponse403 | LauncherFileImportResponse422Type1 | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
