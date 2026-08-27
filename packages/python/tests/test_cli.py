from __future__ import annotations

import datetime
import io
from http import HTTPStatus
from pathlib import Path
from typing import Any, cast

import pytest

from plainrouter.cli import (
    CliDependencies,
    CliOperations,
    get_config_path,
    read_stored_config,
    resolve_config,
    run_cli,
    write_stored_config,
)
from plainrouter.generated import AuthenticatedClient
from plainrouter.generated.types import Response


class RecordingOperation:
    def __init__(self, response: Response[Any] | None = None) -> None:
        self.calls: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
        self.response = response or api_response({"ok": True})

    def __call__(self, *args: Any, **kwargs: Any) -> Response[Any]:
        self.calls.append((args, kwargs))
        return self.response


def api_response(data: Any, status: HTTPStatus = HTTPStatus.OK) -> Response[Any]:
    return Response(status_code=status, content=b"", headers={}, parsed=data)


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
    return CliOperations(**recorded), recorded


def create_dependencies(
    tmp_path: Path,
    *,
    operations: CliOperations | None = None,
    environment: dict[str, str] | None = None,
    prompt_token: str = "fixture-token-1234",
    confirm: bool = True,
) -> tuple[CliDependencies, io.StringIO, io.StringIO, list[tuple[str, str]]]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    clients: list[tuple[str, str]] = []

    def client_factory(token: str, *, base_url: str) -> AuthenticatedClient:
        clients.append((token, base_url))
        return cast(AuthenticatedClient, object())

    if operations is None:
        operations, _ = create_operations()
    dependencies = CliDependencies(
        operations=operations,
        client_factory=client_factory,
        environ={"PLAINROUTER_TOKEN": "environment-token", **(environment or {})},
        home_directory=lambda: tmp_path,
        stdin=io.StringIO(),
        stdout=stdout,
        stderr=stderr,
        prompt_token=lambda _question: prompt_token,
        confirm=lambda _question: confirm,
    )
    return dependencies, stdout, stderr, clients


def test_config_resolution_and_owner_only_permissions(tmp_path: Path) -> None:
    config_path = get_config_path({}, tmp_path)
    write_stored_config(
        config_path,
        {"baseUrl": "https://file.example.test/api/v1", "token": "file-token"},
    )

    assert read_stored_config(config_path)["token"] == "file-token"
    assert config_path.stat().st_mode & 0o777 == 0o600
    assert config_path.parent.stat().st_mode & 0o777 == 0o700
    assert (
        resolve_config(
            {
                "PLAINROUTER_BASE_URL": "https://environment.example.test/api/v1",
                "PLAINROUTER_TOKEN": "environment-token",
            },
            config_path,
        ).base_url
        == "https://environment.example.test/api/v1"
    )


def test_auth_commands_store_mask_and_remove_token(tmp_path: Path) -> None:
    dependencies, stdout, stderr, _clients = create_dependencies(tmp_path, environment={"PLAINROUTER_TOKEN": ""})

    assert run_cli(["auth", "login"], dependencies) == 0
    config_path = get_config_path(dependencies.environ, tmp_path)
    assert read_stored_config(config_path)["token"] == "fixture-token-1234"
    assert "fixture-token-1234" not in stdout.getvalue()

    stdout.seek(0)
    stdout.truncate(0)
    assert run_cli(["auth", "status", "--json"], dependencies) == 0
    assert "••••1234" in stdout.getvalue()
    assert "fixture-token-1234" not in stdout.getvalue()
    assert stderr.getvalue() == ""

    assert run_cli(["auth", "logout"], dependencies) == 0
    assert not config_path.exists()


