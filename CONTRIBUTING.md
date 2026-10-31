# Project Development Workflow

- One independently runnable project per directory or dedicated repository.
- Use a concise English README with real problem, setup, tests, evaluation and limitations.
- Work in feature branches; open a pull request containing a measurable acceptance checklist.
- Never commit API keys, customer data or unlicensed datasets.
- Use deterministic tests and mock providers for ordinary CI; run real-model evaluations separately and report them accurately.
- Use issue labels such as \`planned\`, \`in-progress\`, \`needs-eval\`, \`security-review\`, \`verified\`.
- Keep external portfolio repositories as links unless consolidation is explicitly justified.
- Prefer maintainable, boring architecture before introducing complex agent frameworks.

For a new project, start from [templates/PROJECT_README.md](templates/PROJECT_README.md).
