from __future__ import annotations

import io
import json
from collections.abc import Callable
from http import HTTPStatus
from pathlib import Path
from typing import Any, cast

from plainrouter.cli import CliDependencies, CliOperations, run_cli
from plainrouter.generated import AuthenticatedClient
from plainrouter.generated.types import Response
from plainrouter.validation import validate_create_event_body

VALID_CAPTURED_AT = "2026-08-19T12:34:56.123456+02:00"


class RecordingOperation:
    def __init__(self, response: Response[Any] | None = None) -> None:
        self.calls: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
        self.response = response or Response(
            status_code=HTTPStatus.ACCEPTED,
            content=b"",
            headers={},
            parsed={"event_id": "event-123", "duplicate": False},
        )

    def __call__(self, *args: Any, **kwargs: Any) -> Response[Any]:
        self.calls.append((args, kwargs))
        return self.response


def create_operations() -> tuple[CliOperations, dict[str, RecordingOperation]]:
    names = (
        "create_event",
        "delete_user_data",
        "get_emq_report",
        "get_event",
        "get_reconciliation_report",
        "list_events",
        "replay_deliveries",
        "send_test_purchase",
        "set_destination_test_mode",
    )
    recorded = {name: RecordingOperation() for name in names}
    return CliOperations(**cast(dict[str, Callable[..., Response[Any]]], recorded)), recorded


def create_dependencies(
    tmp_path: Path,
    operations: CliOperations,
) -> tuple[CliDependencies, io.StringIO, io.StringIO, list[tuple[str, str]]]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    clients: list[tuple[str, str]] = []

    def client_factory(token: str, *, base_url: str) -> AuthenticatedClient:
        clients.append((token, base_url))
        return cast(AuthenticatedClient, object())

    dependencies = CliDependencies(
        operations=operations,
        client_factory=client_factory,
        environ={"PLAINROUTER_TOKEN": "environment-token"},
        home_directory=lambda: tmp_path,
        stdin=io.StringIO(),
        stdout=stdout,
        stderr=stderr,
        prompt_token=lambda _question: "fixture-token-1234",
        confirm=lambda _question: True,
    )
    return dependencies, stdout, stderr, clients


def validator_message(body: dict[str, Any]) -> str:
    try:
        validate_create_event_body(body)
    except Exception as error:
        return str(error)
    raise AssertionError("Expected the fixture to fail SDK validation")


def test_python_cli_rejects_visitor_id_without_captured_at_before_call(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    body = {
        "event_name": "Purchase",
        "consent_basis": "consent",
        "visitor_id": "visitor-123",
    }
    dependencies, _stdout, stderr, clients = create_dependencies(tmp_path, operations)

    assert run_cli(["events", "create", "--data", json.dumps(body)], dependencies) == 1
    assert validator_message(body) in stderr.getvalue()
    assert recorded["create_event"].calls == []
    assert clients == []


def test_python_cli_rejects_user_data_space_separator_before_call(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    body = {
        "event_name": "Purchase",
        "consent_basis": "consent",
        "user_data": {"em": "hashed-email"},
        "consent": {"captured_at": "2026-08-19 12:34:56+02:00"},
    }
    dependencies, _stdout, stderr, clients = create_dependencies(tmp_path, operations)

    assert run_cli(["events", "create", "--data", json.dumps(body)], dependencies) == 1
    assert validator_message(body) in stderr.getvalue()
    assert recorded["create_event"].calls == []
    assert clients == []


def test_python_cli_sends_valid_captured_at_input(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    body = {
        "event_name": "Purchase",
        "consent_basis": "consent",
        "visitor_id": "visitor-123",
        "consent": {"captured_at": VALID_CAPTURED_AT},
    }
    dependencies, _stdout, _stderr, clients = create_dependencies(tmp_path, operations)

    assert run_cli(["events", "create", "--data", json.dumps(body)], dependencies) == 0
    assert len(recorded["create_event"].calls) == 1
    assert recorded["create_event"].calls[0][1]["body"].to_dict() == body
    assert clients == [("environment-token", "https://plainrouter.com/api/v1")]


def test_python_cli_prints_202_ingestion_warning_to_stderr_without_failing(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    warning = {
        "code": "consent_captured_at_invalid",
        "field": "consent.captured_at",
        "message": "Consent capture time must be ISO-8601.",
    }
    recorded["create_event"].response = Response(
        status_code=HTTPStatus.ACCEPTED,
        content=b"",
        headers={},
        parsed={"event_id": "event-warning", "duplicate": False, "warnings": [warning]},
    )
    dependencies, _stdout, stderr, _clients = create_dependencies(tmp_path, operations)

    assert (
        run_cli(
            [
                "events",
                "create",
                "--data",
                json.dumps({"event_name": "Purchase", "consent_basis": "consent"}),
            ],
            dependencies,
        )
        == 0
    )
    assert stderr.getvalue() == (
        "Warning: consent_captured_at_invalid (consent.captured_at): Consent capture time must be ISO-8601.\n"
    )
