from backend.agent_tools import web_search_tool
from backend.agent_tools.web_search_tool import WebSearchTool


class FakeDDGS:
    results = []
    error = None
    calls = []

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def text(self, query, max_results):
        FakeDDGS.calls.append((query, max_results))
        if FakeDDGS.error:
            raise FakeDDGS.error
        return FakeDDGS.results[:max_results]


def _install_fake(monkeypatch, results=None, error=None):
    FakeDDGS.results = results or []
    FakeDDGS.error = error
    FakeDDGS.calls = []
    monkeypatch.setattr(web_search_tool, "DDGS", FakeDDGS)


def test_empty_query_is_rejected(monkeypatch):
    _install_fake(monkeypatch)

    result = WebSearchTool().run("")

    assert result.success is False
    assert result.error == "Query cannot be empty."
    assert FakeDDGS.calls == []


def test_results_are_mapped_to_title_body_url(monkeypatch):
    _install_fake(
        monkeypatch,
        results=[
            {"title": "Intro to LLMs", "body": "An overview", "href": "https://a.example"},
            {"title": "Second", "body": "More", "href": "https://b.example"},
            {"title": "Third", "body": "Even more", "href": "https://c.example"},
        ],
    )

    result = WebSearchTool(max_results=2).run("large language models")

    assert result.success is True
    assert result.data == [
        {"title": "Intro to LLMs", "body": "An overview", "url": "https://a.example"},
        {"title": "Second", "body": "More", "url": "https://b.example"},
    ]
    assert FakeDDGS.calls == [("large language models", 2)]


def test_search_errors_are_reported_not_raised(monkeypatch):
    _install_fake(monkeypatch, error=RuntimeError("rate limited"))

    result = WebSearchTool().run("llm")

    assert result.success is False
    assert result.error == "rate limited"
