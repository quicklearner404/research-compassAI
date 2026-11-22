import pytest

from backend.agent_tools.query_utils import enrich_query


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("rag", '"retrieval augmented generation"'),
        ("  ViT ", '"vision transformer"'),
        ("LLM", '"large language model"'),
    ],
)
def test_single_ambiguous_keyword_is_expanded(query, expected):
    assert enrich_query(query) == expected


def test_unknown_single_word_is_unchanged():
    assert enrich_query("pytorch") == "pytorch"


def test_multi_word_query_is_unchanged():
    query = "rag for legal documents"
    assert enrich_query(query) == query
