"""
Optional smoke tests against the real arXiv / GitHub / DuckDuckGo APIs.
Skipped by default; run with:  RUN_LIVE_TESTS=1 pytest -m live
"""

import os

import pytest

from backend.agent_tools.arxiv_tool import ArxivTool
from backend.agent_tools.github_tool import GitHubTool
from backend.agent_tools.web_search_tool import WebSearchTool

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(
        os.getenv("RUN_LIVE_TESTS") != "1",
        reason="set RUN_LIVE_TESTS=1 to hit real external APIs",
    ),
]


def test_arxiv_live():
    result = ArxivTool(max_results=2).run("Graph Neural Networks")
    assert result.success, result.error
    assert len(result.data) == 2


def test_github_live():
    result = GitHubTool(max_results=2).run("Graph Neural Networks")
    assert result.success, result.error
    assert len(result.data) <= 2


def test_web_search_live():
    result = WebSearchTool(max_results=2).run("Large Language Models")
    assert result.success, result.error
    assert len(result.data) <= 2
