import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';

const checksumText = await readFile(
  new URL('../spec/CHECKSUM', import.meta.url),
  'utf8',
);
const checksum = Object.fromEntries(
  checksumText
    .trim()
    .split('\n')
    .map((line) => {
      const separator = line.indexOf(':');

      return [line.slice(0, separator), line.slice(separator + 1).trim()];
    }),
);

try {
  const response = await fetch(checksum.source);

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const liveBytes = Buffer.from(await response.arrayBuffer());
  const liveDigest = createHash('sha256').update(liveBytes).digest('hex');

  if (liveDigest === checksum.sha256) {
    console.log(`Live contract matches vendored sha256 ${liveDigest}.`);
  } else {
    console.log(
      `::warning title=OpenAPI spec drift::Live sha256 ${liveDigest} differs from vendored sha256 ${checksum.sha256}.`,
    );
  }
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);

  console.log(
    `::warning title=OpenAPI spec drift check unavailable::Could not fetch ${checksum.source}: ${message}`,
  );
}
