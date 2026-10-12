# Changelog

## 0.6.0 (unreleased)

- ApiError#response_object decodes the known 503 ProposalUnavailable body, #retryable? identifies it, and #retry_after exposes Retry-After without changing the exception class.
- Regenerate from core main `40a2c3f1563aaa489d5658ef6058ffb6a613709c` with the existing pinned generator and settings.
- Include core contract changes: bounded Actions and Launch projections/continuations, rule summaries, workspace creative and account inventory reads, frozen target evidence, and delivery incident attention/held states. The unused DeploymentPlan schema is removed upstream; creative MCP metadata schemas reflect the template-only connector contract.
