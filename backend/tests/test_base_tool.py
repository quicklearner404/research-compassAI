import pytest

from backend.agent_tools.base_tool import BaseTool
from backend.models.tool_result import ToolResult


def test_base_tool_is_abstract():
    with pytest.raises(TypeError):
        BaseTool()


def test_subclass_must_implement_run():
    class Incomplete(BaseTool):
        pass

    with pytest.raises(TypeError):
        Incomplete()


def test_concrete_subclass_runs():
    class Echo(BaseTool):
        def run(self, query: str) -> ToolResult:
            return ToolResult(tool="echo", success=True, data=query)

    assert Echo().run("hi").data == "hi"
