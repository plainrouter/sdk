import { readFile, writeFile } from 'node:fs/promises';

const [input, output, mode] = process.argv.slice(2);
if (!input || !output) {
  throw new Error('usage: prepare-generator-input.mjs INPUT OUTPUT [--omit-page-defaults|--page-defaults-only]');
}

if (mode && !['--omit-page-defaults', '--page-defaults-only'].includes(mode)) {
  throw new Error(`Unknown generator input mode: ${mode}`);
}

const contract = JSON.parse(await readFile(input, 'utf8'));
// Keep published PHP positional arguments stable when the contract reorders queries.
const phpQueryParameterOrder = {
  'actions.api.index': ['status', 'page', 'account_id', 'cursor', 'limit'],
  'actions.rules.index': ['page', 'account_id', 'platform_ad_account_id', 'cursor', 'per_page'],
  'actions.tests.api.index': ['page', 'per_page'],
  'launch.creatives.index': ['page', 'cursor', 'per_page'],
  'launch.plans.index': ['page', 'cursor', 'per_page'],
  'launch.policies.index': ['page', 'per_page'],
};

const normalize = (value) => {
  if (!value || typeof value !== 'object') return;

  // Generator 7.25.0 treats bare null as a non-nullable fictional Null model.
  // This equivalent schema still permits only null and preserves required keys.
  if (value.type === 'null') {
    value.type = ['object', 'null'];
    value.enum ??= [null];
  }

  // New list responses reuse the pagination-link model. Keep its existing
  // property order when the generator deduplicates those equivalent schemas.
  const paginationFields = ['url', 'label', 'active'];
  if (
    value.type === 'object'
    && value.properties
    && Object.keys(value.properties).length === paginationFields.length
    && paginationFields.every((field) => Object.hasOwn(value.properties, field))
  ) {
    value.properties = Object.fromEntries(
      paginationFields.map((field) => [field, value.properties[field]]),
    );
    if (Array.isArray(value.required)) {
      value.required = paginationFields.filter((field) => value.required.includes(field));
    }
  }

  for (const child of Object.values(value)) normalize(child);
};

if (mode) {
  for (const path of Object.values(contract.paths ?? {})) {
    for (const operation of Object.values(path)) {
      if (mode === '--omit-page-defaults') {
        const existingOrder = phpQueryParameterOrder[operation?.operationId];
        if (existingOrder && Array.isArray(operation.parameters)) {
          const queryParameters = operation.parameters.filter((parameter) => parameter.in === 'query');
          const orderedNames = new Set(existingOrder);
          const byName = new Map(queryParameters.map((parameter) => [parameter.name, parameter]));
          const orderedQueryParameters = [
            ...existingOrder.flatMap((name) => byName.has(name) ? [byName.get(name)] : []),
            ...queryParameters.filter((parameter) => !orderedNames.has(parameter.name)),
          ];
          let queryIndex = 0;
          operation.parameters = operation.parameters.map((parameter) =>
            parameter.in === 'query' ? orderedQueryParameters[queryIndex++] : parameter,
          );
        }
      }

      for (const parameter of operation?.parameters ?? []) {
        // Let the server apply its page default when the caller leaves it unset.
        if (parameter.in === 'query' && parameter.name === 'page' && !parameter.required) {
          delete parameter.schema?.default;
        }
      }
    }
  }
}

if (mode !== '--page-defaults-only') {
  normalize(contract);
}
await writeFile(output, `${JSON.stringify(contract)}\n`);
