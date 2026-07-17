import pytest

from agent_tools.base_tool import BaseTool


def test_base_tool_is_abstract():
    with pytest.raises(TypeError):
        BaseTool()