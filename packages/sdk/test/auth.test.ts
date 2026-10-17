import { createServer } from 'node:http';
import { once } from 'node:events';
import { createClient } from '../src/generated/client/index.js';
import { client as generatedClient } from '../src/generated/client.gen.js';

import { describe, expect, it, vi } from 'vitest';
import * as generatedOperations from '../src/generated/sdk.gen.js';
import * as exportedOperations from '../src/operation-exports.js';
import { integerFields } from '../src/generated/integer-fields.gen.js';

import {
  ApiRedirectError,
  actionsRulesIndex,
  actionsRulesShow,
  actionsRulesStore,
  actionsRulesUpdate,
  agentContext,
  configurePlainrouter,
  createEvent,
  getEmqReport,
  launcherFileImport,
  launchPlansCopy,
  zLaunchPlansCopyResponse,
  verifySignalIngestion,
} from '../src/index.js';

const operationName = (operationId: string): string => operationId
  .split(/[._-]+/)
  .filter(Boolean)
  .map((part, index) => index === 0
    ? `${part[0]?.toLowerCase() ?? ''}${part.slice(1)}`
    : `${part[0]?.toUpperCase() ?? ''}${part.slice(1)}`)
  .join('');

const valueAtIntegerPath = (path: readonly string[], leaf: unknown = true): unknown => {
  const [segment, ...rest] = path;
  if (segment === undefined) return leaf;
  const value = valueAtIntegerPath(rest, leaf);
  return segment === '*' ? [value] : { [segment]: value };
};

describe('signalTrackerSecret authentication', () => {
  it('sets the bearer header from injected configuration without a network call', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(JSON.stringify({ snapshots: [] }), {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      });
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    const result = await getEmqReport();

    expect(result.data).toEqual({ snapshots: [] });
    expect(fetchMock).toHaveBeenCalledOnce();

    expect(requests).toHaveLength(1);
    expect(requests[0]?.headers.get('Authorization')).toBe(
      'Bearer tracker-test-secret',
    );
  });

  it('calls verification ingestion with bearer authentication', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(
        JSON.stringify({ event_id: 'signal-verification', duplicate: false }),
        {
          headers: { 'Content-Type': 'application/json' },
          status: 202,
        },
      );
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    const result = await verifySignalIngestion();

    expect(result.data).toEqual({
      event_id: 'signal-verification',
      duplicate: false,
    });
    expect(requests[0]?.method).toBe('POST');
    expect(requests[0]?.url).toBe(
      'https://example.test/api/v1/verification-events',
    );
    expect(requests[0]?.headers.get('Authorization')).toBe(
      'Bearer tracker-test-secret',
    );
  });

  it('serializes consent fields on event requests', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(
        JSON.stringify({ event_id: 'event-123', duplicate: false }),
        {
          headers: { 'Content-Type': 'application/json' },
          status: 202,
        },
      );
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    await createEvent({
      body: {
        consent: { analytics_storage: 'granted' },
        consent_basis: 'consent',
        consent_mode: { ad_user_data: 'granted' },
        event_name: 'Purchase',
        tcf: { string: 'test-tcf-string' },
      },
    });

    await expect(requests[0]?.json()).resolves.toEqual({
      consent: { analytics_storage: 'granted' },
      consent_basis: 'consent',
      consent_mode: { ad_user_data: 'granted' },
      event_name: 'Purchase',
      tcf: { string: 'test-tcf-string' },
    });
  });
});

describe('plan copy', () => {
  it('copies a failed plan with bearer auth and parses the fresh draft', async () => {
    const requests: Request[] = [];
    const draft = {
      plan: {
        id: 'draft-copy',
        platform_ad_account_id: 7,
        status: 'draft',
        budget_amount_minor: 12345,
        validation_result: null,
        validated_at: null,
        approval_id: null,
      },
    };
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(input instanceof Request ? input : new Request(input, init));
      return new Response(JSON.stringify(draft), {
        headers: { 'Content-Type': 'application/json' },
        status: 201,
      });
    });
    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'plan-writer-test-token',
    });

    const result = await launchPlansCopy({
      path: { workspace: 1, deployment_plan: 'failed-plan' },
    });

    expect(result.response?.status).toBe(201);
    expect(zLaunchPlansCopyResponse.parse(result.data)).toEqual(draft);
    expect(fetchMock).toHaveBeenCalledOnce();
    expect(requests[0]?.method).toBe('POST');
    expect(requests[0]?.url).toBe(
      'https://example.test/api/v1/workspaces/1/admin/plans/failed-plan/copy',
    );
    expect(requests[0]?.headers.get('Authorization')).toBe('Bearer plan-writer-test-token');
    expect(await requests[0]?.text()).toBe('');
  });
});


