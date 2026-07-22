from duckduckgo_search import DDGS

from backend.agent_tools.base_tool import BaseTool
from backend.models.tool_result import ToolResult


class WebSearchTool(BaseTool):
    """
    Tool for searching the web using DuckDuckGo.
    """

    def __init__(self, max_results: int = 3):
        self.max_results = max_results

    def run(self, query: str) -> ToolResult:

        if not query.strip():
            return ToolResult(
                tool="web_search",
                success=False,
                data=[],
                error="Query cannot be empty."
            )

        try:
            results = []

            with DDGS() as ddgs:
                search_results = ddgs.text(
                    query,
                    max_results=self.max_results
                )

                for item in search_results:
                    results.append(
                        {
                            "title": item.get("title"),
                            "body": item.get("body"),
                            "url": item.get("href"),
                        }
                    )

            return ToolResult(
                tool="web_search",
                success=True,
                data=results,
                error=None,
            )

        except Exception as e:
            return ToolResult(
                tool="web_search",
                success=False,
                data=[],
                error=str(e),
            )