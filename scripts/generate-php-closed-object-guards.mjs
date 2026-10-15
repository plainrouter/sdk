import { readFile, readdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';

const [specPath, manifestPath, modelDirectory, apiDirectory] = process.argv.slice(2);
if (!specPath || !manifestPath || !modelDirectory || !apiDirectory) {
  throw new Error('usage: generate-php-closed-object-guards.mjs SPEC MANIFEST MODEL_DIRECTORY API_DIRECTORY');
}

const spec = JSON.parse(await readFile(specPath, 'utf8'));
const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
const decodePointerPart = (part) => part.replaceAll('~1', '/').replaceAll('~0', '~');

function modelNameForPointer(pointer) {
  const parts = pointer.slice(2).split('/').map(decodePointerPart);
  let modelName;
  let index;

  if (parts[0] === 'components' && parts[1] === 'schemas') {
    modelName = parts[2];
    index = 3;
  } else if (parts[0] === 'paths') {
    const operation = spec.paths?.[parts[1]]?.[parts[2]];
    if (!operation?.operationId) {
      return null;
    }

    modelName = `${operation.operationId.replaceAll('.', '_')}_request`;
    index = parts.indexOf('schema') + 1;
  } else {
    return null;
  }

  if (index === 0) {
    return null;
  }

  for (; index < parts.length; index += 1) {
    const part = parts[index];
    if (part === 'properties') {
      modelName += `_${parts[++index]}`;
    } else if (part === 'items') {
      modelName += '_inner';
    } else if (['anyOf', 'oneOf', 'allOf'].includes(part)) {
      const variant = Number(parts[++index]);
      modelName += `_${part}${variant > 0 ? `_${variant}` : ''}`;
    }
  }

  return modelName;
}

function methodBody(source, methodStart, methodText) {
  const openingParen = methodStart + methodText.length - 1;
  let depth = 0;
  let closingParen = -1;
  for (let index = openingParen; index < source.length; index += 1) {
    if (source[index] === '(') depth += 1;
    if (source[index] === ')') {
      depth -= 1;
      if (depth === 0) {
        closingParen = index;
        break;
      }
    }
  }
  if (closingParen === -1) {
    throw new Error(`Could not parse method signature at offset ${methodStart}`);
  }

  const bodyStart = source.indexOf('{', closingParen);
  if (bodyStart === -1) {
    throw new Error(`Could not find method body at offset ${methodStart}`);
  }

  let depthBraces = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === '{') depthBraces += 1;
    if (source[index] === '}') {
      depthBraces -= 1;
      if (depthBraces === 0) {
        return { bodyStart, bodyEnd: index };
      }
    }
  }
  throw new Error(`Could not find method end at offset ${methodStart}`);
}

function insertAfterOpeningBrace(source, methodStart, methodText, line) {
  const { bodyStart } = methodBody(source, methodStart, methodText);
  return `${source.slice(0, bodyStart + 1)}\n        ${line}${source.slice(bodyStart + 1)}`;
}

const modelFiles = (await readdir(modelDirectory)).filter((file) => file.endsWith('.php')).sort();
const staticNames = new Map();
for (const file of modelFiles) {
  const source = await readFile(join(modelDirectory, file), 'utf8');
  const modelName = source.match(/protected static \$openAPIModelName = '([^']+)'/)?.[1];
  if (modelName) {
    staticNames.set(modelName, file);
  }
}

const pointersByModel = new Map();
for (const [pointer] of Object.entries(manifest.schemas)) {
  const schema = resolveSchema(pointer, manifest.schemas);
  if (schema.type !== 'object' && !schema.properties && !schema.anyOf && !schema.oneOf && !schema.allOf) {
    continue;
  }

  const modelName = modelNameForPointer(pointer);
  if (modelName && staticNames.has(modelName)) {
    const pointers = pointersByModel.get(modelName) ?? [];
    pointers.push(pointer);
    pointersByModel.set(modelName, pointers);
  }
}

for (const [modelName, pointers] of pointersByModel) {
  if (pointers.length > 1) {
    throw new Error(`Multiple spec nodes map to PHP model ${modelName}: ${pointers.join(', ')}`);
  }
}

