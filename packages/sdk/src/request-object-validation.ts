import * as z from 'zod';

export type RequestObjectSchema = {
  additionalProperties?: false | RequestObjectSchema;
  allOf?: readonly RequestObjectSchema[];
  anyOf?: readonly RequestObjectSchema[];
  closed?: boolean;
  const?: unknown;
  enum?: readonly unknown[];
  items?: RequestObjectSchema;
  oneOf?: readonly RequestObjectSchema[];
  properties?: Readonly<Record<string, RequestObjectSchema>>;
};

type SchemaDefinition = Record<string, unknown> & { type: string };
type ClosedObjectErrorMap = z.core.$ZodErrorMap;
type SchemaPath = readonly string[];

const containsClosedObject = (schema: RequestObjectSchema): boolean => (
  schema.closed === true
  || Object.values(schema.properties ?? {}).some(containsClosedObject)
  || (typeof schema.additionalProperties === 'object' && containsClosedObject(schema.additionalProperties))
  || Boolean(schema.items && containsClosedObject(schema.items))
  || (schema.anyOf ?? []).some(containsClosedObject)
  || (schema.oneOf ?? []).some(containsClosedObject)
  || (schema.allOf ?? []).some(containsClosedObject)
);

const hasNestedClosedObject = (schema: RequestObjectSchema): boolean => (
  Object.values(schema.properties ?? {}).some(containsClosedObject)
  || (typeof schema.additionalProperties === 'object' && containsClosedObject(schema.additionalProperties))
  || Boolean(schema.items && containsClosedObject(schema.items))
  || (schema.anyOf ?? []).some(containsClosedObject)
  || (schema.oneOf ?? []).some(containsClosedObject)
  || (schema.allOf ?? []).some(containsClosedObject)
);

const objectName = (rootName: string, path: SchemaPath): string => path.reduce((name, segment) => (
  segment === '[]' ? `${name}[]` : `${name}.${segment}`
), rootName);

const errorMapForClosedObject = (
  name: string,
  previousError?: ClosedObjectErrorMap,
): ClosedObjectErrorMap => (issue) => {
  if (issue.code === 'unrecognized_keys' && 'keys' in issue && Array.isArray(issue.keys)) {
    const keyNames = issue.keys.map((key) => `"${String(key)}"`).join(', ');
    const keyLabel = issue.keys.length === 1 ? 'key' : 'keys';
    return `Unknown ${keyLabel} ${keyNames} on closed request object "${name}"`;
  }

  return previousError?.(issue);
};

const errorMapForClosedRecord = (
  name: string,
  previousError?: ClosedObjectErrorMap,
): ClosedObjectErrorMap => (issue) => {
  if (issue.code === 'invalid_type' && issue.expected === 'never') {
    const key = issue.path?.at(-1);
    if (key !== undefined) {
      return `Unknown key "${String(key)}" on closed request object "${name}"`;
    }
  }

  return previousError?.(issue);
};

const collectUnknownKeyMessages = (value: unknown, messages = new Set<string>()): Set<string> => {
  if (Array.isArray(value)) {
    for (const item of value) collectUnknownKeyMessages(item, messages);
    return messages;
  }

  if (typeof value !== 'object' || value === null) {
    return messages;
  }

  const issue = value as Record<string, unknown>;
  if (typeof issue.message === 'string' && issue.message.startsWith('Unknown key')) {
    messages.add(issue.message);
  }
  if (issue.errors) collectUnknownKeyMessages(issue.errors, messages);

  return messages;
};

const errorMapForUnion = (previousError?: ClosedObjectErrorMap): ClosedObjectErrorMap => (issue) => {
  if (issue.code === 'invalid_union' && 'errors' in issue && Array.isArray(issue.errors)) {
    const branchErrors = issue.errors as unknown[][];
    const leastRestrictiveBranch = branchErrors.reduce<unknown[]>((current, branch) => (
      branch.length < current.length ? branch : current
    ), branchErrors[0] ?? []);
    const messages = collectUnknownKeyMessages(leastRestrictiveBranch);
    if (messages.size > 0) {
      return [...messages].join('; ');
    }
  }

  return previousError?.(issue);
};

