from types import SimpleNamespace

from github import GithubException

from backend.agent_tools.github_tool import GitHubTool


def _repo(name: str, description: str | None = "A repo"):
    return SimpleNamespace(
        full_name=name,
        description=description,
        stargazers_count=42,
        language="Python",
        html_url=f"https://github.com/{name}",
    )


class FakeGithub:
    def __init__(self, repos=None, error=None):
        self.repos = repos or []
        self.error = error
        self.calls = []

    def search_repositories(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return self.repos


def _tool_with(fake, **kwargs):
    tool = GitHubTool(**kwargs)
    tool.github = fake
    return tool


def test_empty_query_is_rejected_without_api_call():
    fake = FakeGithub()
    tool = _tool_with(fake)

    result = tool.run("   ")

    assert result.success is False
    assert result.error == "Query cannot be empty."
    assert fake.calls == []


def test_results_are_limited_and_normalized():
    fake = FakeGithub([_repo(f"org/repo{i}") for i in range(10)])
    tool = _tool_with(fake, max_results=2)

    result = tool.run("graph neural networks")

    assert result.success is True
    assert len(result.data) == 2
    assert result.data[0] == {
        "name": "org/repo0",
        "description": "A repo",
        "stars": 42,
        "language": "Python",
        "url": "https://github.com/org/repo0",
    }
    assert fake.calls[0] == {
        "query": "graph neural networks",
        "sort": "stars",
        "order": "desc",
    }


def test_missing_description_becomes_empty_string():
    tool = _tool_with(FakeGithub([_repo("org/x", description=None)]))

    assert tool.run("x").data[0]["description"] == ""


def test_long_description_is_truncated():
    tool = _tool_with(FakeGithub([_repo("org/x", description="d" * 500)]))

    description = tool.run("x").data[0]["description"]

    assert description.endswith("...")
    assert len(description) == tool.max_description_length + 3


def test_github_errors_are_reported_not_raised():
    error = GithubException(403, {"message": "rate limit exceeded"}, None)
    tool = _tool_with(FakeGithub(error=error))

    result = tool.run("llm")

    assert result.success is False
    assert "rate limit" in result.error
