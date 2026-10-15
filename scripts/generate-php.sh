#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/generate-php.sh OUTPUT_DIRECTORY" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$1"
JAVA_BIN="${JAVA_BIN:-java}"
GENERATOR_VERSION="7.25.0"
GENERATOR_SHA256="41ce4f6b07f196676439d710759fa1ced7a08066d06ff1bf314681470289efae"
GENERATOR_CACHE="${TMPDIR:-/tmp}/plainrouter-openapi-generator"
GENERATOR_JAR="$GENERATOR_CACHE/openapi-generator-cli-$GENERATOR_VERSION.jar"
GENERATOR_OUTPUT="$(mktemp -d "${TMPDIR:-/tmp}/plainrouter-php-output.XXXXXX")"

mkdir -p "$GENERATOR_CACHE" "$OUTPUT/src"
GENERATOR_INPUT="$(mktemp "${TMPDIR:-/tmp}/plainrouter-php-input.XXXXXX.json")"
trap 'rm -f "$GENERATOR_INPUT"; rm -rf "$GENERATOR_OUTPUT"' EXIT

node "$ROOT/scripts/generate-closed-objects.mjs" "$OUTPUT/src/closed-input-objects.json" "$ROOT/spec/openapi.json"

if [[ ! -f "$GENERATOR_JAR" ]]; then
  curl --fail --location --silent --show-error \
    "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$GENERATOR_VERSION/openapi-generator-cli-$GENERATOR_VERSION.jar" \
    --output "$GENERATOR_JAR"
fi

ACTUAL_SHA256="$(shasum -a 256 "$GENERATOR_JAR" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$GENERATOR_SHA256" ]]; then
  echo "OpenAPI Generator checksum mismatch: $ACTUAL_SHA256" >&2
  exit 1
fi

node "$ROOT/scripts/verify-spec.mjs"

node "$ROOT/scripts/prepare-generator-input.mjs" "$ROOT/spec/openapi.json" "$GENERATOR_INPUT" --omit-page-defaults

"$JAVA_BIN" -jar "$GENERATOR_JAR" generate \
  -g php \
  -i "$GENERATOR_INPUT" \
  -o "$GENERATOR_OUTPUT" \
  --global-property=models,apis,supportingFiles,modelDocs=false,apiDocs=false,modelTests=false,apiTests=false \
  --additional-properties='invokerPackage=Plainrouter\OpenAPI,srcBasePath=src/OpenAPI,artifactVersion=0.4.0,hideGenerationTimestamp=true,disallowAdditionalPropertiesIfNotPresent=false'

find "$GENERATOR_OUTPUT/src/OpenAPI" -type f -name '*.php' -print0 \
  | xargs -0 perl -pi -e 's/[ \t]+$//'

rm -rf "$OUTPUT/src/OpenAPI"
cp -R "$GENERATOR_OUTPUT/src/OpenAPI" "$OUTPUT/src/OpenAPI"

INTEGER_FIELDS="$OUTPUT/src/integer-input-fields.json"
node "$ROOT/scripts/generate-integer-fields.mjs" "$INTEGER_FIELDS"
node "$ROOT/scripts/generate-php-integer-apis.mjs" \
  "$OUTPUT/src/OpenAPI/Api" \
  "$OUTPUT/src/IntegerInputApis" \
  "$INTEGER_FIELDS"
node "$ROOT/scripts/generate-php-closed-object-guards.mjs" \
  "$ROOT/spec/openapi.json" \
  "$OUTPUT/src/closed-input-objects.json" \
  "$OUTPUT/src/OpenAPI/Model" \
  "$OUTPUT/src/OpenAPI/Api"
