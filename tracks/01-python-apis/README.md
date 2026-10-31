# 01 — Python & APIs: Lexical Retrieval Baseline

**Status: locally tested, not deployed.** This is a deterministic retrieval baseline, **not** an LLM, embedding model, or production RAG system. It demonstrates Python 3.13, typed FastAPI, strict Pydantic validation, automated tests, containerization and CI.

## Problem and intended user

Before spending tokens on a language model, an AI engineer needs a cheap, explainable baseline. This API ranks short documents by the fraction of distinct query tokens present in each document. It can serve as a control in future retrieval evaluations.

## Input / output

- GET /healthz returns {"status":"ok"}.
- POST /v1/rank returns ordered matching document IDs, scores and matched query terms. Zero-overlap documents are excluded.
- Score = distinct matching query tokens / distinct query tokens (0–1). Case-insensitive Unicode word tokens; no stemming, embeddings, stop-word removal or semantic understanding. Ties preserve input order.
- Limits: query <= 500 characters; 1–20 documents, each 1–2,000 characters; top_k between 1 and 20. Document IDs must be unique ASCII letters/digits/underscore/hyphen, up to 64 characters. Invalid input returns HTTP 422.

## Run locally

~~~bash
cd tracks/01-python-apis
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
~~~

Windows: activate the environment using .venv/Scripts/activate instead.

Example request:

~~~bash
curl -sS -X POST http://127.0.0.1:8000/v1/rank \
  -H 'Content-Type: application/json' \
  -d '{"query":"secure ai agents","documents":[{"id":"a","text":"Secure agents with audit logs"},{"id":"b","text":"Cooking recipes"}],"top_k":2}'
~~~

Expected response:

~~~json
{"matches":[{"id":"a","score":0.6666666666666666,"matched_terms":["agents","secure"]}],"algorithm":"query_term_recall_v1"}
~~~

## Tests and quality

~~~bash
python -m pytest -q
python -m ruff check .
python -m compileall -q app tests
~~~

CI runs pytest and Ruff on pull requests that change this project. Runtime and development direct dependencies are pinned in separate files, but transitive packages are **not** locked; a fully reproducible lockfile remains a follow-up. No external model or API key is required.

## Container

~~~bash
docker build -t lexical-baseline .
docker run --rm -p 127.0.0.1:8000:8000 lexical-baseline
~~~

The container uses a non-root user. Image digest pinning and vulnerability scans remain TODO. The service is deliberately unauthenticated; **do not expose it publicly** without authentication, rate limiting and deployment controls.

## Security and privacy

Input sizes, field names, and IDs are validated; duplicate IDs and unknown fields are rejected. Document content is treated as untrusted text, never as executable instructions. Responses omit original document text and use Cache-Control: no-store and X-Content-Type-Options: nosniff. No document storage or model provider is used. These controls do **not** replace authentication, TLS, rate limiting, threat modeling or secure hosting.

## Evaluation and limitations

Unit and HTTP contract tests verify the deterministic scoring formula, stable ties, Unicode case-folding, empty matches, invalid input and input limits. There is **no** labeled retrieval dataset or real-world quality benchmark yet. No model accuracy, production uptime, throughput or cost metrics are claimed. Exact word matching misses synonyms, morphology and context; a future track should compare this baseline against BM25 and vector retrieval using the same held-out dataset.

## Attribution

Implementation is original for this portfolio. No third-party example code or datasets were copied. Dependency licenses remain governed by their respective upstream projects; no repository-wide reuse license is asserted here.
