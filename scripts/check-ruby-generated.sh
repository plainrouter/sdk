#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/plainrouter-ruby-drift.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

"$ROOT/scripts/generate-ruby.sh" "$WORK"

diff -ru "$ROOT/packages/ruby/lib/plainrouter/openapi.rb" "$WORK/lib/plainrouter/openapi.rb"
diff -ru "$ROOT/packages/ruby/lib/plainrouter/openapi" "$WORK/lib/plainrouter/openapi"
diff -u "$ROOT/packages/ruby/lib/plainrouter/integer_input_fields.json" "$WORK/lib/plainrouter/integer_input_fields.json"
diff -u "$ROOT/packages/ruby/lib/plainrouter/closed_input_objects.json" "$WORK/lib/plainrouter/closed_input_objects.json"
