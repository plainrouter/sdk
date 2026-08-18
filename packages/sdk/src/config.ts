import { client } from './generated/client.gen.js';

export type PlainrouterConfig = {
  signalTrackerSecret: string;
  baseUrl?: string;
  fetch?: typeof globalThis.fetch;
};

export const configurePlainrouter = ({
  signalTrackerSecret,
  baseUrl,
  fetch,
}: PlainrouterConfig) => {
  client.setConfig({
    auth: signalTrackerSecret,
    ...(baseUrl === undefined ? {} : { baseUrl }),
    ...(fetch === undefined ? {} : { fetch }),
  });

  return client;
};
