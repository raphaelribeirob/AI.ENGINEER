# AI Engineer Career Roadmap

This is a **project-first** path for applied AI engineering; phases represent skills and gates, not promises about hiring timelines.

| Phase | Tracks | Hands-on outcome |
| --- | --- | --- |
| Foundations | 01–03 | Python service + ML baseline + PyTorch training |
| GenAI systems | 04–05 | LLM interface with schemas + evaluated RAG |
| Agent engineering | 06–07 | Permissioned tool-use agent + repeatable benchmark |
| Advanced AI | 08 | Compare prompting, retrieval and fine-tuning on one task |
| Production engineering | 09–10 | Deploy, observe, secure and cost-control an AI system |
| Capstone | 11 | Deliver a full customer-oriented application |

## Learning loop

1. Define user problem, inputs, outputs and success criteria.
2. Build the cheapest deterministic baseline first.
3. Add the AI component only where it brings measured improvement.
4. Test timeouts, invalid responses, malicious inputs and authorization boundaries.
5. Evaluate accuracy, latency, tool correctness, cost and failure rate.
6. Publish run commands, exact environment, measured results and limitations.
7. Ship a reproducible demo; independently verify deployment before claiming it.

## Next concrete work

1. Resolve the open quality/security/observability gaps in [rag-production](https://github.com/raphaelribeirob/rag-production).
2. Make [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) executable end-to-end with actual measurements.
3. Implement the [01 Python & APIs](tracks/01-python-apis/README.md) project as a small, independent, tested service.
4. Build the [04 LLM Engineering](tracks/04-llm-engineering/README.md) structured-output gateway and compare providers.
5. Publish one capstone only after acceptance criteria pass.

## Status definitions

- **Planned** — requirements documented, no implementation claimed.
- **Scaffold** — initial code or structure, not end-to-end validated.
- **In progress** — important requirements still missing.
- **Verified locally** — reproducible run and test evidence exists.
- **Verified deployed** — a live environment was independently checked.
- **Portfolio-ready** — documentation, quality, safety and evidence gates are satisfied.

Do not confuse third-party labels such as “production-ready” with independent verification.
