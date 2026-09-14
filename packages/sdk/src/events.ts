import { createEvent as generatedCreateEvent } from './generated/sdk.gen.js';
import type {
  CreateEventData,
  CreateEventErrors,
  CreateEventResponses,
} from './generated/types.gen.js';
import type { Options } from './generated/sdk.gen.js';
import type { RequestResult } from './generated/client/index.js';

/**
 * The exact capture-time grammar from app/Domains/Signals/Data/ConsentDecision.php.
 * JavaScript does not support PHP's \A and \z anchors, so they are translated
 * to the equivalent absolute anchors when this copied pattern is compiled.
 */
export const CAPTURED_AT_PATTERN = String.raw`/\A(?<datetime>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(?<fraction>\d{1,6}))?(?<offset>Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)\z/`;

const capturedAtRegex = new RegExp(
  CAPTURED_AT_PATTERN.slice(1, -1).replace('\\A', '^').replace('\\z', '$'),
);

const isLeapYear = (year: number): boolean =>
  year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);

const daysInMonth = (year: number, month: number): number => {
  if (month === 2) {
    return isLeapYear(year) ? 29 : 28;
  }

  return [4, 6, 9, 11].includes(month) ? 30 : 31;
};

const hasValidCalendarTime = (datetime: string): boolean => {
  const [yearText, monthText, dayText, hourText, minuteText, secondText] =
    datetime.match(/\d+/g) ?? [];
  const year = Number(yearText);
  const month = Number(monthText);
  const day = Number(dayText);
  const hour = Number(hourText);
  const minute = Number(minuteText);
  const second = Number(secondText);

  return (
    Number.isInteger(year) &&
    Number.isInteger(month) &&
    Number.isInteger(day) &&
    Number.isInteger(hour) &&
    Number.isInteger(minute) &&
    Number.isInteger(second) &&
    month >= 1 &&
    month <= 12 &&
    day >= 1 &&
    day <= daysInMonth(year, month) &&
    hour >= 0 &&
    hour <= 23 &&
    minute >= 0 &&
    minute <= 59 &&
    second >= 0 &&
    second <= 59
  );
};

const hasValidCapturedAtFormat = (value: unknown): value is string => {
  if (typeof value !== 'string') {
    return false;
  }

  const match = capturedAtRegex.exec(value);

  return match !== null && hasValidCalendarTime(match.groups?.datetime ?? '');
};

/**
 * Validate the identity/capture-time relationship before POST /events builds a request.
 */
export const validateCreateEventBody = (body: unknown): void => {
  if (typeof body !== 'object' || body === null || Array.isArray(body)) {
    return;
  }

  const eventBody = body as Record<string, unknown>;
  const identityPresent =
    (eventBody.visitor_id !== undefined && eventBody.visitor_id !== null) ||
    (eventBody.user_data !== undefined && eventBody.user_data !== null);

  if (!identityPresent) {
    return;
  }

  const consent = eventBody.consent;
  const capturedAt =
    typeof consent === 'object' && consent !== null && !Array.isArray(consent)
      ? (consent as Record<string, unknown>).captured_at
      : undefined;

  if (capturedAt === undefined || capturedAt === null) {
    throw new Error(
      'consent.captured_at is required when visitor_id or user_data is present (missing).',
    );
  }

  if (!hasValidCapturedAtFormat(capturedAt)) {
    throw new Error(
      'consent.captured_at has invalid format; expected the strict ISO-8601 capture time grammar (invalid format).',
    );
  }
};

export const createEvent = <ThrowOnError extends boolean = false>(
  options: Options<CreateEventData, ThrowOnError>,
): RequestResult<CreateEventResponses, CreateEventErrors, ThrowOnError> => {
  validateCreateEventBody(options.body);

  return generatedCreateEvent(options);
};
