from models.tool_result import ToolResult


def test_tool_result_creation():

    result = ToolResult(
        tool="arxiv",
        success=True,
        data=[],
        error=None,
    )

    assert result.tool == "arxiv"
    assert result.success is True
    assert result.data == []
    assert result.error is None