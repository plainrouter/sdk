from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import tomllib
from pathlib import Path

EXPECTED_ACTOR = "bursteri"
ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    tag = os.environ.get("GITHUB_REF_NAME") or (
        sys.argv[1] if len(sys.argv) > 1 else None
    )
    if tag is None:
        raise RuntimeError(
            "Release tag is required via GITHUB_REF_NAME or the first argument."
        )

    match = re.fullmatch(r"python-v(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)", tag)
    if match is None:
        raise RuntimeError(f"Release tag {tag} must use the python-v*.*.* format.")

    actor = os.environ.get("GITHUB_ACTOR")
    if actor is not None and actor != EXPECTED_ACTOR:
        raise RuntimeError(
            f"Python release tags must be pushed by {EXPECTED_ACTOR}, not {actor}."
        )

    release_version = match.group(1)
    package = tomllib.loads((ROOT / "packages/python/pyproject.toml").read_text())
    generator_config = json.loads(
        (ROOT / "packages/python/openapi-python-client.json").read_text()
    )
    spec_bytes = (ROOT / "spec/openapi.json").read_bytes()
    specification = json.loads(spec_bytes)
    checksum = parse_checksum(ROOT / "spec/CHECKSUM")
    actual_hash = hashlib.sha256(spec_bytes).hexdigest()

    versions = {
        "packages/python/pyproject.toml": package["project"]["version"],
        "packages/python/openapi-python-client.json": generator_config[
            "package_version_override"
        ],
        "spec/openapi.json": specification["info"]["version"],
        "spec/CHECKSUM": checksum["info.version"],
    }
    for source, version in versions.items():
        if version != release_version:
            raise RuntimeError(f"{source} version {version} does not match tag {tag}.")

    if specification.get("x-signed") is not True:
        raise RuntimeError("The vendored OpenAPI contract is not signed.")
    if checksum["sha256"] != actual_hash:
        raise RuntimeError(
            f"Vendored spec hash {actual_hash} does not match spec/CHECKSUM {checksum['sha256']}."
        )

    print(
        f"Verified {tag} against Python package {release_version} and the signed OpenAPI contract."
    )


def parse_checksum(path: Path) -> dict[str, str]:
    return dict(line.split(": ", 1) for line in path.read_text().splitlines() if line)


if __name__ == "__main__":
    main()
