import fs from "node:fs";
import path from "node:path";

const [libraryPath] = process.argv.slice(2);
if (!libraryPath) {
  throw new Error("usage: node scripts/patch-ruby-closed-inputs.mjs RUBY_LIBRARY_DIRECTORY");
}

const manifestPath = path.join(libraryPath, "closed_input_objects.json");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const inputModels = new Set(Object.keys(manifest.ruby?.input_models ?? {}));

function addRequire(filename) {
  let source = fs.readFileSync(filename, "utf8");
  const requiredLine = "require 'plainrouter/closed_input_validator'";
  if (source.includes(requiredLine)) {
    return;
  }

  const line = source.indexOf("\n", source.indexOf("=end")) + 1;
  source = `${source.slice(0, line)}\n${requiredLine}\n${source.slice(line)}`;
  fs.writeFileSync(filename, source);
}

for (const filename of [
  path.join(libraryPath, "openapi", "api_client.rb"),
  path.join(libraryPath, "openapi", "api_model_base.rb"),
]) {
  addRequire(filename);
}

const apiClientPath = path.join(libraryPath, "openapi", "api_client.rb");
let apiClient = fs.readFileSync(apiClientPath, "utf8");
const requestMethod = "    def build_request(http_method, path, request, opts = {})\n";
const requestGuard = "      ClosedInputValidator.validate_request!(http_method, path, opts)\n";

if (!apiClient.includes(requestGuard)) {
  if (!apiClient.includes(requestMethod)) {
    throw new Error("Ruby ApiClient#build_request was not found in generated output");
  }
  apiClient = apiClient.replace(requestMethod, `${requestMethod}${requestGuard}`);
  fs.writeFileSync(apiClientPath, apiClient);
}

const modelsDirectory = path.join(libraryPath, "openapi", "models");
for (const filename of fs.readdirSync(modelsDirectory).filter((entry) => entry.endsWith(".rb"))) {
  const modelPath = path.join(modelsDirectory, filename);
  let source = fs.readFileSync(modelPath, "utf8");
  const modelName = source.match(/^\s*class (\w+) < ApiModelBase/m)?.[1];
  const unionName = source.match(/^\s*module (\w+)\s*$/m)?.[1];
  const inputType = modelName || unionName;
  if (!inputType || !inputModels.has(inputType)) {
    continue;
  }

  if (modelName) {
    const initialize = "    def initialize(attributes = {})\n";
    const constructorGuard = "      ClosedInputValidator.validate_model!(self, attributes)\n";
    if (!source.includes(`${initialize}${constructorGuard}`)) {
      if (!source.includes(initialize)) {
        throw new Error(`Ruby ${modelName}#initialize was not found in generated output`);
      }
      source = source.replace(initialize, `${initialize}${constructorGuard}`);
    }
  }

  const buildFromHash = "    def self.build_from_hash(attributes)\n";
  const modelGuard = "      ClosedInputValidator.validate_model!(self, attributes)\n";
  if (modelName && !source.includes(`${buildFromHash}${modelGuard}`)) {
    if (!source.includes(buildFromHash)) {
      throw new Error(`Ruby ${modelName}#build_from_hash was not found in generated output`);
    }
    source = source.replace(buildFromHash, `${buildFromHash}${modelGuard}`);
  }

  const unionBuild = "      def build(data)\n";
  const unionGuard = "        ClosedInputValidator.validate_model!(self, data)\n";
  if (unionName && !source.includes(unionGuard)) {
    if (!source.includes(unionBuild)) {
      throw new Error(`Ruby ${unionName}.build was not found in generated output`);
    }
    source = source.replace(unionBuild, `${unionBuild}${unionGuard}`);
  }

  fs.writeFileSync(modelPath, source);
}