describe('JSON API transport', () => {
  it('defaults Accept to JSON and preserves case-insensitive caller overrides', async () => {
    expect(Object.keys(exportedOperations).sort()).toEqual(Object.keys(generatedOperations).sort());
    const requests: Request[] = [];
    const fetchMock: typeof globalThis.fetch = async (input, init) => {
      requests.push(new Request(input, init));
      return new Response('{"snapshots":[]}', { headers: { 'Content-Type': 'application/json' } });
    };
    configurePlainrouter({ signalTrackerSecret: 'test', fetch: fetchMock });
    await getEmqReport();
    await getEmqReport({ headers: { accept: 'text/html' } });
    await getEmqReport({ headers: { ACCEPT: ['text/csv'] } });
    await getEmqReport({ headers: [['AcCePt', 'text/xml']] });
    configurePlainrouter({ signalTrackerSecret: 'test', fetch: fetchMock, headers: { accept: '*/*' } });
    await getEmqReport();
    expect(requests.map((request) => request.headers.get('Accept'))).toEqual(['application/json', 'text/html', 'text/csv', 'text/xml', '*/*']);
    for (const [shape, headers, accept] of [
      ['Headers', new Headers({ AcCePt: 'text/html', AuThOrIzAtIoN: 'Bearer caller-token' }), 'text/html'],
      ['tuples', [['ACCEPT', 'text/xml'], ['Authorization', 'Bearer old-token'], ['authorization', 'Bearer caller-token']], 'text/xml'],
    ] as const) {
      await createEvent({
        body: { event_name: 'Purchase', consent_basis: 'consent' },
        headers: headers instanceof Headers ? headers : headers.map(([name, value]): [string, string] => [name, value]),
      });
      const request = requests.at(-1)!;
      expect.soft(request.headers.get('Accept'), `body operation with ${shape}`).toBe(accept);
      expect.soft(request.headers.get('Authorization'), `body operation with ${shape}`).toBe('Bearer test');
      expect.soft(Array.from(request.headers.keys()).filter((name) => /^\d+$/.test(name)), `body operation with ${shape}`).toEqual([]);
      expect(request.headers.get('Content-Type')).toBe('application/json');
      expect(await request.json()).toEqual({ event_name: 'Purchase', consent_basis: 'consent' });
    }

    configurePlainrouter({ signalTrackerSecret: 'test', fetch: fetchMock });
    await agentContext({ query: { workspace_id: 7 } });
    await actionsRulesIndex({ path: { workspace: 7 } });
    await actionsRulesStore({
      path: { workspace: 7 },
      body: {
        name: 'Test rule',
        platform_ad_account_id: 123,
        definition: {
          target_level: 'ad_set',
          action: 'pause',
          minimum_counted_arrivals: 50,
          cost_comparison: 'at_least',
          cost_ratio: '1',
        },
      },
    });
    await actionsRulesShow({ path: { workspace: 7, action_rule: 'rule-1' } });
    await actionsRulesUpdate({
      path: { workspace: 7, action_rule: 'rule-1' },
      body: { name: 'Updated rule' },
    });

    expect(requests).toHaveLength(12);
    expect(requests.slice(7).map((request) => [request.method, new URL(request.url).pathname])).toEqual([
      ['GET', '/api/v1/agent/context'],
      ['GET', '/api/v1/agent/workspaces/7/action-rules'],
      ['POST', '/api/v1/agent/workspaces/7/action-rules'],
      ['GET', '/api/v1/agent/workspaces/7/action-rules/rule-1'],
      ['PATCH', '/api/v1/agent/workspaces/7/action-rules/rule-1'],
    ]);
    expect(requests.slice(7).map((request) => request.headers.get('Accept'))).toEqual([
      'application/json',
      'application/json',
      'application/json',
      'application/json',
      'application/json',
    ]);
    expect(requests.slice(7).map((request) => request.headers.get('Authorization'))).toEqual([
      'Bearer test',
      'Bearer test',
      'Bearer test',
      'Bearer test',
      'Bearer test',
    ]);
    expect(requests[9]?.headers.get('Content-Type')).toBe('application/json');
    expect(requests[11]?.headers.get('Content-Type')).toBe('application/json');
    await expect(requests[9]?.json()).resolves.toEqual({
      name: 'Test rule',
      platform_ad_account_id: 123,
      definition: {
        target_level: 'ad_set',
        action: 'pause',
        minimum_counted_arrivals: 50,
        cost_comparison: 'at_least',
        cost_ratio: '1',
      },
    });
    await expect(requests[11]?.json()).resolves.toEqual({ name: 'Updated rule' });

    const requestCountBeforeIntegerChecks = requests.length;
    const integerProbes: Array<{
      operation: (options: unknown) => Promise<unknown>;
      field: string;
      options: (value: boolean | number | string) => unknown;
    }> = [];
    for (const fields of Object.values(integerFields)) {
      const name = operationName(fields.operationId);
      const operation = (exportedOperations as unknown as Record<string, (options: unknown) => Promise<unknown>>)[name];
      if (!operation) throw new Error(`Missing generated operation ${name}`);

      for (const field of fields.path) {
        integerProbes.push({ operation, field, options: (value) => ({ path: { [field]: value } }) });
      }
      for (const field of fields.query) {
        integerProbes.push({ operation, field, options: (value) => ({ query: { [field]: value } }) });
      }
      for (const selector of fields.body) {
        const field = selector.filter((part) => part !== '*').at(-1) ?? 'body';
        integerProbes.push({ operation, field, options: (value) => ({ body: valueAtIntegerPath(selector, value) }) });
      }
    }
    for (const probe of integerProbes) {
      for (const value of [true, false]) {
        await expect(probe.operation(probe.options(value))).rejects.toThrow(probe.field);
      }
    }
    expect(requests).toHaveLength(requestCountBeforeIntegerChecks);
    for (const probe of integerProbes) {
      for (const value of [1, '1'] as const) {
        const before = requests.length;
        await probe.operation(probe.options(value));
        expect(requests).toHaveLength(before + 1);
      }
    }
    expect(requests).toHaveLength(requestCountBeforeIntegerChecks + integerProbes.length * 2);
  });

  it.each([300, 301, 302, 303, 304, 307, 308, 399])('rejects HTTP %i before parsing, for every result style', async (status) => {
    const fetchMock: typeof globalThis.fetch = async (input, init) => {
      expect(new Request(input, init).redirect).toBe('manual');
      return new Response(status === 304 ? null : '<html>Redirect</html>', { status, headers: { Location: '/html' } });
    };
    configurePlainrouter({ signalTrackerSecret: 'test', fetch: fetchMock });
    for (const responseStyle of ['fields', 'data'] as const) {
      for (const throwOnError of [false, true]) {
        try {
          await getEmqReport({ responseStyle, throwOnError, redirect: 'follow' });
          expect.unreachable('a redirect must never return data');
        } catch (error) {
          expect(error).toBeInstanceOf(ApiRedirectError);
          expect((error as ApiRedirectError).status).toBe(status);
          expect((error as ApiRedirectError).headers.get('Location')).toBe('/html');
        }
      }
    }
  });

  it('surfaces the documented workspace 404 body on both newly documented operations', async () => {
    const apiRouteNotFound = (method: string, path: string) => ({
      error: {
        code: 'api_route_not_found' as const,
        message: 'Workspace is nonexistent, inaccessible or noncanonical.',
        resolution: 'Check the workspace selector and retry.',
      },
      request: { method, path },
      resources: { documentation: 'https://plainrouter.com/docs', openapi: 'https://plainrouter.com/openapi.json' },
    });
    const requests: Request[] = [];
    const fetchMock: typeof globalThis.fetch = async (input, init) => {
      const request = input instanceof Request ? input : new Request(input, init);
      requests.push(request);
      expect(new URL(request.url).hostname).toBe('127.0.0.1');
      const url = new URL(request.url);
      return new Response(JSON.stringify(apiRouteNotFound(request.method, url.pathname.replace(/^\/api\/v1(?=\/)/, ''))), {
        status: 404,
        headers: { 'Content-Type': 'application/json' },
      });
    };
    configurePlainrouter({ baseUrl: 'http://127.0.0.1:4567/api/v1', fetch: fetchMock, signalTrackerSecret: 'workspace-404-test' });

    const contextError = apiRouteNotFound('GET', '/agent/context');
    const context = await agentContext();
    expect(context.error).toEqual(contextError);
    expect(context.response?.status).toBe(404);
    await expect(agentContext({ throwOnError: true })).rejects.toEqual(contextError);
    expect(await agentContext({ responseStyle: 'data' })).toBeUndefined();
    await expect(agentContext({ responseStyle: 'data', throwOnError: true })).rejects.toEqual(contextError);

    const importOptions = { body: { file: new Blob(['id']), source_adset_id: '123', source_ad_id: '456', mode: 'duplicate_adset' as const } };
    const fileImportError = apiRouteNotFound('POST', '/mcp/launcher/import');
    const fileImport = await launcherFileImport(importOptions);
    expect(fileImport.error).toEqual(fileImportError);
    expect(fileImport.response?.status).toBe(404);
    await expect(launcherFileImport({ ...importOptions, throwOnError: true })).rejects.toEqual(fileImportError);
    expect(await launcherFileImport({ ...importOptions, responseStyle: 'data' })).toBeUndefined();
    await expect(launcherFileImport({ ...importOptions, responseStyle: 'data', throwOnError: true })).rejects.toEqual(fileImportError);

    expect(requests).toHaveLength(8);
    expect(requests.map((request) => [request.method, new URL(request.url).pathname])).toEqual([
      ['GET', '/api/v1/agent/context'],
      ['GET', '/api/v1/agent/context'],
      ['GET', '/api/v1/agent/context'],
      ['GET', '/api/v1/agent/context'],
      ['POST', '/mcp/launcher/import'],
      ['POST', '/mcp/launcher/import'],
      ['POST', '/mcp/launcher/import'],
      ['POST', '/mcp/launcher/import'],
    ]);
  });
});

