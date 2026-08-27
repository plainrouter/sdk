from __future__ import annotations

import argparse
import datetime
import getpass
import json
import os
import sys
import tempfile
from collections.abc import Callable, Mapping, Sequence
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, TextIO, cast

from .client import DEFAULT_BASE_URL, create_client
from .generated import AuthenticatedClient
from .generated.api.event import create_event, get_event
from .generated.api.operations import (
    delete_user_data,
    get_emq_report,
    get_reconciliation_report,
    list_events,
    replay_deliveries,
    send_test_purchase,
    set_destination_test_mode,
)
from .generated.models import (
    CreateEventBodyType0,
    CreateEventBodyType1,
    DeleteUserDataBody,
    DeleteUserDataBodyIdentifierType,
    ReplayDeliveriesBody,
    SendTestPurchaseBody,
    SetDestinationTestModeBody,
)
from .generated.types import Response

Operation = Callable[..., Response[Any]]
ClientFactory = Callable[..., AuthenticatedClient]


@dataclass(frozen=True)
class CliOperations:
    create_event: Operation
    delete_user_data: Operation
    get_emq_report: Operation
    get_event: Operation
    get_reconciliation_report: Operation
    list_events: Operation
    replay_deliveries: Operation
    send_test_purchase: Operation
    set_destination_test_mode: Operation


DEFAULT_OPERATIONS = CliOperations(
    create_event=create_event.sync_detailed,
    delete_user_data=delete_user_data.sync_detailed,
    get_emq_report=get_emq_report.sync_detailed,
    get_event=get_event.sync_detailed,
    get_reconciliation_report=get_reconciliation_report.sync_detailed,
    list_events=list_events.sync_detailed,
    replay_deliveries=replay_deliveries.sync_detailed,
    send_test_purchase=send_test_purchase.sync_detailed,
    set_destination_test_mode=set_destination_test_mode.sync_detailed,
)


@dataclass(frozen=True)
class CliDependencies:
    operations: CliOperations = DEFAULT_OPERATIONS
    client_factory: ClientFactory = create_client
    environ: Mapping[str, str] = field(default_factory=lambda: os.environ)
    home_directory: Callable[[], Path] = Path.home
    stdin: TextIO = field(default_factory=lambda: sys.stdin)
    stdout: TextIO = field(default_factory=lambda: sys.stdout)
    stderr: TextIO = field(default_factory=lambda: sys.stderr)
    prompt_token: Callable[[str], str] | None = None
    confirm: Callable[[str], bool] | None = None


@dataclass(frozen=True)
class ResolvedConfig:
    base_url: str
    config_path: Path
    token: str | None = None
    token_source: str | None = None


@dataclass(frozen=True)
class _RawEventBody:
    """Preserve server-side validation for the CLI's arbitrary JSON body."""

    data: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return self.data


class CliError(Exception):
    pass


class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


def get_config_path(
    environment: Mapping[str, str] | None = None,
    home_directory: Path | None = None,
) -> Path:
    environment = os.environ if environment is None else environment
    home_directory = Path.home() if home_directory is None else home_directory
    config_home = environment.get("XDG_CONFIG_HOME", "").strip()
    root = Path(config_home) if config_home else home_directory / ".config"
    return root / "plainrouter" / "config.json"


def read_stored_config(config_path: Path) -> dict[str, str]:
    try:
        contents = config_path.read_text()
    except FileNotFoundError:
        return {}
    try:
        parsed = json.loads(contents)
    except json.JSONDecodeError as error:
        raise CliError(f"Config file is not valid JSON: {config_path}") from error
    if not isinstance(parsed, dict):
        raise CliError(f"Config file must contain a JSON object: {config_path}")

    stored: dict[str, str] = {}
    for key in ("token", "baseUrl"):
        value = parsed.get(key)
        if value is not None and not isinstance(value, str):
            raise CliError(f"Config {key} must be a string: {config_path}")
        if isinstance(value, str):
            stored[key] = value
    return stored


