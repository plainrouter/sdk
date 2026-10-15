import { integerFields } from './generated/integer-fields.gen.js';

type IntegerSelectors = {
  operationId: string;
  body: readonly (readonly string[])[];
  path: readonly string[];
  query: readonly string[];
};

const operationName = (operationId: string): string => operationId
  .split(/[._-]+/)
  .filter(Boolean)
  .map((part, index) => index === 0
    ? `${part[0]?.toLowerCase() ?? ''}${part.slice(1)}`
    : `${part[0]?.toUpperCase() ?? ''}${part.slice(1)}`)
  .join('');

const fieldsByOperation = new Map<string, IntegerSelectors>();
for (const fields of Object.values(integerFields)) {
  fieldsByOperation.set(operationName(fields.operationId), fields);
}

const fieldName = (location: string, selector: readonly string[]): string =>
  [location, ...selector].map((segment) => segment === '*' ? '[]' : segment).join('.').replaceAll('.[]', '[]');

const rejectBoolean = (field: string, value: unknown): void => {
  if (Array.isArray(value)) {
    value.forEach((entry, index) => rejectBoolean(`${field}[${index}]`, entry));
    return;
  }
  if (typeof value === 'boolean' || Object.prototype.toString.call(value) === '[object Boolean]') {
    const error = new TypeError(`Integer field "${field}" cannot be a boolean.`);
    error.name = 'IntegerFieldBooleanError';
    throw error;
  }
};

const inspectSelector = (
  value: unknown,
  selector: readonly string[],
  location: string,
  fullSelector: readonly string[] = selector,
): void => {
  if (selector.length === 0) {
    rejectBoolean(fieldName(location, fullSelector), value);
    return;
  }

  const [segment, ...rest] = selector;
  if (segment === undefined) return;
  if (segment === '*') {
    if (Array.isArray(value)) {
      value.forEach((entry) => inspectSelector(entry, rest, location, fullSelector));
      return;
    }
    if (value && typeof value === 'object') {
      for (const entry of Object.values(value)) {
        inspectSelector(entry, rest, location, fullSelector);
      }
    }
    return;
  }

  if (value && typeof value === 'object' && segment in value) {
    inspectSelector((value as Record<string, unknown>)[segment], rest, location, fullSelector);
  }
};

/** Refuse booleans at OpenAPI integer request fields before an operation reaches fetch. */
export const assertNoBooleanIntegerFields = (operation: string, options: unknown): void => {
  const fields = fieldsByOperation.get(operation);
  if (!fields || !options || typeof options !== 'object') return;

  const request = options as Record<string, unknown>;
  for (const location of ['path', 'query'] as const) {
    const values = request[location];
    for (const name of fields[location]) {
      if (values && typeof values === 'object' && name in values) {
        rejectBoolean(`${location}.${name}`, (values as Record<string, unknown>)[name]);
      }
    }
  }

  for (const selector of fields.body) {
    inspectSelector(request.body, selector, 'body');
  }
};
