from smolagents import Tool

from agent_tools.arxiv_tool import ArxivTool
from agent_tools.github_tool import GitHubTool
from agent_tools.web_search_tool import WebSearchTool


class ArxivSearchTool(Tool):
    name = "arxiv_search"
    description = (
        "Search arXiv for research papers related to a research topic. "
        "Use this tool whenever the user asks for papers, publications, surveys, or academic research."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "Research topic to search for."
        }
    }

    output_type = "object"

    def __init__(self):
        super().__init__()
        self.tool = ArxivTool()

    def forward(self, query: str):
        result = self.tool.run(query)
        return result.data


class GitHubSearchTool(Tool):
    name = "github_search"
    description = (
        "Search GitHub for repositories related to a research topic. "
        "Use this tool whenever code implementations or projects are needed."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "Research topic to search GitHub for."
        }
    }

    output_type = "object"

    def __init__(self):
        super().__init__()
        self.tool = GitHubTool()

    def forward(self, query: str):
        result = self.tool.run(query)
        return result.data


class DuckDuckGoSearchTool(Tool):
    name = "web_search"
    description = (
        "Search the web for tutorials, blogs, documentation and learning resources."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "Topic to search on the web."
        }
    }

    output_type = "object"

    def __init__(self):
        super().__init__()
        self.tool = WebSearchTool()

    def forward(self, query: str):
        result = self.tool.run(query)
        return result.data