def write_stored_config(config_path: Path, config: Mapping[str, str]) -> None:
    config_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    config_path.parent.chmod(0o700)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("w", dir=config_path.parent, encoding="utf-8", delete=False) as temporary:
            temporary_path = Path(temporary.name)
            temporary_path.chmod(0o600)
            json.dump(dict(config), temporary, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
        temporary_path.replace(config_path)
        config_path.chmod(0o600)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def save_token(config_path: Path, token: str) -> None:
    write_stored_config(config_path, {**read_stored_config(config_path), "token": token})


def remove_stored_config(config_path: Path) -> None:
    config_path.unlink(missing_ok=True)


def resolve_config(
    environment: Mapping[str, str] | None = None,
    config_path: Path | None = None,
    home_directory: Path | None = None,
) -> ResolvedConfig:
    environment = os.environ if environment is None else environment
    config_path = get_config_path(environment, home_directory) if config_path is None else config_path
    stored = read_stored_config(config_path)
    environment_token = environment.get("PLAINROUTER_TOKEN", "").strip()
    file_token = stored.get("token", "").strip()
    environment_base_url = environment.get("PLAINROUTER_BASE_URL", "").strip()
    file_base_url = stored.get("baseUrl", "").strip()
    token = environment_token or file_token or None
    token_source = "environment" if environment_token else "file" if file_token else None
    return ResolvedConfig(
        base_url=environment_base_url or file_base_url or DEFAULT_BASE_URL,
        config_path=config_path,
        token=token,
        token_source=token_source,
    )


def mask_token(token: str) -> str:
    return "••••" if len(token) <= 4 else f"••••{token[-4:]}"


def _package_version() -> str:
    try:
        return version("plainrouter")
    except PackageNotFoundError:
        return "0+unknown"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plainrouter", description="PlainRouter Signals API command line interface")
    parser.add_argument("--version", action="version", version=f"%(prog)s {_package_version()}")
    parser.add_argument("--json", action="store_true", help="emit the API response as JSON")
    commands = parser.add_subparsers(dest="command", required=True)

    auth = commands.add_parser("auth", help="manage tracker authentication")
    auth_commands = auth.add_subparsers(dest="auth_command", required=True)
    auth_commands.add_parser("login", help="paste and store a tracker token").set_defaults(handler="auth_login")
    auth_commands.add_parser("logout", help="remove the stored config").set_defaults(handler="auth_logout")
    auth_commands.add_parser("status", help="show the active masked credential source").set_defaults(
        handler="auth_status"
    )

    events = commands.add_parser("events", help="create and inspect events")
    event_commands = events.add_subparsers(dest="events_command", required=True)
    event_create = event_commands.add_parser("create", help="submit a Signal event")
    event_create.add_argument("--data", required=True, help="event request body as a JSON object")
    event_create.set_defaults(handler="events_create")
    event_get = event_commands.add_parser("get", help="get an event and its delivery state")
    event_get.add_argument("id")
    event_get.set_defaults(handler="events_get")
    event_list = event_commands.add_parser("list", help="list recent events and acceptance metrics")
    event_list.add_argument("--per-page", type=int, help="events per page")
    event_list.set_defaults(handler="events_list")

    destinations = commands.add_parser("destinations", help="manage destination test operations")
    destination_commands = destinations.add_subparsers(dest="destinations_command", required=True)
    test_mode = destination_commands.add_parser("test-mode", help="enable or disable destination test mode")
    test_mode.add_argument("id")
    mode = test_mode.add_mutually_exclusive_group()
    mode.add_argument("--on", action="store_true", help="enable test mode")
    mode.add_argument("--off", action="store_true", help="disable test mode")
    test_mode.add_argument("--test-event-code", help="optional platform test event code")
    test_mode.set_defaults(handler="destinations_test_mode")
    test_purchase = destination_commands.add_parser("test-purchase", help="send a destination test purchase")
    test_purchase.add_argument("id")
    test_purchase.add_argument("--value", help="purchase value")
    test_purchase.add_argument("--currency", help="purchase currency")
    test_purchase.add_argument("--order-id", help="purchase order ID")
    test_purchase.set_defaults(handler="destinations_test_purchase")

    deliveries = commands.add_parser("deliveries", help="manage event deliveries")
    delivery_commands = deliveries.add_subparsers(dest="deliveries_command", required=True)
    replay = delivery_commands.add_parser("replay", help="queue eligible deliveries for replay")
    replay.add_argument("--delivery-id", action="append", type=int, help="delivery ID; repeat for multiple IDs")
    replay.add_argument("--event-name", help="limit replay to an event name")
    replay.add_argument("--limit", type=int, help="maximum deliveries to evaluate")
    replay.set_defaults(handler="deliveries_replay")

    reports = commands.add_parser("reports", help="view Signal reports")
    report_commands = reports.add_subparsers(dest="reports_command", required=True)
    reconciliation = report_commands.add_parser("reconciliation", help="get reconciliation reports for a date")
    reconciliation.add_argument("--date", required=True, help="report date in YYYY-MM-DD format")
    reconciliation.set_defaults(handler="reports_reconciliation")
    report_commands.add_parser("emq", help="get event match quality snapshots").set_defaults(handler="reports_emq")

    user_data = commands.add_parser("user-data", help="manage data subject deletion")
    user_data_commands = user_data.add_subparsers(dest="user_data_command", required=True)
    delete = user_data_commands.add_parser("delete", help="delete matching user data")
    delete.add_argument("--type", required=True, help="identifier type: email, phone, or external_id")
    delete.add_argument("--hash", required=True, help="hashed identifier value")
    delete.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    delete.set_defaults(handler="user_data_delete")
    return parser


def _normalize_arguments(arguments: Sequence[str]) -> tuple[list[str], bool]:
    as_json = False
    normalized: list[str] = []
    for argument in arguments:
        if argument == "--json":
            as_json = True
        else:
            normalized.append(argument)
    return normalized, as_json


def _parse_json_object(value: str) -> dict[str, Any]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as error:
        raise CliError("--data must be a valid JSON object") from error
    if not isinstance(parsed, dict):
        raise CliError("--data must be a JSON object")
    return cast(dict[str, Any], parsed)


def _prompt_for_token(dependencies: CliDependencies) -> str:
    if dependencies.prompt_token is not None:
        return dependencies.prompt_token("Paste tracker token: ").strip()
    return getpass.getpass("Paste tracker token: ", stream=dependencies.stderr).strip()


def _confirm_action(question: str, dependencies: CliDependencies) -> bool:
    if dependencies.confirm is not None:
        return dependencies.confirm(question)
    dependencies.stderr.write(f"{question} [y/N] ")
    dependencies.stderr.flush()
    return dependencies.stdin.readline().strip().lower() in {"y", "yes"}


def _printable_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(",", ":"), ensure_ascii=False)
    return str(value)


