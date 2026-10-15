import type { ActionProposalInput } from './generated/types.gen.js';

type ActionVariant = ActionProposalInput['actions'][number];

type ExactAction<T extends ActionVariant> = T extends ActionVariant
  ? T extends { type: infer Type; params: infer Params }
    ? Params extends object
      ? Omit<T, 'params'> & {
          params: Params & Record<
            Exclude<keyof Params, keyof Extract<ActionVariant, { type: Type }>['params']>,
            never
          >;
        }
      : T
    : T
  : never;

/** Preserve inferred params keys so curated operation calls reject excess keys, including variables. */
export type ExactActionProposal<T extends ActionProposalInput> = Omit<T, 'actions'> & {
  actions: Array<ExactAction<T['actions'][number]>>;
};
