from __future__ import annotations

import importlib
import inspect
import json
import pkgutil
import re
from collections.abc import Callable, Mapping
from functools import wraps
from pathlib import Path
from typing import Any, cast

from httpx import AsyncClient, Client, Request, RequestNotRead

_PACKAGE_PATH = Path(__file__).parent
_CLOSED_OBJECTS = json.loads((_PACKAGE_PATH / "_closed_objects.json").read_text())
_SCHEMAS: dict[str, Any] = _CLOSED_OBJECTS["schemas"]
_OPERATIONS: dict[str, str] = _CLOSED_OBJECTS["operations"]
_CLOSED_REQUEST_MODEL_FIELDS: dict[str, list[str]] = json.loads(
    (_PACKAGE_PATH / "_closed_request_models.json").read_text()
)
_HTTP_METHODS = {"delete", "get", "patch", "post", "put"}


class ClosedRequestKeyError(RuntimeError):
    """Raised when a request contains a key that a closed OpenAPI object does not define."""


def _escape_pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _decode_pointer_token(value: str) -> str:
    return value.replace("~1", "/").replace("~0", "~")


def _schema_label(pointer: str, schema: Mapping[str, Any], operation: str) -> str:
    title = schema.get("title")
    if isinstance(title, str) and title:
        return title

    segments = [_decode_pointer_token(segment) for segment in pointer.removeprefix("#/").split("/")]
    label_parts: list[str] = []

    if "schemas" in segments:
        schema_index = segments.index("schemas")
        if schema_index + 1 < len(segments):
            label_parts.append(segments[schema_index + 1])
            segments = segments[schema_index + 2 :]
    else:
        label_parts.append(f"{operation} request body")
        if "schema" in segments:
            segments = segments[segments.index("schema") + 1 :]

    index = 0
    while index < len(segments):
        segment = segments[index]
        if segment == "properties" and index + 1 < len(segments):
            label_parts.append(segments[index + 1])
            index += 2
            continue
        if segment == "items" and label_parts:
            label_parts[-1] = f"{label_parts[-1]}[]"
        index += 1

    return ".".join(label_parts) if label_parts else pointer


def _resolve_schema(schema: Mapping[str, Any], pointer: str) -> tuple[dict[str, Any], str]:
    resolved = dict(schema)
    current_pointer = pointer
    seen: set[str] = set()

    while isinstance(resolved.get("$ref"), str):
        reference = resolved["$ref"]
        if reference in seen or reference not in _SCHEMAS:
            break
        seen.add(reference)
        current_pointer = reference
        target = _SCHEMAS[reference]
        if not isinstance(target, Mapping):
            break
        siblings = {key: value for key, value in resolved.items() if key != "$ref"}
        resolved = {**target, **siblings}

    return resolved, current_pointer


def _is_unset(value: object) -> bool:
    return value.__class__.__name__ == "Unset"


def _attribute_value(value: object, property_name: str) -> tuple[bool, Any]:
    candidates = (property_name, f"{property_name}_", f"field_{property_name}")
    for candidate in candidates:
        try:
            return True, getattr(value, candidate)
        except AttributeError:
            continue
    return False, None


def _mapping_for_value(value: object, property_names: set[str]) -> Mapping[Any, Any] | None:
    if isinstance(value, Mapping):
        return value

    if hasattr(value, "to_dict"):
        to_dict = getattr(value, "to_dict")
        if callable(to_dict):
            try:
                converted = to_dict()
            except (AttributeError, KeyError, TypeError, ValueError):
                converted = None
            if isinstance(converted, Mapping):
                return converted

    raw_body = getattr(value, "_body", None)
    if isinstance(raw_body, Mapping):
        return raw_body

    attributes: dict[str, Any] = {}
    for property_name in property_names:
        found, field_value = _attribute_value(value, property_name)
        if found and not _is_unset(field_value):
            attributes[property_name] = field_value
    return attributes if attributes else None


