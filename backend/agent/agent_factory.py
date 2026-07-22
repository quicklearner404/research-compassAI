from smolagents import ToolCallingAgent

from backend.agent.tool_registry import get_tools
from backend.agent.prompts import SYSTEM_PROMPT


def build_agent(model):
    return ToolCallingAgent(
        tools=get_tools(),
        model=model,
        instructions=SYSTEM_PROMPT,
        max_steps=6,
    )