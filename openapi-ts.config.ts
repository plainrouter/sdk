import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  input: './spec/openapi.json',
  output: {
    module: {
      extension: '.js',
    },
    path: './packages/sdk/src/generated',
  },
  plugins: [
    '@hey-api/typescript',
    '@hey-api/client-fetch',
    '@hey-api/sdk',
    'zod',
  ],
});
