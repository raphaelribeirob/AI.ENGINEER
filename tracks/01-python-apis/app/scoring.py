"""A small, explainable baseline for retrieval before adding an LLM."""

import re
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RankedDocument:
    id: str
    score: float
    matched_terms: tuple[str, ...]


def tokenize(text: str) -> frozenset[str]:
    """Return distinct case-insensitive Unicode word tokens."""
    return frozenset(re.findall(r"\w+", text.casefold(), flags=re.UNICODE))


def rank_documents(
    query: str, documents: Sequence[tuple[str, str]], top_k: int
) -> list[RankedDocument]:
    """Rank by query-term recall; ties keep input order, zero matches are omitted."""
    query_terms = tokenize(query)
    if not query_terms:
        raise ValueError("query must contain at least one word token")
    if top_k < 1:
        raise ValueError("top_k must be positive")

    results: list[RankedDocument] = []
    for doc_id, text in documents:
        matched = query_terms & tokenize(text)
        if matched:
            results.append(
                RankedDocument(
                    id=doc_id,
                    score=len(matched) / len(query_terms),
                    matched_terms=tuple(sorted(matched)),
                )
            )
    results.sort(key=lambda item: -item.score)  # Stable for ties.
    return results[:top_k]