def _render_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "(none)"
    columns = list(dict.fromkeys(key for row in rows for key in row))
    widths = [max(len(column), *(len(_printable_value(row.get(column))) for row in rows)) for column in columns]

    def line(values: list[str]) -> str:
        return "  ".join(value.ljust(widths[index]) for index, value in enumerate(values))

    return "\n".join(
        [
            line(columns),
            line(["-" * width for width in widths]),
            *(line([_printable_value(row.get(column)) for column in columns]) for row in rows),
        ]
    )


def format_human(data: Any) -> str:
    if isinstance(data, list):
        if all(isinstance(item, dict) for item in data):
            return _render_table(cast(list[dict[str, Any]], data))
        return "\n".join(_printable_value(item) for item in data)
    if not isinstance(data, dict):
        return _printable_value(data)
    lines: list[str] = []
    for key, value in data.items():
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            lines.extend((f"{key}:", _render_table(cast(list[dict[str, Any]], value))))
        elif isinstance(value, dict):
            lines.extend((f"{key}:", format_human(value)))
        else:
            lines.append(f"{key}: {_printable_value(value)}")
    return "\n".join(lines)


def _write_response(data: Any, as_json: bool, output: TextIO) -> None:
    rendered = json.dumps(data, indent=2, ensure_ascii=False) if as_json else format_human(data)
    output.write(f"{rendered}\n")


def _response_data(parsed: Any) -> Any:
    to_dict = getattr(parsed, "to_dict", None)
    return to_dict() if callable(to_dict) else parsed


def _format_api_error(data: Any) -> str:
    if isinstance(data, dict) and isinstance(data.get("message"), str):
        message = cast(str, data["message"])
        errors = data.get("errors")
        if isinstance(errors, dict):
            details: list[str] = []
            for field_name, field_errors in errors.items():
                if isinstance(field_errors, list):
                    details.extend(f"{field_name}: {error}" for error in field_errors)
                else:
                    details.append(f"{field_name}: {field_errors}")
            if details:
                return message + "\n" + "\n".join(details)
        return message
    if isinstance(data, dict):
        return json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    return str(data or "Unknown API error")


def _execute_api(response: Response[Any], as_json: bool, dependencies: CliDependencies) -> None:
    data = _response_data(response.parsed)
    status = int(response.status_code)
    if status >= 400:
        if data is None:
            data = response.content.decode(errors="replace")
        raise ApiError(_format_api_error(data), status)
    if data is None:
        raise ApiError("API response did not contain data.", status)
    _write_response(data, as_json, dependencies.stdout)


def _api_client(dependencies: CliDependencies) -> AuthenticatedClient:
    config = resolve_config(dependencies.environ, home_directory=dependencies.home_directory())
    if config.token is None:
        raise CliError("No token configured. Set PLAINROUTER_TOKEN or run `plainrouter auth login`.")
    return dependencies.client_factory(config.token, base_url=config.base_url)


