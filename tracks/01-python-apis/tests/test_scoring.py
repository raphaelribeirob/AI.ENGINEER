"""Unit tests for deterministic scoring behavior."""

import pytest

from app.scoring import rank_documents, tokenize


def test_unicode_and_casefold_tokenization() -> None:
    assert tokenize("CAFÉ café A.I.") == frozenset({"café", "a", "i"})


def test_ranking_is_stable_and_explainable() -> None:
    docs = [("first", "secure agent"), ("second", "agent secure"), ("third", "agent")]
    result = rank_documents("secure agent", docs, top_k=2)
    assert [item.id for item in result] == ["first", "second"]
    assert result[0].score == 1.0
    assert result[0].matched_terms == ("agent", "secure")


def test_no_match_returns_empty_list() -> None:
    assert rank_documents("python", [("one", "cooking recipes")], 3) == []


def test_repeated_query_terms_do_not_inflate_score() -> None:
    result = rank_documents("ai ai agents", [("one", "agents")], 1)
    assert result[0].score == 0.5


@pytest.mark.parametrize("query,top_k", [("!!!", 1), ("hello", 0)])
def test_invalid_direct_calls(query: str, top_k: int) -> None:
    with pytest.raises(ValueError):
        rank_documents(query, [("one", "hello")], top_k)
