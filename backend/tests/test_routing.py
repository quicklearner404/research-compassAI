import pytest

from backend.agent.agent import needs_tools, normalize


def test_normalize_strips_punctuation_and_case():
    assert normalize("Find PAPERS, on RAG!!") == "find papers on rag"


@pytest.mark.parametrize(
    "query",
    [
        "hello",
        "hi there",
        "What is backpropagation?",
        "Explain attention in transformers",
    ],
)
def test_general_questions_use_direct_llm(query):
    assert needs_tools(query) is False


@pytest.mark.parametrize(
    "query",
    [
        "find recent papers about transformers",
        "search github for llm repos",
        "Any good tutorials on diffusion models?",
        "Latest work on RAG evaluation",
    ],
)
def test_research_requests_use_tools(query):
    assert needs_tools(query) is True


def test_keywords_match_whole_words_only():
    # "researcher" contains "research" but is not a tool request on its own
    assert needs_tools("Who was a famous researcher in AI?") is False
