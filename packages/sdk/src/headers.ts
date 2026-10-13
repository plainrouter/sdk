import type { Config } from './generated/client/types.gen.js';

export const normalizeHeaders = (headers: Config['headers']): Record<string, string | null | undefined> => {
  const result: Record<string, string | null | undefined> = Object.create(null);
  const entries = headers instanceof Headers
    ? Array.from(headers.entries())
    : Array.isArray(headers) ? headers : Object.entries(headers ?? {});
  for (const [name, value] of entries) {
    result[name.toLowerCase()] = value === null || value === undefined ? value
      : Array.isArray(value) ? value.map(String).join(', ')
      : typeof value === 'object' ? JSON.stringify(value) : String(value);
  }
  return result;
};

