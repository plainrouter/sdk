import { Writable } from 'node:stream';
import { createInterface } from 'node:readline';
import { createInterface as createPromisesInterface } from 'node:readline/promises';

export const promptForToken = async (
  question: string,
  input: NodeJS.ReadableStream = process.stdin,
  output: NodeJS.WritableStream = process.stderr,
): Promise<string> => {
  output.write(question);

  const mutedOutput = new Writable({
    write(_chunk, _encoding, callback) {
      callback();
    },
  });
  const readline = createInterface({
    input,
    output: mutedOutput,
    terminal: Boolean((input as NodeJS.ReadStream).isTTY),
  });

  try {
    const token = await new Promise<string>((resolve) => {
      readline.question('', resolve);
    });

    output.write('\n');

    return token.trim();
  } finally {
    readline.close();
  }
};

export const confirmAction = async (
  question: string,
  input: NodeJS.ReadableStream = process.stdin,
  output: NodeJS.WritableStream = process.stderr,
): Promise<boolean> => {
  const readline = createPromisesInterface({ input, output });

  try {
    const answer = await readline.question(`${question} [y/N] `);

    return /^(?:y|yes)$/i.test(answer.trim());
  } finally {
    readline.close();
  }
};
