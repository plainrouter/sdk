from __future__ import annotations

import sys
import tarfile
import zipfile
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 3:
        raise RuntimeError("Usage: verify-python-dist.py WHEEL SDIST")

    wheel = Path(sys.argv[1])
    sdist = Path(sys.argv[2])
    with zipfile.ZipFile(wheel) as archive:
        wheel_files = sorted(name for name in archive.namelist() if not name.endswith("/"))
    with tarfile.open(sdist, "r:gz") as archive:
        sdist_files = sorted(member.name for member in archive.getmembers() if member.isfile())

    assert_distribution_is_clean(wheel_files, "wheel")
    assert_distribution_is_clean(sdist_files, "sdist")
    require_suffix(wheel_files, "plainrouter/__init__.py", "wheel")
    require_suffix(wheel_files, "plainrouter/client.py", "wheel")
    require_suffix(wheel_files, "plainrouter/py.typed", "wheel")
    require_suffix(wheel_files, ".dist-info/licenses/LICENSE", "wheel")
    require_suffix(sdist_files, "/src/plainrouter/py.typed", "sdist")
    require_suffix(sdist_files, "/README.md", "sdist")
    require_suffix(sdist_files, "/LICENSE", "sdist")

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


if __name__ == "__main__":
    main()
