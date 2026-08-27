from __future__ import annotations

import sys
import tarfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) != 3:
        raise RuntimeError("Usage: verify-python-dist.py WHEEL SDIST")

    wheel = Path(sys.argv[1])
    sdist = Path(sys.argv[2])
    with zipfile.ZipFile(wheel) as archive:
        wheel_files = sorted(name for name in archive.namelist() if not name.endswith("/"))
        metadata_name = require_single_suffix(wheel_files, ".dist-info/METADATA", "wheel")
        metadata = archive.read(metadata_name).decode()
        entry_points_name = require_single_suffix(wheel_files, ".dist-info/entry_points.txt", "wheel")
        entry_points = archive.read(entry_points_name).decode()
    with tarfile.open(sdist, "r:gz") as archive:
        sdist_files = sorted(member.name for member in archive.getmembers() if member.isfile())

    assert_distribution_is_clean(wheel_files, "wheel")
    assert_distribution_is_clean(sdist_files, "sdist")
    require_suffix(wheel_files, "plainrouter/__init__.py", "wheel")
    require_suffix(wheel_files, "plainrouter/__main__.py", "wheel")
    require_suffix(wheel_files, "plainrouter/cli.py", "wheel")
    require_suffix(wheel_files, "plainrouter/client.py", "wheel")
    require_suffix(wheel_files, "plainrouter/py.typed", "wheel")
    require_suffix(wheel_files, ".dist-info/licenses/LICENSE", "wheel")
    require_suffix(sdist_files, "/src/plainrouter/py.typed", "sdist")
    require_suffix(sdist_files, "/src/plainrouter/__main__.py", "sdist")
    require_suffix(sdist_files, "/src/plainrouter/cli.py", "sdist")
    require_suffix(sdist_files, "/README.md", "sdist")
    require_suffix(sdist_files, "/LICENSE", "sdist")
    require_metadata(metadata)
    if "plainrouter = plainrouter.cli:main" not in entry_points.splitlines():
        raise RuntimeError("wheel entry points do not expose plainrouter.cli:main")

    print(f"Verified wheel contents ({len(wheel_files)} files):")
    print("\n".join(wheel_files))
    print(f"Verified sdist contents ({len(sdist_files)} files):")
    print("\n".join(sdist_files))


def assert_distribution_is_clean(files: list[str], label: str) -> None:
    forbidden = ("/tests/", "/test/", "/spec/", ".map", ".pyc", "__pycache__", ".env")
    offenders = [name for name in files if any(fragment in f"/{name}" for fragment in forbidden)]
    if offenders:
        raise RuntimeError(f"{label} contains forbidden files: {', '.join(offenders)}")


def require_suffix(files: list[str], suffix: str, label: str) -> None:
    if not any(name.endswith(suffix) for name in files):
        raise RuntimeError(f"{label} is missing required file ending in {suffix}")


def require_single_suffix(files: list[str], suffix: str, label: str) -> str:
    matches = [name for name in files if name.endswith(suffix)]
    if len(matches) != 1:
        raise RuntimeError(f"{label} must contain exactly one file ending in {suffix}")
    return matches[0]


def require_metadata(metadata: str) -> None:
    package = tomllib.loads((ROOT / "packages/python/pyproject.toml").read_text())
    version = package["project"]["version"]
    required_lines = {
        "Name: plainrouter",
        f"Version: {version}",
        "Project-URL: Homepage, https://plainrouter.com",
        "Project-URL: Documentation, https://docs.plainrouter.com/sdk/python",
        "Project-URL: Repository, https://github.com/plainrouter/sdk",
    }
    lines = set(metadata.splitlines())
    missing = sorted(required_lines - lines)
    if missing:
        raise RuntimeError(f"wheel metadata is missing official project identity: {', '.join(missing)}")


if __name__ == "__main__":
    main()
