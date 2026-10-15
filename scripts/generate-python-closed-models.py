#!/usr/bin/env python3
"""Write generated Python model fields for closed request objects."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from openapi_python_client import Config
from openapi_python_client.config import ConfigFile, MetaType
from openapi_python_client.parser import GeneratorData
from openapi_python_client.parser.properties.list_property import ListProperty
from openapi_python_client.parser.properties.model_property import ModelProperty
from openapi_python_client.parser.properties.union import UnionProperty


def request_models(spec_path: Path, config_path: Path) -> dict[str, list[str]]:
    """Return closed model classes reachable from request bodies."""
    config = Config.from_sources(
        ConfigFile.load_from_path(config_path),
        MetaType.NONE,
        spec_path,
        "utf-8",
        False,
        None,
    )
    generator_data = GeneratorData.from_dict(json.loads(spec_path.read_text()), config=config)
    if not isinstance(generator_data, GeneratorData):
        raise RuntimeError("The OpenAPI document could not be parsed by openapi-python-client.")

    closed_models: dict[str, list[str]] = {}
    visited: set[int] = set()

    def visit(prop: Any) -> None:
        if prop is None or id(prop) in visited:
            return
        visited.add(id(prop))

        if isinstance(prop, ModelProperty):
            if prop.additional_properties is None:
                closed_models[str(prop.class_info.name)] = list((prop.data.properties or {}).keys())
            for child in (prop.required_properties or []) + (prop.optional_properties or []):
                visit(child)
        elif isinstance(prop, ListProperty):
            visit(prop.inner_property)
        elif isinstance(prop, UnionProperty):
            for child in prop.inner_properties:
                visit(child)

    for collection in generator_data.endpoint_collections_by_tag.values():
        for endpoint in collection.endpoints:
            for body in endpoint.bodies:
                visit(body.prop)

    return dict(sorted(closed_models.items()))


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: generate-python-closed-models.py SPEC CONFIG OUTPUT")

    spec_path, config_path, output_path = (Path(value) for value in sys.argv[1:])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(request_models(spec_path, config_path), indent=2) + "\n")


if __name__ == "__main__":
    main()
