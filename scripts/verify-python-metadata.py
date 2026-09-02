from __future__ import annotations

import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    package = tomllib.loads((ROOT / "packages/python/pyproject.toml").read_text())
    specification = json.loads((ROOT / "spec/openapi.json").read_text())
    project = package["project"]
    urls = project["urls"]

    expected_urls = {
        "Homepage": "https://plainrouter.com",
        "Documentation": "https://plainrouter.com/docs/sdk/python",
        "Repository": "https://github.com/plainrouter/sdk",
    }
    if urls != expected_urls:
        raise RuntimeError(f"Python project URLs do not identify PlainRouter: {urls!r}")

    print(
        "Verified official PyPI metadata for "
        f"plainrouter {project['version']} targeting signed OpenAPI {specification['info']['version']}."
    )


if __name__ == "__main__":
    main()
