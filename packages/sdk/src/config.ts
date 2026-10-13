import { client } from './generated/client.gen.js';

/** An API redirect is an error, even when its destination is a successful HTML page. */
export class ApiRedirectError extends Error {
  readonly status: number;
  readonly headers: Headers;

  constructor(readonly response: Response) {
    super(`API request returned HTTP ${response.status}`);
    this.name = 'ApiRedirectError';
    this.status = response.status;
    this.headers = response.headers;
  }
}

client.setConfig({ headers: { Accept: 'application/json' } });
client.interceptors.request.use((request) => new Request(request, { redirect: 'manual' }));
client.interceptors.response.use((response) => {
  if (response.status >= 300 && response.status < 400) {
    throw new ApiRedirectError(response);
  }
  // Browsers hide cross-origin manual redirects, including their status and headers.
  if (response.type === 'opaqueredirect') {
    throw new ApiRedirectError(response);
  }
  return response;
});
client.interceptors.error.use((error) => {
  if (error instanceof ApiRedirectError) throw error;
  return error;
});

export type PlainrouterConfig = {
  signalTrackerSecret: string;
  baseUrl?: string;
  fetch?: typeof globalThis.fetch;
  headers?: HeadersInit;
};

export const configurePlainrouter = ({
  signalTrackerSecret,
  baseUrl,
  fetch,
  headers,
}: PlainrouterConfig) => {
  const requestHeaders = new Headers({ Accept: 'application/json' });
  new Headers(headers).forEach((value, key) => requestHeaders.set(key, value));
  client.setConfig({
    auth: signalTrackerSecret,
    headers: requestHeaders,
    ...(baseUrl === undefined ? {} : { baseUrl }),
    ...(fetch === undefined ? {} : { fetch }),
  });

  return client;
};
