from datetime import datetime
from types import SimpleNamespace

from backend.agent_tools.arxiv_tool import ArxivTool


def _paper(title: str, summary: str = "A short abstract."):
    return SimpleNamespace(
        title=title,
        authors=[SimpleNamespace(name="Ada Lovelace"), SimpleNamespace(name="Alan Turing")],
        summary=f"  {summary}  ",
        published=datetime(2024, 5, 17),
        pdf_url=f"https://arxiv.org/pdf/{title}",
    )


class FakeClient:
    def __init__(self, papers=None, error=None):
        self.papers = papers or []
        self.error = error
        self.searches = []

    def results(self, search):
        self.searches.append(search)
        if self.error:
            raise self.error
        return iter(self.papers)


def _tool_with(client, **kwargs):
    tool = ArxivTool(**kwargs)
    tool.client = client
    return tool


def test_returns_normalized_papers():
    tool = _tool_with(FakeClient([_paper("p1"), _paper("p2")]), max_results=2)

    result = tool.run("Graph Neural Networks")

    assert result.success is True
    assert result.tool == "arxiv"
    assert [p["title"] for p in result.data] == ["p1", "p2"]
    assert result.data[0] == {
        "title": "p1",
        "authors": ["Ada Lovelace", "Alan Turing"],
        "summary": "A short abstract.",
        "published": "2024-05-17",
        "pdf_url": "https://arxiv.org/pdf/p1",
    }


def test_long_summaries_are_truncated():
    tool = _tool_with(FakeClient([_paper("p", "x" * 1000)]))

    summary = tool.run("anything").data[0]["summary"]

    assert summary.endswith("...")
    assert len(summary) == tool.max_summary_length + 3


def test_search_uses_enriched_query_and_limit():
    client = FakeClient([])
    tool = _tool_with(client, max_results=5)

    tool.run("rag")

    search = client.searches[0]
    assert search.query == '"retrieval augmented generation"'
    assert search.max_results == 5


def test_api_errors_are_reported_not_raised():
    tool = _tool_with(FakeClient(error=ConnectionError("arXiv is down")))

    result = tool.run("transformers")

    assert result.success is False
    assert "arXiv is down" in result.error