def _plain_value(value: object) -> object:
    return getattr(value, "value", value)


def _matching_union_branch(value: object, branches: list[Any], pointer: str) -> int | None:
    branch_constraints: list[dict[str, list[Any]]] = []
    union_properties: set[str] = set()

    for index, branch in enumerate(branches):
        if not isinstance(branch, Mapping):
            branch_constraints.append({})
            continue
        resolved, _ = _resolve_schema(branch, f"{pointer}/{index}")
        properties = resolved.get("properties")
        constraints: dict[str, list[Any]] = {}
        if isinstance(properties, Mapping):
            union_properties.update(str(name) for name in properties)
            for property_name, property_schema in properties.items():
                if not isinstance(property_schema, Mapping):
                    continue
                property_schema, _ = _resolve_schema(
                    property_schema,
                    f"{pointer}/{index}/properties/{_escape_pointer_token(str(property_name))}",
                )
                expected_values: list[Any] = []
                if "const" in property_schema:
                    expected_values.append(property_schema["const"])
                enum_values = property_schema.get("enum")
                if isinstance(enum_values, list):
                    expected_values.extend(enum_values)
                if expected_values:
                    constraints[str(property_name)] = expected_values
        branch_constraints.append(constraints)

    value_mapping = _mapping_for_value(value, union_properties)
    if value_mapping is None:
        return None

    constraint_names = set.intersection(*(set(constraints) for constraints in branch_constraints)) if branches else set()
    discriminators: dict[str, list[list[Any]]] = {}
    for property_name in constraint_names:
        values_by_branch = [constraints[property_name] for constraints in branch_constraints]
        first_values = values_by_branch[0]
        if any(
            len(values) != len(first_values) or any(value not in first_values for value in values)
            for values in values_by_branch[1:]
        ):
            discriminators[property_name] = values_by_branch

    possible_branches = set(range(len(branches)))
    matched_discriminators = False
    for property_name, values_by_branch in discriminators.items():
        if property_name not in value_mapping:
            continue
        matched_discriminators = True
        actual_value = _plain_value(value_mapping[property_name])
        matching_branches = {
            index for index, expected_values in enumerate(values_by_branch) if actual_value in expected_values
        }
        possible_branches.intersection_update(matching_branches)

    return next(iter(possible_branches)) if matched_discriminators and len(possible_branches) == 1 else None


def _raise_unknown_key(key: object, pointer: str, schema: Mapping[str, Any], operation: str) -> None:
    object_name = _schema_label(pointer, schema, operation)
    raise ClosedRequestKeyError(f"Unknown key {key!r} for closed request object {object_name}.")


def _validate_value(value: object, schema: Mapping[str, Any], pointer: str, operation: str) -> None:
    schema, pointer = _resolve_schema(schema, pointer)

    for union_name in ("oneOf", "anyOf"):
        branches = schema.get(union_name)
        if not isinstance(branches, list):
            continue
        selected = _matching_union_branch(value, branches, f"{pointer}/{union_name}")
        if selected is not None:
            branch = branches[selected]
            if isinstance(branch, Mapping):
                _validate_value(value, branch, f"{pointer}/{union_name}/{selected}", operation)
            return

        branch_errors: list[ClosedRequestKeyError] = []
        branch_accepted = False
        for index, branch in enumerate(branches):
            if not isinstance(branch, Mapping):
                continue
            try:
                _validate_value(value, branch, f"{pointer}/{union_name}/{index}", operation)
            except ClosedRequestKeyError as error:
                branch_errors.append(error)
            else:
                branch_accepted = True
        if branch_accepted:
            return
        if branch_errors:
            raise branch_errors[0]

    all_of = schema.get("allOf")
    if isinstance(all_of, list):
        for index, branch in enumerate(all_of):
            if isinstance(branch, Mapping):
                _validate_value(value, branch, f"{pointer}/allOf/{index}", operation)

    properties = schema.get("properties")
    additional_properties = schema.get("additionalProperties")
    is_object = schema.get("type") == "object" or isinstance(properties, Mapping) or additional_properties is not None
    if is_object:
        property_schemas = properties if isinstance(properties, Mapping) else {}
        property_names = {str(name) for name in property_schemas}
        value_mapping = _mapping_for_value(value, property_names)
        if value_mapping is None:
            return

        if additional_properties is False:
            for key in value_mapping:
                if not isinstance(key, str) or key not in property_schemas:
                    _raise_unknown_key(key, pointer, schema, operation)

        for key, child_value in value_mapping.items():
            child_schema: object | None = property_schemas.get(key) if isinstance(key, str) else None
            child_pointer = f"{pointer}/properties/{_escape_pointer_token(str(key))}"
            if child_schema is None and isinstance(additional_properties, Mapping):
                child_schema = additional_properties
                child_pointer = f"{pointer}/additionalProperties"
            if isinstance(child_schema, Mapping):
                _validate_value(child_value, child_schema, child_pointer, operation)

    items = schema.get("items")
    if isinstance(items, Mapping) and isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            _validate_value(item, items, f"{pointer}/items", operation)