for (const [modelName, [pointer]] of pointersByModel) {
  const file = staticNames.get(modelName);
  const path = join(modelDirectory, file);
  let source = await readFile(path, 'utf8');

  const constructorMatch = source.match(/public function __construct\s*\(/);
  if (!constructorMatch) {
    throw new Error(`Mapped PHP model ${file} has no array constructor`);
  }
  const constructorStart = constructorMatch.index;
  const constructorText = constructorMatch[0];
  if (!source.slice(constructorStart, source.indexOf('\n    }', constructorStart)).includes('ClosedObjectGuard::assertModelInput')) {
    source = insertAfterOpeningBrace(
      source,
      constructorStart,
      constructorText,
      `\\Plainrouter\\ClosedObjectGuard::assertModelInput(self::class, $data ?? []);`,
    );
  }

  const rootSchema = resolveSchema(pointer, manifest.schemas);
  if (rootSchema.additionalProperties === false) {
    const offsetSetMatch = source.match(/public function offsetSet\s*\(/);
    if (!offsetSetMatch) {
      throw new Error(`Closed PHP model ${file} has no ArrayAccess::offsetSet`);
    }
    const offsetSetStart = offsetSetMatch.index;
    if (!source.slice(offsetSetStart, source.indexOf('\n    }', offsetSetStart)).includes('ClosedObjectGuard::assertClosedModelKeyForModel')) {
      source = insertAfterOpeningBrace(
        source,
        offsetSetStart,
        offsetSetMatch[0],
        '\\Plainrouter\\ClosedObjectGuard::assertClosedModelKeyForModel(self::class, $offset);',
      );
    }

    if (!source.includes('public function __set(string $name, mixed $value): void')) {
      const offsetExistsStart = source.indexOf('public function offsetExists(');
      if (offsetExistsStart === -1) {
        throw new Error(`Closed PHP model ${file} has no ArrayAccess::offsetExists`);
      }
      const offsetExistsDocStart = source.lastIndexOf('/**', offsetExistsStart);
      source = `${source.slice(0, offsetExistsDocStart)}/**
     * Sets a property using the generated model's existing dynamic-property behavior.
     *
     * @param string $name Property name
     * @param mixed $value Property value
     */
    public function __set(string $name, mixed $value): void
    {
        \\Plainrouter\\ClosedObjectGuard::assertClosedModelKeyForModel(self::class, $name);
        $setDynamicProperty = \\Closure::bind(
            function () use ($name, $value): void {
                $this->{$name} = $value;
            },
            $this,
            self::class,
        );
        $setDynamicProperty();
    }

    ${source.slice(offsetExistsDocStart)}`;
    }
  }

  await writeFile(path, source);
}

const modelMap = Object.fromEntries([...pointersByModel].map(([modelName, [pointer]]) => [modelName, pointer]));
await writeFile(
  join(dirname(manifestPath), 'closed-input-models.json'),
  `${JSON.stringify(modelMap, null, 2)}\n`,
);

const serializerPath = join(dirname(modelDirectory), 'ObjectSerializer.php');
let serializer = await readFile(serializerPath, 'utf8');
const deserializeMatch = serializer.match(/public static function deserialize\s*\(/);
if (!deserializeMatch) {
  throw new Error('Could not locate generated ObjectSerializer::deserialize');
}
if (!serializer.slice(deserializeMatch.index, serializer.indexOf('\n    }', deserializeMatch.index)).includes('ClosedObjectGuard::assertModelInput')) {
  serializer = insertAfterOpeningBrace(
    serializer,
    deserializeMatch.index,
    deserializeMatch[0],
    '\\Plainrouter\\ClosedObjectGuard::assertModelInput($class, $data);',
  );
}
await writeFile(serializerPath, serializer);

const apiFiles = (await readdir(apiDirectory)).filter((file) => file.endsWith('.php')).sort();
const requestMethods = new Map();
for (const file of apiFiles) {
  const path = join(apiDirectory, file);
  let source = await readFile(path, 'utf8');
  const methods = [...source.matchAll(/public function ([A-Za-z_][A-Za-z0-9_]*Request)\s*\(/g)].reverse();

  for (const methodMatch of methods) {
    const methodStart = methodMatch.index;
    const methodText = methodMatch[0];
    const { bodyEnd } = methodBody(source, methodStart, methodText);
    const body = source.slice(methodStart, bodyEnd + 1);
    const resourcePath = body.match(/\$resourcePath\s*=\s*'([^']+)'/)?.[1];
    const method = body.match(/return new Request\(\s*'([A-Z]+)'/)?.[1];
    if (!resourcePath || !method) {
      continue;
    }

    const operation = `${method} ${resourcePath}`;
    const schemaPointer = manifest.operations[operation];
    if (!schemaPointer) {
      continue;
    }

    const jsonArgument = body.match(/json_encode\(ObjectSerializer::sanitizeForSerialization\(\$(\w+)\)/)?.[1];
    let guardArgument = jsonArgument ? `$${jsonArgument}` : null;
    const preparedFormData = body.match(/\$formData\s*=\s*\$formDataProcessor->prepare\(\s*\[[\s\S]*?\]\s*\);/)?.[0];

    if (!guardArgument && preparedFormData) {
      guardArgument = '$formData';
      const prepareEnd = source.indexOf(preparedFormData, methodStart) + preparedFormData.length;
      source = `${source.slice(0, prepareEnd)}\n        \\Plainrouter\\ClosedObjectGuard::assertRequestBody('${operation}', $formData);${source.slice(prepareEnd)}`;
    } else if (!guardArgument && body.match(/json_encode\(\$formParams,/)) {
      guardArgument = '$formParams';
      const encodeAt = source.indexOf('json_encode($formParams,', methodStart);
      const lineStart = source.lastIndexOf('\n', encodeAt) + 1;
      const indentation = source.slice(lineStart, encodeAt);
      source = `${source.slice(0, lineStart)}${indentation}\\Plainrouter\\ClosedObjectGuard::assertRequestBody('${operation}', $formParams);\n${source.slice(lineStart)}`;
    } else if (guardArgument) {
      if (source.slice(methodStart, bodyEnd + 1).includes(`ClosedObjectGuard::assertRequestBody('${operation}'`)) {
        continue;
      }
      source = insertAfterOpeningBrace(
        source,
        methodStart,
        methodText,
        `\\Plainrouter\\ClosedObjectGuard::assertRequestBody('${operation}', ${guardArgument});`,
      );
    }

    if (!guardArgument) {
      throw new Error(`Could not locate PHP request-body input for ${operation} (${file}::${methodMatch[1]})`);
    }

    requestMethods.set(operation, `${file}::${methodMatch[1]}`);
  }

  await writeFile(path, source);
}

for (const operation of Object.keys(manifest.operations)) {
  if (!requestMethods.has(operation)) {
    throw new Error(`Could not locate generated PHP request method for ${operation}`);
  }
}

function resolveSchema(pointer, schemas) {
  const seen = new Set();
  let schema = schemas[pointer];
  while (schema?.$ref) {
    if (seen.has(pointer)) {
      throw new Error(`Recursive schema reference at ${pointer}`);
    }
    seen.add(pointer);
    pointer = schema.$ref;
    schema = schemas[pointer];
  }
  if (!schema) {
    throw new Error(`Missing schema node ${pointer}`);
  }
  return schema;
}