// All logical hosts are redirected before fetch; the capture server only binds loopback.
describe('launcher import route', () => {
  it.each([
    ['default', generatedClient.getConfig().baseUrl ?? '', '/mcp/launcher/import'],
    ['prefixed', 'https://proxy.example/api/v1', '/mcp/launcher/import'],
    ['slash', 'https://proxy.example/api/v1/', '/mcp/launcher/import'],
    ['nested', 'https://proxy.example/prefix/api/v1', '/prefix/mcp/launcher/import'],
    ['similar', 'https://proxy.example/api/v1beta', '/api/v1beta/mcp/launcher/import'],
    ['inner', 'https://proxy.example/api/v1/inner', '/api/v1/inner/mcp/launcher/import'],
    ['bare', 'http://127.0.0.1:8080', '/mcp/launcher/import'],
  ])('%s base reaches core in every call mode', async (_label, baseUrl, expected) => {
    if (_label === 'default') expect(baseUrl).toBe('https://plainrouter.com/api/v1');
    const paths: string[] = [];
    const server = createServer((request, response) => {
      paths.push(request.url ?? '');
      request.resume();
      response.writeHead(401, { 'Content-Type': 'application/json', Connection: 'close' });
      response.end('{"message":"Unauthenticated."}');
    });
    server.listen(0, '127.0.0.1');
    await once(server, 'listening');
    const address = server.address();
    if (!address || typeof address === 'string') throw new Error('Missing capture address');
    const redirect: typeof fetch = (input, init) => {
      const request = new Request(input, init);
      const target = new URL(request.url);
      expect(target.origin).toBe(new URL(baseUrl).origin);
      target.protocol = 'http:';
      target.hostname = '127.0.0.1';
      target.port = String(address.port);
      return globalThis.fetch(new Request(target, request));
    };
    try {
      for (const mode of ['configured', 'per-call', 'custom-client']) {
        configurePlainrouter({ baseUrl: mode === 'configured' ? baseUrl : 'http://127.0.0.1:1', fetch: redirect, signalTrackerSecret: 'loopback' });
        for (const responseStyle of ['fields', 'data'] as const) {
          for (const throwOnError of [false, true]) {
            const result = launcherFileImport({
              body: { file: new Blob(['image']), source_adset_id: '123', source_ad_id: '456', mode: 'duplicate_adset' },
              ...(mode === 'per-call' ? { baseUrl } : {}),
              ...(mode === 'custom-client' ? { client: createClient({ baseUrl, fetch: redirect }) } : {}),
              responseStyle, throwOnError,
            });
            if (throwOnError) await expect(result).rejects.toEqual({ message: 'Unauthenticated.' });
            else await result;
          }
        }
      }
      expect(paths).toEqual(Array(12).fill(expected));
    } finally {
      await new Promise<void>((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));
    }
  });
});