/**
 * Rebuild only schema nodes that contain spec-closed objects. Cloning through
 * each concrete Zod type keeps public APIs such as ZodObject.shape and .extend.
 */
const applyClosedObjectRules = <T extends z.ZodType>(
  target: T,
  schema: RequestObjectSchema,
  rootName: string,
  path: SchemaPath = [],
): T => {
  if (!containsClosedObject(schema)) {
    return target;
  }

  const definition = target._zod.def as SchemaDefinition;
  const clone = (changes: Record<string, unknown>): T => target.clone({ ...definition, ...changes } as never);
  const previousError = definition.error as ClosedObjectErrorMap | undefined;

  if (definition.type === 'object') {
    const currentShape = (target as unknown as z.ZodObject).shape;
    const transformedShape = Object.fromEntries(Object.entries(currentShape).map(([key, child]) => {
      const childSchema = schema.properties?.[key];
      return [key, childSchema && containsClosedObject(childSchema)
        ? applyClosedObjectRules(child, childSchema, rootName, [...path, key])
        : child];
    }));
    const originalCatchall = definition.catchall as z.ZodType | undefined;
    const additionalProperties = schema.additionalProperties;
    const catchall = typeof additionalProperties === 'object' && originalCatchall
      ? applyClosedObjectRules(originalCatchall, additionalProperties, rootName, [...path, '.*'])
      : originalCatchall;
    const changes: Record<string, unknown> = { shape: transformedShape };

    if (schema.closed) {
      changes.catchall = z.never();
      changes.error = errorMapForClosedObject(objectName(rootName, path), previousError);
    } else if (catchall !== originalCatchall) {
      changes.catchall = catchall;
    }

    if (!schema.closed && !hasNestedClosedObject(schema)) {
      return target;
    }

    return clone(changes);
  }

  if (definition.type === 'record') {
    const valueType = definition.valueType as z.ZodType | undefined;
    const additionalProperties = schema.additionalProperties;

    if (schema.closed && valueType) {
      const valueDefinition = valueType._zod.def as SchemaDefinition;
      const customNever = valueType.clone({
        ...valueDefinition,
        error: errorMapForClosedRecord(objectName(rootName, path), valueDefinition.error as ClosedObjectErrorMap | undefined),
      } as never);
      return clone({ valueType: customNever });
    }

    if (typeof additionalProperties === 'object' && valueType) {
      return clone({
        valueType: applyClosedObjectRules(valueType, additionalProperties, rootName, [...path, '.*']),
      });
    }

    return target;
  }

  if (definition.type === 'array' && schema.items) {
    const element = definition.element as z.ZodType;
    return clone({ element: applyClosedObjectRules(element, schema.items, rootName, [...path, '[]']) });
  }

  if (definition.type === 'union') {
    const branches = schema.anyOf ?? schema.oneOf ?? [];
    const options = definition.options as z.ZodType[];
    return clone({
      options: options.map((option, index) => {
        const branch = branches[index];
        return branch && containsClosedObject(branch)
          ? applyClosedObjectRules(option, branch, rootName, path)
          : option;
      }),
      error: errorMapForUnion(previousError),
    });
  }

  if (definition.type === 'intersection') {
    const branches = schema.allOf ?? [];
    const left = definition.left as z.ZodType;
    const right = definition.right as z.ZodType;
    return clone({
      left: branches[0] && containsClosedObject(branches[0])
        ? applyClosedObjectRules(left, branches[0], rootName, path)
        : left,
      right: branches[1] && containsClosedObject(branches[1])
        ? applyClosedObjectRules(right, branches[1], rootName, path)
        : right,
    });
  }

  if ('innerType' in definition && containsClosedObject(schema)) {
    const innerType = definition.innerType as z.ZodType;
    return clone({ innerType: applyClosedObjectRules(innerType, schema, rootName, path) });
  }

  return target;
};

/** Apply strict validation derived from the vendored OpenAPI request schema. */
export const withClosedRequestObjects = <T extends z.ZodType>(
  rootName: string,
  schema: RequestObjectSchema,
  target: T,
): T => applyClosedObjectRules(target, schema, rootName);
