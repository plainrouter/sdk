#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/plainrouter-php-drift.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

"$ROOT/scripts/generate-php.sh" "$WORK"

diff -ru "$ROOT/packages/php/src/OpenAPI" "$WORK/src/OpenAPI"
diff -u "$ROOT/packages/php/src/integer-input-fields.json" "$WORK/src/integer-input-fields.json"
diff -ru "$ROOT/packages/php/src/IntegerInputApis" "$WORK/src/IntegerInputApis"
