from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from plainrouter import create_client, launch_plans_copy
from plainrouter.generated.api.deployment_plan import launch_plans_copy as generated_copy
from plainrouter.generated.types import Response

DRAFT = json.dumps(
    {
        "plan": {
            "id": "draft",
            "platform_ad_account_id": 1,
            "status": "draft",
            "budget_amount_minor": 100,
            "validation_result": None,
            "validated_at": None,
            "approval_id": None,
        }
    }
)
CASES: list[tuple[str, int, str]] = [
    ("200-valid", 200, DRAFT),
    ("201-valid", 201, DRAFT),
    ("200-malformed", 200, "{not json"),
    ("201-malformed", 201, "{not json"),
    ("204-empty", 204, ""),
    ("400-generic", 400, '{"message":"Bad request"}'),
    ("401-generic", 401, '{"message":"Unauthenticated"}'),
    ("403-generic", 403, '{"message":"Forbidden"}'),
    ("404-generic", 404, '{"message":"Not found"}'),
    ("413-generic", 413, '{"message":"Too large"}'),
    ("422-generic", 422, '{"message":"Invalid"}'),
    ("429-generic", 429, '{"message":"Rate limited"}'),
    ("500-generic", 500, '{"message":"Server error"}'),
    ("502-html", 502, "<html>Unavailable</html>"),
    ("503-generic", 503, '{"message":"Unavailable"}'),
    ("503-html", 503, "<html>Unavailable</html>"),
    ("503-malformed", 503, "{not json"),
    ("503-other-envelope", 503, '{"error":{"code":"maintenance","message":"Down"}}'),
    ("503-no-message", 503, '{"error":{"code":"proposal_not_recorded"}}'),
    ("503-error-null", 503, '{"error":null}'),
    ("503-error-array", 503, '{"error":[]}'),
    ("connect-error", 0, ""),
    ("connect-timeout", 0, ""),
]

CASES.extend(
    (f"cross-{status}-{kind}", status, body)
    for status in (200, 201, 204, 400, 401, 403, 404, 413, 422, 429, 500, 502, 503)
    for kind, body in (
        ("generic", '{"message":"Unavailable"}'),
        ("html", "<html>Unavailable</html>"),
        ("malformed", "{not json"),
        ("other-envelope", '{"error":{"code":"maintenance","message":"Down"}}'),
    )
    if (status, body) not in {(case[1], case[2]) for case in CASES}
)


def normalized(value: object) -> object:
    if isinstance(value, Response):
        parsed = value.parsed
        to_dict = getattr(parsed, "to_dict", None)
        return {
            "status": int(value.status_code),
            "headers": dict(value.headers),
            "content": value.content,
            "parsed_type": type(parsed).__name__,
            "parsed": to_dict() if callable(to_dict) else parsed,
        }
    return value


async def capture(
    facade: bool, asynchronous: bool, name: str, status: int, body: str, raise_unexpected: bool
) -> dict[str, Any]:
    requests: list[tuple[str, str, str, bytes]] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append((request.method, str(request.url), request.headers["Authorization"], request.read()))
        if name == "connect-error":
            raise httpx.ConnectError("Connection refused", request=request)
        if name == "connect-timeout":
            raise httpx.ConnectTimeout("Connect timed out", request=request)
        return httpx.Response(status, text=body, headers={"Retry-After": "30"})

    client = create_client(
        "parity-token", base_url="https://example.test/api/v1", raise_on_unexpected_status=raise_unexpected
    )
    transport = httpx.MockTransport(handle)
    client.set_httpx_client(
        httpx.Client(
            base_url="https://example.test/api/v1",
            transport=transport,
            headers={"Authorization": "Bearer parity-token"},
        )
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(
            base_url="https://example.test/api/v1",
            transport=transport,
            headers={"Authorization": "Bearer parity-token"},
        )
    )
    module = launch_plans_copy if facade else generated_copy
    result: object
    try:
        result = (
            await module.asyncio_detailed(1, "failed-plan", client=client)
            if asynchronous
            else module.sync_detailed(1, "failed-plan", client=client)
        )
        outcome = {"returned": normalized(result)}
    except Exception as error:
        outcome = {"exception": type(error).__name__, "message": str(error)}
    finally:
        client.get_httpx_client().close()
        await client.get_async_httpx_client().aclose()
    outcome["requests"] = requests
    return outcome


@pytest.mark.parametrize("case", CASES, ids=[case[0] for case in CASES])
@pytest.mark.parametrize("raise_unexpected", [False, True])
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_copy_facade_matches_generated_for_other_responses_and_failures(
    case: tuple[str, int, str], raise_unexpected: bool, asynchronous: bool
) -> None:
    name, status, body = case
    expected = await capture(False, asynchronous, name, status, body, raise_unexpected)
    actual = await capture(True, asynchronous, name, status, body, raise_unexpected)
    assert actual == expected
    assert len(actual["requests"]) == 1
