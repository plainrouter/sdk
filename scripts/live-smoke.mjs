import {
  configurePlainrouter,
  getSandbox,
  listEvents,
  validateSandboxEvent,
  validateSandboxEventWithKey,
  zGetSandboxResponse,
  zListEventsResponse,
  zValidateSandboxEventResponse,
  zValidateSandboxEventWithKeyResponse,
} from '@plainrouter/sdk';

const baseUrl = process.env.PLAINROUTER_BASE_URL;
const requestOptions = {
  throwOnError: true,
  ...(baseUrl ? { baseUrl } : {}),
};

const assertDiscarded = (result, description) => {
  if (
    result.sandbox !== true ||
    result.accepted !== true ||
    result.persisted !== false ||
    result.provider_delivery !== false
  ) {
    throw new Error(`${description} was not validated and discarded: ${JSON.stringify(result)}`);
  }
};

const sandbox = zGetSandboxResponse.parse((await getSandbox(requestOptions)).data);

if (sandbox.persists_data !== false || sandbox.provider_delivery !== false) {
  throw new Error('The live sandbox no longer declares itself isolated.');
}

const body = sandbox.try.body;

assertDiscarded(
  zValidateSandboxEventResponse.parse(
    (await validateSandboxEvent({ ...requestOptions, body })).data,
  ),
  'Zero-auth synthetic event',
);
assertDiscarded(
  zValidateSandboxEventWithKeyResponse.parse(
    (
      await validateSandboxEventWithKey({
        ...requestOptions,
        auth: sandbox.self_serve_key.issued_key.api_key,
        body,
      })
    ).data,
  ),
  'Keyed synthetic event',
);

console.log('TypeScript SDK live sandbox smoke passed.');

const signalTrackerSecret = process.env.PLAINROUTER_SMOKE_SECRET;

if (signalTrackerSecret) {
  configurePlainrouter({ signalTrackerSecret, ...(baseUrl ? { baseUrl } : {}) });
  zListEventsResponse.parse((await listEvents({ throwOnError: true, query: { per_page: 5 } })).data);
  console.log('TypeScript SDK live authenticated read smoke passed.');
} else {
  console.log(
    '::notice title=Authenticated live smoke skipped::PLAINROUTER_SMOKE_SECRET is not set; only the zero-auth sandbox was exercised.',
  );
}