def test_events_commands_map_to_python_operations(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    dependencies, stdout, _stderr, clients = create_dependencies(tmp_path, operations=operations)

    assert (
        run_cli(
            ["events", "create", "--data", '{"event_name":"Purchase","event_id":"evt_1"}', "--json"],
            dependencies,
        )
        == 0
    )
    body = recorded["create_event"].calls[0][1]["body"]
    assert body.to_dict() == {"event_name": "Purchase", "event_id": "evt_1"}
    assert stdout.getvalue() == '{\n  "ok": true\n}\n'

    assert run_cli(["events", "get", "evt_1"], dependencies) == 0
    assert recorded["get_event"].calls[0][0] == ("evt_1",)
    assert run_cli(["events", "list", "--per-page", "25"], dependencies) == 0
    assert recorded["list_events"].calls[0][1]["per_page"] == 25
    assert clients[0] == ("environment-token", "https://plainrouter.com/api/v1")


def test_destination_and_delivery_commands_preserve_options(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    dependencies, _stdout, _stderr, _clients = create_dependencies(tmp_path, operations=operations)

    assert run_cli(["destinations", "test-mode", "dest_1", "--on", "--test-event-code", "TEST42"], dependencies) == 0
    assert recorded["set_destination_test_mode"].calls[0][1]["body"].to_dict() == {
        "enabled": True,
        "test_event_code": "TEST42",
    }

    assert (
        run_cli(
            [
                "destinations",
                "test-purchase",
                "dest_1",
                "--value",
                "25.00",
                "--currency",
                "USD",
                "--order-id",
                "order_1",
            ],
            dependencies,
        )
        == 0
    )
    assert recorded["send_test_purchase"].calls[0][1]["body"].to_dict() == {
        "value": "25.00",
        "currency": "USD",
        "order_id": "order_1",
    }

    assert (
        run_cli(
            [
                "deliveries",
                "replay",
                "--delivery-id",
                "7",
                "--delivery-id",
                "9",
                "--event-name",
                "Purchase",
                "--limit",
                "50",
            ],
            dependencies,
        )
        == 0
    )
    assert recorded["replay_deliveries"].calls[0][1]["body"].to_dict() == {
        "delivery_ids": [7, 9],
        "event_name": "Purchase",
        "limit": 50,
    }


def test_report_and_deletion_commands_preserve_types(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    dependencies, _stdout, _stderr, _clients = create_dependencies(tmp_path, operations=operations)

    assert run_cli(["reports", "reconciliation", "--date", "2026-08-18"], dependencies) == 0
    assert recorded["get_reconciliation_report"].calls[0][1]["date"] == datetime.date(2026, 8, 18)
    assert run_cli(["reports", "emq"], dependencies) == 0
    assert len(recorded["get_emq_report"].calls) == 1

    assert (
        run_cli(["user-data", "delete", "--type", "email", "--hash", "hashed_identifier", "--yes"], dependencies) == 0
    )
    assert recorded["delete_user_data"].calls[0][1]["body"].to_dict() == {
        "identifier_type": "email",
        "identifier_hash": "hashed_identifier",
    }


def test_deletion_decline_is_non_mutating(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    dependencies, stdout, _stderr, clients = create_dependencies(tmp_path, operations=operations, confirm=False)

    assert run_cli(["user-data", "delete", "--type", "email", "--hash", "hashed_identifier"], dependencies) == 0
    assert recorded["delete_user_data"].calls == []
    assert clients == []
    assert stdout.getvalue() == "Deletion cancelled.\n"


def test_api_error_is_formatted_and_returns_nonzero(tmp_path: Path) -> None:
    operations, recorded = create_operations()
    recorded["create_event"].response = api_response(
        {
            "message": "The given data was invalid.",
            "errors": {"event_name": ["The event name field is required."]},
        },
        HTTPStatus.UNPROCESSABLE_ENTITY,
    )
    dependencies, _stdout, stderr, _clients = create_dependencies(tmp_path, operations=operations)

    assert run_cli(["events", "create", "--data", "{}"], dependencies) == 1
    assert "API error (HTTP 422)" in stderr.getvalue()
    assert "event_name: The event name field is required." in stderr.getvalue()


@pytest.mark.parametrize("arguments", [["destinations", "test-mode", "dest_1"], ["events", "create", "--data", "[]"]])
def test_cli_validation_fails_before_api_calls(tmp_path: Path, arguments: list[str]) -> None:
    operations, recorded = create_operations()
    dependencies, _stdout, stderr, clients = create_dependencies(tmp_path, operations=operations)

    assert run_cli(arguments, dependencies) == 1
    assert clients == []
    assert all(operation.calls == [] for operation in recorded.values())
    assert "Error:" in stderr.getvalue()


def test_help_and_module_entrypoint_contract(tmp_path: Path) -> None:
    dependencies, stdout, stderr, _clients = create_dependencies(tmp_path)

    assert run_cli(["--help"], dependencies) == 0
    assert "PlainRouter Signals API command line interface" in stdout.getvalue()
    assert stderr.getvalue() == ""
