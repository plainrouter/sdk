import { mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import { basename, join } from 'node:path';

const [apiDirectory, outputDirectory, manifestPath] = process.argv.slice(2);
if (!apiDirectory || !outputDirectory || !manifestPath) {
  throw new Error('usage: generate-php-integer-apis.mjs API_DIRECTORY OUTPUT_DIRECTORY MANIFEST');
}

const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
const apiFiles = (await readdir(apiDirectory)).filter((file) => file.endsWith('.php')).sort();
const requestMethods = new Map();

for (const file of apiFiles) {
  const source = await readFile(join(apiDirectory, file), 'utf8');
  const methods = [...source.matchAll(/public function ([A-Za-z_][A-Za-z0-9_]*Request)\s*\(/g)];

  for (let index = 0; index < methods.length; index += 1) {
    const start = methods[index].index;
    const end = methods[index + 1]?.index ?? source.length;
    const body = source.slice(start, end);
    const methodSignature = signature(source, start, methods[index][0]);
    const path = body.match(/\$resourcePath\s*=\s*'([^']+)'/)?.[1];
    const method = body.match(/return new Request\(\s*'([A-Z]+)'/)?.[1];
    if (path && method) {
      requestMethods.set(`${method} ${path}`, {
        apiClass: basename(file, '.php'),
        methodName: methods[index][1],
        methodSignature,
        hostSettingsMethod: body.match(/\$this->(getHostSettingsFor[A-Za-z_][A-Za-z0-9_]*)\(\)/)?.[1] ?? null,
        source: body,
      });
    }
  }
}

const guardedByApi = new Map(apiFiles.map((file) => [basename(file, '.php'), []]));
for (const [operation, fields] of Object.entries(manifest)) {
  const generated = requestMethods.get(operation);
  if (!generated) {
    if (fields.query.length || fields.path.length || fields.body.length) {
      throw new Error(`Could not match PHP generated request method for ${operation}`);
    }
    continue;
  }

  const bodyArgument = generated.source.match(/json_encode\(ObjectSerializer::sanitizeForSerialization\(\$(\w+)\)/)?.[1] ?? null;
  const formData = generated.source.match(/\$formData\s*=\s*\$formDataProcessor->prepare\(\[([\s\S]*?)\]\)/)?.[1] ?? '';
  const formArguments = new Map([...formData.matchAll(/'([^']+)'\s*=>\s*\$(\w+)/g)].map((match) => [match[1], match[2]]));
  const bodyFieldArguments = fields.body
    .filter((path) => path.length === 1 && formArguments.has(path[0]))
    .map((path) => [path[0], formArguments.get(path[0])]);

  if (fields.body.length && bodyArgument === null && bodyFieldArguments.length !== fields.body.length) {
    const unmapped = fields.body.filter((path) => !(path.length === 1 && formArguments.has(path[0])));
    throw new Error(`Could not map PHP request-body integer fields for ${operation}: ${JSON.stringify(unmapped)}`);
  }
  if (!fields.query.length && !fields.path.length && !bodyArgument && !bodyFieldArguments.length) continue;

  const guarded = guardedByApi.get(generated.apiClass) ?? [];
  guarded.push({
    operation,
    methodName: generated.methodName,
    methodSignature: generated.methodSignature,
    bodyArgument,
    bodyFieldArguments,
    hostSettingsMethod: generated.hostSettingsMethod,
  });
  guardedByApi.set(generated.apiClass, guarded);
}

await rm(outputDirectory, { recursive: true, force: true });
await mkdir(outputDirectory, { recursive: true });

for (const [apiClass, methods] of guardedByApi) {
  const declarations = methods.map(({ operation, methodName, methodSignature, bodyArgument, bodyFieldArguments }) => `    ${methodSignature}
    {
        IntegerInputGuard::assertArguments('${operation}', self::class, __FUNCTION__, func_get_args(), ${bodyArgument === null ? 'null' : `'${bodyArgument}'`}, ${phpPairs(bodyFieldArguments)});
        return parent::${methodName}(...func_get_args());
    }`).join('\n\n');
  const hostOverrides = [...new Set(methods.map(({ hostSettingsMethod }) => hostSettingsMethod).filter(Boolean))]
    .map((method) => method === 'getHostSettingsForlauncherFileImport' ? `    protected function ${method}(): array
    {
        $base = rtrim($this->config->getHost(), '/');
        $base = preg_replace('~/api/v1$~', '', $base);
        return [['url' => $base, 'description' => 'Configured launcher base URL']];
    }` : `    protected function ${method}(): array
    {
        if ($this->config->getHost() !== \\Plainrouter\\Client::DEFAULT_BASE_URL) {
            return [['url' => $this->config->getHost(), 'description' => 'Configured base URL']];
        }
        return parent::${method}();
    }`).join('\n\n');
  const className = `Guarded${apiClass}`;
  const source = `<?php

declare(strict_types=1);

namespace Plainrouter\\IntegerInputApis;

use Plainrouter\\IntegerInputGuard;

/** Generated from spec/openapi.json by scripts/generate-php-integer-apis.mjs. */
class ${className} extends \\Plainrouter\\OpenAPI\\Api\\${apiClass}
{
${[declarations, hostOverrides].filter(Boolean).join('\n\n')}
}
`;
  await writeFile(join(outputDirectory, `${className}.php`), source);
}

function signature(source, start, matchedText) {
  const openingParen = start + matchedText.length - 1;
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
  if (closingParen === -1) throw new Error(`Could not close generated request signature at offset ${start}`);
  const bodyStart = source.indexOf('{', closingParen);
  if (bodyStart === -1) throw new Error(`Could not find generated request body at offset ${start}`);
  return source.slice(start, bodyStart).trim();
}

function phpPairs(pairs) {
  if (pairs.length === 0) return '[]';
  return `[${pairs.map(([field, argument]) => `['${field}', '${argument}']`).join(', ')}]`;
}
