import { describe, expect, it } from 'vitest';

import {
  zCreateEventResponse,
  zGetEmqReportResponse,
} from '../src/index.js';

describe('generated response schemas', () => {
  it('round-trips a valid POST /events response and rejects a broken response', () => {
    const response = {
      event_id: '01JTESTEVENT00000000000000',
      duplicate: false,
    };

    expect(
      zCreateEventResponse.parse(JSON.parse(JSON.stringify(response))),
    ).toEqual(response);
    expect(() =>
      zCreateEventResponse.parse({ event_id: 123, duplicate: false }),
    ).toThrow();
  });

  it('round-trips a valid GET /reports/emq response and rejects a broken response', () => {
    const response = { snapshots: [] };

    expect(
      zGetEmqReportResponse.parse(JSON.parse(JSON.stringify(response))),
    ).toEqual(response);
    expect(() =>
      zGetEmqReportResponse.parse({ snapshots: 'not-an-array' }),
    ).toThrow();
  });
});
