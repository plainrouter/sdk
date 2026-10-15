from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_plans_validate_response_200 import LaunchPlansValidateResponse200
from ...models.plan_validate_rejected import PlanValidateRejected
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    workspace: int,
    deployment_plan: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/admin/plans/{deployment_plan}/validate".format(
            workspace=quote(str(workspace), safe=""),
            deployment_plan=quote(str(deployment_plan), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchPlansValidateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 422:

        def _parse_response_422(data: object) -> PlanValidateRejected | ValidationError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ValidationError.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = PlanValidateRejected.from_dict(data)

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
    ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError
]:
    """Validate a deployment plan

     Validate a plan without provider writes. Reuse a ready Meta video in the same ad account; plans
    needing a new video upload are refused.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError | None:
    """Validate a deployment plan

     Validate a plan without provider writes. Reuse a ready Meta video in the same ad account; plans
    needing a new video upload are refused.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        deployment_plan=deployment_plan,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError
]:
    """Validate a deployment plan

     Validate a plan without provider writes. Reuse a ready Meta video in the same ad account; plans
    needing a new video upload are refused.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError | None:
    """Validate a deployment plan

     Validate a plan without provider writes. Reuse a ready Meta video in the same ad account; plans
    needing a new video upload are refused.

    Args:
        workspace (int):
        deployment_plan (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansValidateResponse200 | PlanValidateRejected | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
        )
    ).parsed
