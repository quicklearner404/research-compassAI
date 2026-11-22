"""
Shared test setup.

Environment variables are set *before* any backend module is imported, so the
whole suite runs offline: no LLM calls, no API keys, and a throwaway database.
"""

import os
import tempfile

_tmp_dir = tempfile.mkdtemp(prefix="research-compass-tests-")
os.environ["DATABASE_URL"] = f"sqlite:///{os.path.join(_tmp_dir, 'test.db')}"
os.environ["USE_MOCK_LLM"] = "true"
os.environ.setdefault("LLM_PROVIDER", "huggingface")

from types import SimpleNamespace  # noqa: E402

import pytest  # noqa: E402


@pytest.fixture
def make_message():
    """Build a lightweight stand-in for a backend.models.Message row."""

    def _make(role: str, content: str):
        return SimpleNamespace(role=role, content=content)

    return _make
