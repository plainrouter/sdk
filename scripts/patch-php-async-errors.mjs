import fs from 'node:fs';
import path from 'node:path';

const apiDirectory = process.argv[2];
if (!apiDirectory || !fs.statSync(apiDirectory).isDirectory()) {
  throw new Error('usage: node scripts/patch-php-async-errors.mjs API_DIRECTORY');
}

const methodPattern = /^[ \t]*public function ([A-Za-z_][A-Za-z0-9_]*)\s*\(/gm;
const responsePattern = /case\s+(\d+):\s*\$data\s*=\s*ObjectSerializer::deserialize\(\s*\$e->getResponseBody\(\),\s*'([^']+)'\s*,\s*\$e->getResponseHeaders\(\)\s*\);\s*\$e->setResponseObject\(\$data\);\s*throw \$e;/g;
const asyncHandlerPattern = /function \(\$exception\) \{\n([\s\S]*?)\n([ \t]*)\}/;

function methodsIn(source) {
  const matches = [...source.matchAll(methodPattern)];
  return matches.map((match, index) => ({
    name: match[1],
    start: match.index,
    end: matches[index + 1]?.index ?? source.length,
    source: source.slice(match.index, matches[index + 1]?.index ?? source.length),
  }));
}

function responseModels(syncMethod, file, name) {
  const catchStart = syncMethod.source.indexOf('catch (ApiException $e) {');
  if (catchStart < 0) {
    throw new Error(`${file}:${name}: missing generated sync ApiException mapping`);
  }

  const models = new Map();
  for (const match of syncMethod.source.slice(catchStart).matchAll(responsePattern)) {
    const status = Number(match[1]);
    if (status < 400) continue;
    const previous = models.get(status);
    if (previous && previous !== match[2]) {
      throw new Error(`${file}:${name}: conflicting model mappings for ${status}`);
    }
    models.set(status, match[2]);
  }
  return models;
}

function errorModelBlock(models, bodyIndent) {
  const innerIndent = `${bodyIndent}    `;
  const entries = [...models]
    .sort(([left], [right]) => left - right)
    .map(([status, model]) => `${innerIndent}${status} => '${model}',`)
    .join('\n');

  return [
    `${bodyIndent}\\Plainrouter\\GeneratedErrorResponses::apply($apiException, $this->client, [`,
    entries,
    `${bodyIndent}]);`,
    `${bodyIndent}throw $apiException;`,
  ].join('\n');
}

let patchedMethods = 0;
let expectedMethods = 0;
for (const filename of fs.readdirSync(apiDirectory).filter((name) => name.endsWith('.php'))) {
  const filePath = path.join(apiDirectory, filename);
  let source = fs.readFileSync(filePath, 'utf8');
  const methods = methodsIn(source);
  const methodsByName = new Map(methods.map((method) => [method.name, method]));
  const expectedAsyncNames = new Set();

  for (const method of methods.filter(({ name }) => name.endsWith('WithHttpInfo') && !name.includes('Async'))) {
    const models = responseModels(method, filename, method.name);
    if (models.size === 0) continue;
    const asyncName = method.name.replace(/WithHttpInfo$/, 'AsyncWithHttpInfo');
    if (!methodsByName.has(asyncName)) {
      throw new Error(`${filename}:${method.name}: paired generated async method not found`);
    }
    expectedAsyncNames.add(asyncName);
  }
  expectedMethods += expectedAsyncNames.size;
  const patchedAsyncNames = new Set();

  for (const method of methods
    .filter(({ name }) => name.endsWith('AsyncWithHttpInfo'))
    .sort((left, right) => right.start - left.start)) {
    const syncName = method.name.replace(/AsyncWithHttpInfo$/, 'WithHttpInfo');
    const syncMethod = methodsByName.get(syncName);
    if (!syncMethod) throw new Error(`${filename}:${method.name}: paired sync method not found`);

    const models = responseModels(syncMethod, filename, syncName);
    if (models.size === 0) continue;

    const handlerMatch = method.source.match(asyncHandlerPattern);
    if (!handlerMatch) throw new Error(`${filename}:${method.name}: generated async error handler not found`);

    const body = handlerMatch[1];
    const responseLine = body.match(/^([ \t]*)\$response = \$exception->getResponse\(\);$/m);
    if (!responseLine) throw new Error(`${filename}:${method.name}: generated response line not found`);
    const bodyIndent = responseLine[1];

    let patchedBody = body.replace(
      /^([ \t]*)throw new ApiException\(/m,
      '$1$apiException = new ApiException(',
    );
    if (patchedBody === body) throw new Error(`${filename}:${method.name}: ApiException construction not found`);
    patchedBody = patchedBody.replace('(string) $response->getBody()', '$responseBody');
    patchedBody = patchedBody.replace(
      /^([ \t]*)\$statusCode = \$response->getStatusCode\(\);$/m,
      `$1$statusCode = $response->getStatusCode();\n${bodyIndent}$responseBody = (string) $response->getBody();`,
    );
    if (patchedBody === body) throw new Error(`${filename}:${method.name}: response body extraction not found`);

    const closing = patchedBody.match(/\n([ \t]*)\);\s*$/);
    if (!closing) throw new Error(`${filename}:${method.name}: ApiException construction close not found`);
    const closeStart = closing.index;
    const closeEnd = closeStart + closing[0].length;
    const beforeClose = patchedBody.slice(0, closeStart + 1);
    const closeIndent = closing[1];
    const afterClose = patchedBody.slice(closeEnd);
    patchedBody = `${beforeClose}${closeIndent});\n${errorModelBlock(models, bodyIndent)}${afterClose}`;

    const patchedHandler = handlerMatch[0].replace(body, patchedBody);
    const methodStart = method.start;
    const handlerOffset = method.source.indexOf(handlerMatch[0]);
    const absoluteStart = methodStart + handlerOffset;
    source = `${source.slice(0, absoluteStart)}${patchedHandler}${source.slice(absoluteStart + handlerMatch[0].length)}`;
    patchedMethods += 1;
    patchedAsyncNames.add(method.name);
  }

  if (expectedAsyncNames.size !== patchedAsyncNames.size
    || [...expectedAsyncNames].some((name) => !patchedAsyncNames.has(name))) {
    throw new Error(`${filename}: expected ${expectedAsyncNames.size} async model mappings, patched ${patchedAsyncNames.size}`);
  }

  fs.writeFileSync(filePath, source);
}

if (patchedMethods !== expectedMethods) {
  throw new Error(`expected to patch ${expectedMethods} generated async operations, patched ${patchedMethods}`);
}
