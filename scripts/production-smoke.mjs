import {
  configurePlainrouter,
  getEmqReport,
  zGetEmqReportResponse,
} from '@plainrouter/sdk';

let capturedRequest;
const fetch = async (input, init) => {
  capturedRequest = input instanceof Request ? input : new Request(input, init);

  return new Response(JSON.stringify({ snapshots: [] }), {
    headers: { 'Content-Type': 'application/json' },
    status: 200,
  });
};

configurePlainrouter({
  baseUrl: 'https://example.test/api/v1',
  fetch,
  signalTrackerSecret: 'production-smoke-secret',
});

const result = await getEmqReport();

zGetEmqReportResponse.parse(result.data);

if (capturedRequest?.headers.get('Authorization') !== 'Bearer production-smoke-secret') {
  throw new Error('Production SDK did not apply bearer authentication.');
}

console.log('Production SDK runtime smoke test passed.');
