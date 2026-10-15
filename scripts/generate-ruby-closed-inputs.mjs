import fs from "node:fs";
import path from "node:path";

const [manifestPath, specificationPath, libraryPath] = process.argv.slice(2);

if (!manifestPath || !specificationPath || !libraryPath) {
  throw new Error("usage: node scripts/generate-ruby-closed-inputs.mjs MANIFEST SPECIFICATION RUBY_LIBRARY_DIRECTORY");
}

const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const specification = JSON.parse(fs.readFileSync(specificationPath, "utf8"));
const schemas = manifest.schemas;
const ruby = {
  operation_ids: {},
  input_models: {},
};

function methodPathKey(method, route) {
  return `${method.toUpperCase()} ${route}`;
}

function rubyOperationName(operationId) {
  return operationId
    .replace(/([a-z0-9])([A-Z])/g, "$1_$2")
    .replace(/[.-]/g, "_")
    .toLowerCase();
}

function parseMethodBlock(source, methodName) {
  const expression = new RegExp(`^\\s*def (?:self\\.)?${methodName}\\b([\\s\\S]*?)^\\s*end\\s*$`, "m");
  return source.match(expression)?.[1] ?? "";
}

function parseRubyMap(source, methodName) {
  const body = parseMethodBlock(source, methodName);
  const values = {};

  for (const match of body.matchAll(/:'([^']+)'\s*=>\s*:'([^']+)'/g)) {
    values[match[1]] = match[2];
  }

  return values;
}

function parseModelInformation() {
  const modelsDirectory = path.join(libraryPath, "openapi", "models");
  const modelInformation = new Map();
  const unionInformation = new Map();

  for (const filename of fs.readdirSync(modelsDirectory).filter((entry) => entry.endsWith(".rb"))) {
    const source = fs.readFileSync(path.join(modelsDirectory, filename), "utf8");
    const modelName = source.match(/^\s*class (\w+) < ApiModelBase/m)?.[1];
    const unionName = source.match(/^\s*module (\w+)\s*$/m)?.[1];

    if (modelName) {
      const attributeMap = parseRubyMap(source, "attribute_map");
      const openapiTypes = parseRubyMap(source, "openapi_types");
      const typeByJsonName = {};

      for (const [rubyName, jsonName] of Object.entries(attributeMap)) {
        if (openapiTypes[rubyName] !== undefined) {
          typeByJsonName[jsonName] = openapiTypes[rubyName];
        }
      }

      modelInformation.set(modelName, {
        properties: Object.values(attributeMap).sort(),
        typeByJsonName,
      });
    }

    if (unionName) {
      const alternatives = [];

      for (const methodName of ["openapi_any_of", "openapi_one_of", "openapi_all_of"]) {
        const body = parseMethodBlock(source, methodName);
        if (body === "") {
          continue;
        }

        for (const match of body.matchAll(/:'([^']+)'/g)) {
          alternatives.push(match[1]);
        }
      }

      if (alternatives.length > 0) {
        unionInformation.set(unionName, alternatives);
      }
    }
  }

  return { modelInformation, unionInformation };
}

function resolvePointer(pointer) {
  const seen = new Set();
  let currentPointer = pointer;

  while (true) {
    if (seen.has(currentPointer)) {
      throw new Error(`schema reference cycle at ${currentPointer}`);
    }
    seen.add(currentPointer);

    const node = schemas[currentPointer];
    if (!node) {
      throw new Error(`missing normalized schema ${currentPointer}`);
    }

    if (typeof node.$ref !== "string") {
      return { pointer: currentPointer, node };
    }

    currentPointer = node.$ref;
  }
}

function schemaProperties(pointer, visited = new Set()) {
  const { node } = resolvePointer(pointer);
  const result = { ...(node.properties ?? {}) };

  for (const child of node.allOf ?? []) {
    const childPointer = child.$ref;
    if (!childPointer || visited.has(childPointer)) {
      continue;
    }
    visited.add(childPointer);
    Object.assign(result, schemaProperties(childPointer, visited));
  }

  return result;
}

function schemaContainsClosedObject(pointer, visited = new Set()) {
  const { pointer: resolvedPointer, node } = resolvePointer(pointer);
  if (visited.has(resolvedPointer)) {
    return false;
  }
  visited.add(resolvedPointer);

  if (node.additionalProperties === false) {
    return true;
  }

  const childPointers = [
    ...Object.values(schemaProperties(resolvedPointer)).map((property) => property.$ref),
    node.items?.$ref,
    typeof node.additionalProperties === "object" ? node.additionalProperties.$ref : null,
    ...(node.allOf ?? []).map((branch) => branch.$ref),
    ...(node.oneOf ?? []).map((branch) => branch.$ref),
    ...(node.anyOf ?? []).map((branch) => branch.$ref),
  ].filter(Boolean);

  return childPointers.some((childPointer) => schemaContainsClosedObject(childPointer, visited));
}

function innerType(type) {
  if (!type) {
    return null;
  }

  const array = type.match(/^Array<(.+)>$/);
  if (array) {
    return array[1];
  }

  const hash = type.match(/^Hash<String, (.+)>$/);
  if (hash) {
    return hash[1];
  }

  return type;
}

function branchType(unionName, keyword, index, unionInformation, modelInformation) {
  const alternatives = unionInformation.get(unionName) ?? [];
  const expectedBase = `${unionName}${keyword[0].toUpperCase()}${keyword.slice(1)}`;
  const expectedName = `${expectedBase}${index === 0 ? "" : index}`;
  const found = alternatives.find((name) => name === expectedName);

  if (found) {
    return found;
  }

  if (modelInformation.has(expectedName) || unionInformation.has(expectedName)) {
    return expectedName;
  }

  return null;
}

