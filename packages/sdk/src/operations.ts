import * as generated from './generated/sdk.gen.js';
import type { Config } from './generated/client/types.gen.js';
import { normalizeHeaders } from './headers.js';

type Operation = (options: never) => unknown;

// Preserve each generated signature, including its generics and optional options.
const normalizeOperation = <T extends Operation>(operation: T): T => (
  (options: { headers?: Config['headers']; auth?: Config['auth'] } | undefined) => {
    if (options === undefined) return operation(options as never);
    const headers = normalizeHeaders(options.headers);
    return operation({
      ...options,
      headers,
      // Generated bearer auth otherwise overwrites an explicit Authorization.
      ...(typeof headers.authorization === 'string' ? { auth: undefined } : {}),
    } as never);
  }
) as unknown as T;

// Normalize before generated body operations spread headers into Content-Type defaults.
const operations = Object.fromEntries(
  Object.entries(generated).map(([name, operation]) => [name, normalizeOperation(operation)]),
) as typeof generated;

export const {
  actionsApiDryRun,
  actionsApiIndex,
  actionsApiPropose,
  actionsApiPolicy,
  actionsApiDecisionReceipt,
  actionsApiShow,
  actionsApiBatch,
  actionsRulesIndex,
  actionsTestsApiIndex,
  actionsTestsApiStore,
  actionsTestsApiShow,
  getCookieDeclaration,
  launchCreativesIndex,
  storeCreative,
  storeCreativeFromUrl,
  launchPlansCopy,
  launchPlansExecute,
  launchPlansIndex,
  launchPlansShow,
  createEvent,
  verifySignalIngestion,
  getEvent,
  getAccountInventory,
  getInventoryMetrics,
  listEvents,
  listEventsByCursor,
  setDestinationTestMode,
  sendTestPurchase,
  replayDeliveries,
  getReconciliationReport,
  getEmqReport,
  deleteUserData,
  getSandbox,
  getSandboxKey,
  createSandboxKey,
  validateSandboxEvent,
  validateSandboxEventWithKey,
} = operations;
