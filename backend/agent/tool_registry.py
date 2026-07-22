from backend.agent.hf_tools import (
    ArxivSearchTool,
    GitHubSearchTool,
    DuckDuckGoSearchTool,
)


def get_tools():
    return [
        ArxivSearchTool(),
        GitHubSearchTool(),
        DuckDuckGoSearchTool(),
    ]