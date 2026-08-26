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

    if project["version"] != specification["info"]["version"]:
        raise RuntimeError("Python package version must match the signed OpenAPI contract.")

    expected_urls = {
        "Homepage": "https://plainrouter.com",
        "Documentation": "https://docs.plainrouter.com/sdk/python",
        "Repository": "https://github.com/wudaku/plainrouter-sdk",
    }
    if urls != expected_urls:
        raise RuntimeError(f"Python project URLs do not identify PlainRouter: {urls!r}")

    print(f"Verified official PyPI metadata for plainrouter {project['version']}.")


if __name__ == "__main__":
    main()
