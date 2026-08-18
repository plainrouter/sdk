export type TextWriter = (text: string) => void;

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);

const printableValue = (value: unknown): string => {
  if (value === null) {
    return 'null';
  }

  if (typeof value === 'object') {
    return JSON.stringify(value);
  }

  return String(value);
};

const renderTable = (rows: Array<Record<string, unknown>>): string => {
  if (rows.length === 0) {
    return '(none)';
  }

  const columns = Array.from(
    new Set(rows.flatMap((row) => Object.keys(row))),
  );
  const widths = columns.map((column) =>
    Math.max(
      column.length,
      ...rows.map((row) => printableValue(row[column]).length),
    ),
  );
  const line = (values: string[]): string =>
    values.map((value, index) => value.padEnd(widths[index] ?? 0)).join('  ');

  return [
    line(columns),
    line(columns.map((_column, index) => '-'.repeat(widths[index] ?? 0))),
    ...rows.map((row) =>
      line(columns.map((column) => printableValue(row[column]))),
    ),
  ].join('\n');
};

export const formatHuman = (data: unknown): string => {
  if (Array.isArray(data)) {
    if (data.every(isRecord)) {
      return renderTable(data);
    }

    return data.map(printableValue).join('\n');
  }

  if (!isRecord(data)) {
    return printableValue(data);
  }

  const lines: string[] = [];

  for (const [key, value] of Object.entries(data)) {
    if (Array.isArray(value) && value.every(isRecord)) {
      lines.push(`${key}:`, renderTable(value));
    } else if (isRecord(value)) {
      lines.push(`${key}:`, formatHuman(value));
    } else {
      lines.push(`${key}: ${printableValue(value)}`);
    }
  }

  return lines.join('\n');
};

export const writeResponse = (
  data: unknown,
  asJson: boolean,
  write: TextWriter,
): void => {
  write(`${asJson ? JSON.stringify(data, null, 2) : formatHuman(data)}\n`);
};

export const formatApiError = (error: unknown): string => {
  if (isRecord(error) && typeof error.message === 'string') {
    if (isRecord(error.errors)) {
      const details = Object.entries(error.errors).flatMap(([field, messages]) =>
        Array.isArray(messages)
          ? messages.map((message) => `${field}: ${String(message)}`)
          : [`${field}: ${String(messages)}`],
      );

      return details.length > 0
        ? `${error.message}\n${details.join('\n')}`
        : error.message;
    }

    return error.message;
  }

  if (error instanceof Error) {
    return error.message;
  }

  if (isRecord(error)) {
    return JSON.stringify(error);
  }

  return String(error || 'Unknown API error');
};

export const maskToken = (token: string): string => {
  if (token.length <= 4) {
    return '••••';
  }

  return `••••${token.slice(-4)}`;
};