function findOperationBodyModel(operationId, operationPointer, modelInformation) {
  const rawRoot = schemas[operationPointer];
  if (rawRoot?.$ref) {
    const componentName = rawRoot.$ref.match(/^#\/components\/schemas\/([^/]+)$/)?.[1];
    if (componentName && modelInformation.has(componentName)) {
      return componentName;
    }
  }

  const apiDirectory = path.join(libraryPath, "openapi", "api");
  const marker = new RegExp(`:operation\\s*=>\\s*:["']\\w+\\.${operationId}["']`);

  for (const filename of fs.readdirSync(apiDirectory).filter((entry) => entry.endsWith(".rb"))) {
    const source = fs.readFileSync(path.join(apiDirectory, filename), "utf8");
    const markerMatch = marker.exec(source);
    if (!markerMatch) {
      continue;
    }

    const methodStart = source.lastIndexOf(`def ${operationId}_with_http_info`, markerMatch.index);
    if (methodStart < 0) {
      continue;
    }

    const methodPrefix = source.slice(methodStart, markerMatch.index);
    const bodyExpression = methodPrefix.match(/object_to_http_body\(([^)]+)\)/)?.[1]?.trim();
    if (!bodyExpression) {
      continue;
    }

    const bodyParameter = bodyExpression.match(/opts\[:'?([^'\]]+)'?\]/)?.[1] ?? bodyExpression;
    const documentation = source.slice(Math.max(0, methodStart - 10000), methodStart);
    const parameterTypes = [...documentation.matchAll(/^\s*# @param ([^\s]+) \[([^\]]+)\]/gm)];
    const optionTypes = [...documentation.matchAll(/^\s*# @option opts \[([^\]]+)\] :?([^\s]+)/gm)];
    const bodyType = parameterTypes.find((match) => match[1] === bodyParameter)?.[2]
      ?? optionTypes.find((match) => match[2] === bodyParameter)?.[1];

    if (bodyType && modelInformation.has(bodyType)) {
      return bodyType;
    }
  }

  return null;
}

function collectClosedInputModels(rootPointer, rootModel, modelInformation, unionInformation, modelSchemas) {
  const visited = new Set();

  function visit(pointer, modelType) {
    if (!pointer) {
      return;
    }

    const { pointer: resolvedPointer, node } = resolvePointer(pointer);
    const visitKey = `${resolvedPointer}|${modelType ?? ""}`;
    if (visited.has(visitKey)) {
      return;
    }
    visited.add(visitKey);

    const normalizedType = innerType(modelType);

    for (const keyword of ["allOf", "anyOf", "oneOf"]) {
      if (!Array.isArray(node[keyword])) {
        continue;
      }

      node[keyword].forEach((alternative, index) => {
        const alternativeType = normalizedType
          ? branchType(normalizedType, keyword, index, unionInformation, modelInformation)
          : null;
        if (alternative.$ref) {
          visit(alternative.$ref, alternativeType);
        }
      });
    }

    if (node.items?.$ref) {
      visit(node.items.$ref, normalizedType);
    }

    if (node.additionalProperties && typeof node.additionalProperties === "object" && node.additionalProperties.$ref) {
      visit(node.additionalProperties.$ref, normalizedType);
    }

    const properties = schemaProperties(resolvedPointer);
    const typeInformation = normalizedType ? modelInformation.get(normalizedType) : null;
    const propertyNames = Object.keys(properties).sort();

    if (normalizedType && (modelInformation.has(normalizedType) || unionInformation.has(normalizedType)) &&
      schemaContainsClosedObject(resolvedPointer)) {
      modelSchemas[normalizedType] ??= [];
      if (!modelSchemas[normalizedType].includes(resolvedPointer)) {
        modelSchemas[normalizedType].push(resolvedPointer);
      }
    }

    if (node.additionalProperties === false && typeInformation &&
      JSON.stringify(propertyNames) === JSON.stringify(typeInformation.properties)) {
      modelSchemas[normalizedType] ??= [];
      if (!modelSchemas[normalizedType].includes(resolvedPointer)) {
        modelSchemas[normalizedType].push(resolvedPointer);
      }
    }

    for (const [propertyName, propertyPointer] of Object.entries(properties)) {
      const propertyType = typeInformation?.typeByJsonName[propertyName] ?? null;
      if (propertyPointer?.$ref) {
        visit(propertyPointer.$ref, propertyType);
      }
    }
  }

  visit(rootPointer, rootModel);
}

for (const [route, pathItem] of Object.entries(specification.paths ?? {})) {
  for (const [method, operation] of Object.entries(pathItem)) {
    if (!operation?.operationId || !manifest.operations[methodPathKey(method, route)]) {
      continue;
    }

    const pointer = manifest.operations[methodPathKey(method, route)];
    ruby.operation_ids[rubyOperationName(operation.operationId)] = pointer;
  }
}

const { modelInformation, unionInformation } = parseModelInformation();

for (const [operationId, pointer] of Object.entries(ruby.operation_ids)) {
  const bodyModel = findOperationBodyModel(operationId, pointer, modelInformation);
  collectClosedInputModels(pointer, bodyModel, modelInformation, unionInformation, ruby.input_models);
}

for (const modelNames of Object.values(ruby.input_models)) {
  modelNames.sort();
}

manifest.ruby = ruby;
fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
