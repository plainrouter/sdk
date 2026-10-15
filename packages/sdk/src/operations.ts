import * as generated from './generated/sdk.gen.js';
import type { Config } from './generated/client/types.gen.js';
import { normalizeHeaders } from './headers.js';
import { assertNoBooleanIntegerFields } from './integer-fields.js';

type Operation = (options: never) => unknown;

// Preserve each generated signature, including its generics and optional options.
const normalizeOperation = <T extends Operation>(name: string, operation: T): T => (
  (options: { headers?: Config['headers'] } | undefined) => {
    try {
      assertNoBooleanIntegerFields(name, options);
    } catch (error) {
      return Promise.reject(error);
    }
    if (options === undefined) return operation(options as never);
    const headers = normalizeHeaders(options.headers);
    return operation({
      ...options,
      headers,
    } as never);
  }
) as unknown as T;

// Normalize before generated body operations spread headers into Content-Type defaults.
export const operations = Object.fromEntries(
  Object.entries(generated).map(([name, operation]) => [name, normalizeOperation(name, operation)]),
) as typeof generated;

// The curated event-validation facade uses this operation internally.
export const createEvent = operations.createEvent;
