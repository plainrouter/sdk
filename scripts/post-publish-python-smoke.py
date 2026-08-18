from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

IMPORT_SMOKE = """
from plainrouter import (
    create_client,
    create_event,
    delete_user_data,
    get_emq_report,
    get_event,
    get_reconciliation_report,
    list_events,
    replay_deliveries,
    send_test_purchase,
    set_destination_test_mode,
)
assert create_client
"""


def main() -> None:
    tag = os.environ.get("GITHUB_REF_NAME") or (
        sys.argv[1] if len(sys.argv) > 1 else None
    )
    if tag is None:
        raise RuntimeError("Python release tag is required.")
    match = re.fullmatch(r"python-v(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)", tag)
    if match is None:
        raise RuntimeError(f"Invalid Python release tag: {tag}")

    version = match.group(1)
    last_error: subprocess.CalledProcessError | None = None
    for attempt in range(1, 6):
        directory = Path(tempfile.mkdtemp(prefix="plainrouter-pypi-smoke-"))
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", directory / "venv"], check=True
            )
            python = directory / "venv/bin/python"
            subprocess.run(
                [
                    python,
                    "-m",
                    "pip",
                    "install",
                    "--disable-pip-version-check",
                    f"plainrouter=={version}",
                ],
                check=True,
            )
            subprocess.run(
                [python, "-c", IMPORT_SMOKE],
                check=True,
            )
            print(f"Verified published plainrouter {version} from PyPI.")
            return
        except subprocess.CalledProcessError as error:
            last_error = error
            if attempt < 5:
                time.sleep(10)
        finally:
            shutil.rmtree(directory, ignore_errors=True)

    raise RuntimeError(
        f"PyPI package was not installable after five attempts: {last_error}"
    )


if __name__ == "__main__":
    main()
