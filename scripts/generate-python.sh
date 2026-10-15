#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGE_OUTPUT="${1:-$ROOT/packages/python/src/plainrouter}"
SPEC="${2:-$ROOT/spec/openapi.json}"

openapi-python-client generate \
  --path "$SPEC" \
  --config "$ROOT/packages/python/openapi-python-client.json" \
  --meta none \
  --output-path "$PACKAGE_OUTPUT/generated" \
  --overwrite \
  --fail-on-warning

node "$ROOT/scripts/generate-integer-fields.mjs" "$PACKAGE_OUTPUT/_integer_fields.json" "$SPEC"
