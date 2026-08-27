#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/generate-ruby.sh OUTPUT_DIRECTORY" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$1"
JAVA_BIN="${JAVA_BIN:-java}"
GENERATOR_VERSION="7.25.0"
GENERATOR_SHA256="41ce4f6b07f196676439d710759fa1ced7a08066d06ff1bf314681470289efae"
GENERATOR_CACHE="${TMPDIR:-/tmp}/plainrouter-openapi-generator"
GENERATOR_JAR="$GENERATOR_CACHE/openapi-generator-cli-$GENERATOR_VERSION.jar"

mkdir -p "$GENERATOR_CACHE" "$OUTPUT"

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

"$JAVA_BIN" -jar "$GENERATOR_JAR" generate \
  -g ruby \
  -i "$ROOT/spec/openapi.json" \
  -o "$OUTPUT" \
  --global-property=models,apis,supportingFiles,modelDocs=false,apiDocs=false,modelTests=false,apiTests=false \
  --additional-properties="gemName=plainrouter/openapi,moduleName=PlainRouter::OpenAPI,gemVersion=0.1.0,gemRequiredRubyVersion=>= 3.2,library=faraday,gemAuthor=PlainRouter,gemLicense=Apache-2.0,gemHomepage=https://github.com/plainrouter/sdk,gemSummary=Official PlainRouter Ruby SDK,gemDescription=Ruby SDK generated from the signed PlainRouter OpenAPI contract,hideGenerationTimestamp=true,disallowAdditionalPropertiesIfNotPresent=false"

find "$OUTPUT/lib/plainrouter" -type f -name '*.rb' -print0 \
  | xargs -0 perl -pi -e 's/[ \t]+$//'
