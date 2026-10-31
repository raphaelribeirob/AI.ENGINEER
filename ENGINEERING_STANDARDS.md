# Definition of Done — AI Engineer Portfolio

A project can be labeled **portfolio-ready** only when applicable gates below pass.

## Reproducibility and software engineering
- Clear problem, architecture, API contract and quickstart.
- Pinned dependencies, example environment file and no committed secrets.
- Automated unit/integration tests, lint and basic CI.
- Typed and validated inputs/outputs, bounded retries and documented failure handling.

## AI-specific evaluation
- Baseline and held-out evaluation set; datasets and metrics are explained.
- RAG: retrieval quality, groundedness, citations and abstention.
- Agents: task success, tool calls, tool authorization, failure categories, cost and latency.
- Models: provenance, licenses, seeds, splits and confidence/variance where feasible.
- Mock results are always labeled mock. Never substitute them for real-model measurements.

## Security, privacy, reliability
- Least-privilege tool access, correct authorization and (where relevant) tenant isolation.
- Prompt injection and retrieved-content trust boundaries tested.
- Secrets and personal data are not leaked in commits, output or logs.
- Rate limiting, timeouts, budgets and monitoring are designed and measured.
- Deployment/rollback/health checks documented; current production status verified.

## Documentation and attribution
- Follow [the reusable README template](templates/PROJECT_README.md).
- Report genuine status and known gaps.
- Credit upstream repositories and retain required notices/licenses.
- Screenshots and demos must show actual behavior, not only mockups.