def validate_request_body(body: object, schema_pointer: str, operation: str) -> None:
    """Reject unknown keys anywhere in a request body covered by the vendored schema."""
    schema = _SCHEMAS.get(schema_pointer)
    if isinstance(schema, Mapping):
        _validate_value(body, schema, schema_pointer, operation)


def _reject_model_unknown_keys(model_name: str, data: Mapping[str, Any]) -> None:
    allowed_keys = _CLOSED_REQUEST_MODEL_FIELDS.get(model_name)
    if allowed_keys is None:
        return
    for key in data:
        if not isinstance(key, str) or key not in allowed_keys:
            raise ClosedRequestKeyError(f"Unknown key {key!r} for closed request object {model_name}.")


def _install_model_guards() -> None:
    models = importlib.import_module("plainrouter.generated.models")

    for model_name, model in vars(models).items():
        allowed_keys = _CLOSED_REQUEST_MODEL_FIELDS.get(model_name)
        if allowed_keys is None or not isinstance(model, type):
            continue
        from_dict = getattr(model, "from_dict", None)
        if not isinstance(from_dict, classmethod) and not callable(from_dict):
            continue
        original = cast(Callable[..., Any], getattr(from_dict, "__func__", from_dict))
        if getattr(original, "_plainrouter_closed_object_guard", False):
            continue

        def guarded_from_dict(
            cls: type[Any],
            src_dict: Mapping[str, Any],
            _original: Callable[..., Any] = original,
            _model_name: str = model_name,
        ) -> Any:
            _reject_model_unknown_keys(_model_name, src_dict)
            return _original(cls, src_dict)

        setattr(guarded_from_dict, "_plainrouter_closed_object_guard", True)
        setattr(model, "from_dict", classmethod(guarded_from_dict))


def _operation_for_function(function: Callable[..., Any]) -> tuple[str, str] | None:
    constants = function.__code__.co_consts
    method = next((value for value in constants if isinstance(value, str) and value in _HTTP_METHODS), None)
    path = next((value for value in constants if isinstance(value, str) and value.startswith("/")), None)
    if method is None or path is None:
        return None
    return method.upper(), path


