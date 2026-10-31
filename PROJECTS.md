# AI Engineer Project Portfolio

**Review date:** 2026-10-31. Statuses below describe *documented evidence*; no CI run or deployment was performed as part of organizing this hub.

| Project | Tracks | Status | Next acceptance gate |
| --- | --- | --- | --- |
| [rag-production](https://github.com/raphaelribeirob/rag-production) | 05, 07, 09, 10 | In progress | Fix real-model groundedness gap; add prompt-injection defense, telemetry and tests |
| [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | 06, 07 | Scaffold | Implement task suite and measured comparison with deterministic test runner |
| Python API foundations | 01 | Planned | Typed endpoints + pytest + lint + CI |
| Classical ML prediction service | 02 | Planned | Dataset baseline + holdout evaluation + reproducible API |
| Deep learning training pipeline | 03 | Planned | Train/evaluate/save/reload a PyTorch model |
| Structured-output LLM gateway | 04 | Planned | Provider interface, schema validation, streaming, retries and usage metrics |
| RAG system comparison | 05, 07 | Planned | Compare sparse/dense/hybrid retrieval with identical evaluation sets |
| Permissioned tool-using agent | 06 | Planned | Enforce tool allowlist, approval policy and auditable action logs |
| Fine-tuning vs alternatives | 08 | Planned | Compare baseline, RAG and fine-tune on fixed test data |
| Production AI service | 09, 10 | Planned | Docker, monitoring, rate limits, rollback, budget and security test |
| AI product capstone | 11 | Planned | End-to-end demo and documented real use case |

## Evidence checklist per project

- Permanent commit SHA and exact installation/run commands
- Dataset provenance, holdout set and baseline
- Tests and CI result (with timestamp)
- Measured evaluation and failure cases
- Latency, token usage, cost or resource use
- Threat model and secrets/PII practices
- Demo or independently verified deployment, explicitly labeled
- Documented limitations and license

**Do not mark planned projects as complete because an upstream tutorial exists.**