def _dispatch(arguments: argparse.Namespace, as_json: bool, dependencies: CliDependencies) -> None:
    handler = cast(str, arguments.handler)
    config_path = get_config_path(dependencies.environ, dependencies.home_directory())
    if handler == "auth_login":
        token = _prompt_for_token(dependencies)
        if not token:
            raise CliError("Token cannot be empty.")
        save_token(config_path, token)
        _write_response({"saved": True, "path": str(config_path)}, as_json, dependencies.stdout)
        return
    if handler == "auth_logout":
        remove_stored_config(config_path)
        _write_response({"removed": True, "path": str(config_path)}, as_json, dependencies.stdout)
        return
    if handler == "auth_status":
        config = resolve_config(dependencies.environ, config_path)
        status = (
            {
                "authenticated": True,
                "token": mask_token(config.token),
                "source": "PLAINROUTER_TOKEN" if config.token_source == "environment" else str(config.config_path),
                "base_url": config.base_url,
            }
            if config.token is not None
            else {"authenticated": False, "source": "none", "base_url": config.base_url}
        )
        _write_response(status, as_json, dependencies.stdout)
        return

    raw_event_body: _RawEventBody | None = None
    report_date: datetime.date | None = None
    identifier_type: DeleteUserDataBodyIdentifierType | None = None
    if handler == "events_create":
        raw_event_body = _RawEventBody(_parse_json_object(arguments.data))
    elif handler == "destinations_test_mode" and not arguments.on and not arguments.off:
        raise CliError("Choose exactly one of --on or --off.")
    elif handler == "reports_reconciliation":
        try:
            report_date = datetime.date.fromisoformat(arguments.date)
        except ValueError as error:
            raise CliError("--date must use YYYY-MM-DD format") from error
    elif handler == "user_data_delete":
        try:
            identifier_type = DeleteUserDataBodyIdentifierType(arguments.type)
        except ValueError as error:
            raise CliError("--type must be email, phone, or external_id") from error

    if handler == "user_data_delete" and not arguments.yes:
        if not _confirm_action(f"Delete user data for identifier type {arguments.type}?", dependencies):
            dependencies.stdout.write("Deletion cancelled.\n")
            return

    client = _api_client(dependencies)
    operations = dependencies.operations
    if handler == "events_create":
        assert raw_event_body is not None
        response = operations.create_event(
            client=client,
            body=cast(CreateEventBodyType0 | CreateEventBodyType1, raw_event_body),
        )
    elif handler == "events_get":
        response = operations.get_event(arguments.id, client=client)
    elif handler == "events_list":
        response = (
            operations.list_events(client=client)
            if arguments.per_page is None
            else operations.list_events(client=client, per_page=arguments.per_page)
        )
    elif handler == "destinations_test_mode":
        body = SetDestinationTestModeBody(enabled=bool(arguments.on))
        if arguments.test_event_code is not None:
            body.test_event_code = arguments.test_event_code
        response = operations.set_destination_test_mode(arguments.id, client=client, body=body)
    elif handler == "destinations_test_purchase":
        values = {
            key: value
            for key, value in {
                "value": arguments.value,
                "currency": arguments.currency,
                "order_id": arguments.order_id,
            }.items()
            if value is not None
        }
        response = operations.send_test_purchase(
            arguments.id, client=client, **({"body": SendTestPurchaseBody(**values)} if values else {})
        )
    elif handler == "deliveries_replay":
        values = {
            key: value
            for key, value in {
                "delivery_ids": arguments.delivery_id,
                "event_name": arguments.event_name,
                "limit": arguments.limit,
            }.items()
            if value is not None
        }
        response = operations.replay_deliveries(
            client=client, **({"body": ReplayDeliveriesBody(**values)} if values else {})
        )
    elif handler == "reports_reconciliation":
        assert report_date is not None
        response = operations.get_reconciliation_report(client=client, date=report_date)
    elif handler == "reports_emq":
        response = operations.get_emq_report(client=client)
    elif handler == "user_data_delete":
        assert identifier_type is not None
        response = operations.delete_user_data(
            client=client,
            body=DeleteUserDataBody(identifier_type=identifier_type, identifier_hash=arguments.hash),
        )
    else:
        raise CliError(f"Unsupported command handler: {handler}")
    _execute_api(response, as_json, dependencies)


def run_cli(argv: Sequence[str] | None = None, dependencies: CliDependencies | None = None) -> int:
    dependencies = CliDependencies() if dependencies is None else dependencies
    arguments, as_json = _normalize_arguments(sys.argv[1:] if argv is None else argv)
    parser = _build_parser()
    try:
        with redirect_stdout(dependencies.stdout), redirect_stderr(dependencies.stderr):
            parsed = parser.parse_args(arguments)
        _dispatch(parsed, as_json, dependencies)
        return 0
    except SystemExit as error:
        return int(error.code or 0)
    except ApiError as error:
        suffix = "" if error.status is None else f" (HTTP {error.status})"
        dependencies.stderr.write(f"API error{suffix}: {error}\n")
        return 1
    except (CliError, OSError, ValueError) as error:
        dependencies.stderr.write(f"Error: {error}\n")
        return 1


def main() -> int:
    return run_cli()


__all__ = [
    "CliDependencies",
    "CliOperations",
    "ResolvedConfig",
    "format_human",
    "get_config_path",
    "main",
    "mask_token",
    "read_stored_config",
    "remove_stored_config",
    "resolve_config",
    "run_cli",
    "save_token",
    "write_stored_config",
]
