# Changelog

## 0.10.0 (unreleased)

- The 503 ProposalUnavailable model includes proposal_not_recorded and workspace_lock_timeout. is_retryable_proposal_error(status_code, parsed) identifies the known retryable model; Response.headers retains Retry-After.
- Regenerate from core main `40a2c3f1563aaa489d5658ef6058ffb6a613709c` with the existing pinned generator and settings.
- Include core contract changes: bounded Actions and Launch projections/continuations, rule summaries, workspace creative and account inventory reads, frozen target evidence, and delivery incident attention/held states. The unused DeploymentPlan schema is removed upstream; creative MCP metadata schemas reflect the template-only connector contract.
