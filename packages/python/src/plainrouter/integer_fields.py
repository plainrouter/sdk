from __future__ import annotations

import json
from collections.abc import Iterator, Mapping
from importlib.resources import files
from typing import Any

import httpx

_INTEGER_FIELDS: dict[str, dict[str, Any]] = json.loads(
    files("plainrouter").joinpath("_integer_fields.json").read_text(encoding="utf-8")
)
_OPERATIONS = sorted(
    _INTEGER_FIELDS.items(),
    key=lambda item: (item[0].count("{"), -len(item[0])),
)


def _route_parameters(template: str, request_path: str) -> dict[str, str] | None:
    template_parts = [part for part in template.split("/") if part]
    actual_parts = [part for part in request_path.split("/") if part]
    if len(actual_parts) < len(template_parts):
        return None

    offset = len(actual_parts) - len(template_parts)
    parameters: dict[str, str] = {}
    for expected, actual in zip(template_parts, actual_parts[offset:]):
        if expected.startswith("{") and expected.endswith("}"):
            parameters[expected[1:-1]] = actual
        elif expected != actual:
            return None
    return parameters


def _operation_for_request(request: httpx.Request) -> tuple[str, dict[str, Any], dict[str, str]] | None:
    method = request.method.upper()
    for operation_key, fields in _OPERATIONS:
        operation_method, template = operation_key.split(" ", 1)
        if operation_method != method:
            continue
        parameters = _route_parameters(template, request.url.path)
        if parameters is not None:
            return operation_key, fields, parameters
    return None


def _values_at_path(value: Any, path: list[str]) -> Iterator[Any]:
    if not path:
        yield value
        return

    head, *tail = path
    if head == "*":
        if isinstance(value, Mapping):
            for child in value.values():
                yield from _values_at_path(child, tail)
        elif isinstance(value, list):
            for child in value:
                yield from _values_at_path(child, tail)
    elif isinstance(value, Mapping) and head in value:
        yield from _values_at_path(value[head], tail)


def _field_name(path: list[str]) -> str:
    return ".".join("[]" if part == "*" else part for part in path) or "request body"


def _multipart_values(request: httpx.Request, name: str) -> Iterator[str]:
    # HTTPX represents regular multipart form fields as byte-valued FileField entries;
    # inspect those entries without reading the uploaded file stream into memory.
    stream_fields = getattr(request.stream, "fields", ())
    for field in stream_fields:
        if getattr(field, "name", None) != name:
            continue
        value = getattr(field, "file", None)
        if isinstance(value, bytes):
            yield value.decode("utf-8", errors="replace")
        elif isinstance(value, str):
            yield value


def _reject_boolean(
    request: httpx.Request, fields: dict[str, Any], parameters: dict[str, str], body: bytes | None = None
) -> None:
    operation_id = fields["operationId"]
    boolean_strings = {"true", "false"}

    for name in fields["path"]:
        if parameters.get(name, "").casefold() in boolean_strings:
            raise TypeError(f"{operation_id} integer field {name!r} must not be a boolean")

    for name in fields["query"]:
        for value in request.url.params.get_list(name):
            if value.casefold() in boolean_strings:
                raise TypeError(f"{operation_id} integer field {name!r} must not be a boolean")

    if not fields["body"]:
        return
    if hasattr(request.stream, "fields"):
        for path in fields["body"]:
            if len(path) == 1 and path[0] != "*":
                if any(value.strip().casefold() in boolean_strings for value in _multipart_values(request, path[0])):
                    raise TypeError(f"{operation_id} integer field {path[0]!r} must not be a boolean")
        return
    try:
        payload = json.loads(request.content if body is None else body)
    except (TypeError, ValueError):
        return

    for path in fields["body"]:
        if any(isinstance(value, bool) for value in _values_at_path(payload, path)):
            raise TypeError(f"{operation_id} integer field {_field_name(path)!r} must not be a boolean")


def check_integer_fields(request: httpx.Request) -> None:
    """Reject booleans only at request locations declared integer by the signed spec."""

    matched = _operation_for_request(request)
    if matched is not None:
        _, fields, parameters = matched
        try:
            _reject_boolean(request, fields, parameters)
        except httpx.RequestNotRead:
            _reject_boolean(request, fields, parameters, request.read())


async def check_integer_fields_async(request: httpx.Request) -> None:
    """Async HTTPX request-hook wrapper for the shared synchronous check."""

    matched = _operation_for_request(request)
    if matched is not None:
        _, fields, parameters = matched
        try:
            _reject_boolean(request, fields, parameters)
        except httpx.RequestNotRead:
            _reject_boolean(request, fields, parameters, await request.aread())
