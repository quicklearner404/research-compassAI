import pytest
from pydantic import ValidationError

from backend.models.tool_result import ToolResult


def test_tool_result_creation():
    result = ToolResult(tool="arxiv", success=True, data=[], error=None)

    assert result.tool == "arxiv"
    assert result.success is True
    assert result.data == []
    assert result.error is None


def test_tool_result_defaults():
    result = ToolResult(tool="github", success=False)

    assert result.data is None
    assert result.error is None


def test_tool_result_requires_success_flag():
    with pytest.raises(ValidationError):
        ToolResult(tool="arxiv")