def _install_operation_guards() -> None:
    api_package = importlib.import_module("plainrouter.generated.api")

    for module_info in pkgutil.walk_packages(api_package.__path__, f"{api_package.__name__}."):
        module = importlib.import_module(module_info.name)
        function = getattr(module, "_get_kwargs", None)
        if not callable(function):
            continue
        operation = _operation_for_function(function)
        if operation is None:
            continue
        operation_name = f"{operation[0]} {operation[1]}"
        schema_pointer = _OPERATIONS.get(operation_name)
        if schema_pointer is None:
            continue
        if getattr(function, "_plainrouter_closed_object_guard", False):
            continue

        signature = inspect.signature(function)

        @wraps(function)
        def guarded_get_kwargs(
            *args: Any,
            _function: Callable[..., Any] = function,
            _signature: inspect.Signature = signature,
            _schema_pointer: str = schema_pointer,
            _operation_name: str = operation_name,
            **kwargs: Any,
        ) -> Any:
            bound = _signature.bind_partial(*args, **kwargs)
            body = bound.arguments.get("body")
            if body is not None:
                validate_request_body(body, _schema_pointer, _operation_name)
            return _function(*args, **kwargs)

        setattr(guarded_get_kwargs, "_plainrouter_closed_object_guard", True)
        setattr(module, "_get_kwargs", guarded_get_kwargs)


def _install_generated_client_guards() -> None:
    generated_client = importlib.import_module("plainrouter.generated.client")

    for class_name in ("Client", "AuthenticatedClient"):
        client_class = getattr(generated_client, class_name)
        for method_name, httpx_type, request_hook in (
            ("get_httpx_client", Client, check_closed_request_objects),
            ("get_async_httpx_client", AsyncClient, check_closed_request_objects_async),
        ):
            original = getattr(client_class, method_name)
            if getattr(original, "_plainrouter_closed_object_guard", False):
                continue

            def guarded_get_httpx_client(
                self: Any,
                _original: Callable[..., Any] = original,
                _httpx_type: type[Any] = httpx_type,
                _request_hook: Callable[..., Any] = request_hook,
            ) -> Any:
                client = _original(self)
                if isinstance(client, _httpx_type) and _request_hook not in client.event_hooks["request"]:
                    client.event_hooks["request"].append(_request_hook)
                return client

            setattr(guarded_get_httpx_client, "_plainrouter_closed_object_guard", True)
            setattr(client_class, method_name, guarded_get_httpx_client)


def install_closed_object_guards() -> None:
    """Install guards on generated mapping converters and request builders."""
    _install_model_guards()
    _install_operation_guards()
    _install_generated_client_guards()


def _request_path_matches(template: str, actual_path: str) -> bool:
    pattern = re.sub(r"\\\{[^{}]+\\\}", r"[^/]+", re.escape(template))
    return re.search(f"{pattern}/?$", actual_path) is not None


def _request_schema(request: Request) -> tuple[str, str] | None:
    path = request.url.path or "/"
    for operation_name, schema_pointer in _OPERATIONS.items():
        method, template = operation_name.split(" ", 1)
        if request.method.upper() == method and _request_path_matches(template, path):
            return schema_pointer, operation_name
    return None


def check_closed_request_objects(request: Request) -> None:
    """Validate JSON request bodies from SDK-managed custom httpx clients."""
    request_schema = _request_schema(request)
    if request_schema is None:
        return

    content_type = request.headers.get("content-type", "").split(";", 1)[0].strip().lower()
    if content_type != "application/json":
        return

    try:
        body_content = request.content
    except RequestNotRead:
        body_content = request.read()

    _validate_json_request_body(body_content, request_schema)


async def check_closed_request_objects_async(request: Request) -> None:
    """Validate streamed JSON bodies in SDK-managed async httpx clients."""
    request_schema = _request_schema(request)
    if request_schema is None:
        return

    content_type = request.headers.get("content-type", "").split(";", 1)[0].strip().lower()
    if content_type != "application/json":
        return

    try:
        body_content = request.content
    except RequestNotRead:
        body_content = await request.aread()

    _validate_json_request_body(body_content, request_schema)


def _validate_json_request_body(body_content: bytes, request_schema: tuple[str, str]) -> None:
    try:
        body = json.loads(body_content)
    except (json.JSONDecodeError, TypeError):
        return

    schema_pointer, operation_name = request_schema
    validate_request_body(body, schema_pointer, operation_name)
