import { listEvents, zErrorMessage } from '@plainrouter/sdk';

const baseUrl = process.env.PLAINROUTER_BASE_URL;
const result = await listEvents({
  throwOnError: false,
  query: { per_page: 1 },
  ...(baseUrl ? { baseUrl } : {}),
});

if (result.response.status !== 401) {
  throw new Error(`Anonymous event listing must return HTTP 401, received ${result.response.status}.`);
}

const error = zErrorMessage.parse(result.error);
if (!error.message.trim()) {
  throw new Error('Anonymous event listing returned an empty authentication error.');
}

console.log('TypeScript SDK anonymous authorization smoke passed (401). No authenticated operations exercised.');
