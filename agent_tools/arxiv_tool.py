from arxiv import Client, Search, SortCriterion

from agent_tools.base_tool import BaseTool
from models.tool_result import ToolResult


class ArxivTool(BaseTool):
    """
    Tool for searching research papers on arXiv.
    """

    def __init__(self, max_results: int = 3):
        self.client = Client()
        self.max_results = max_results

    def run(self, query: str) -> ToolResult:
        try:
            search = Search(
                query=query,
                max_results=self.max_results,
                sort_by=SortCriterion.Relevance,
            )

            papers = []

            for result in self.client.results(search):
                papers.append(
                    {
                        "title": result.title,
                        "authors": [a.name for a in result.authors],
                        "summary": result.summary,
                        "published": result.published.strftime("%Y-%m-%d"),
                        "pdf_url": result.pdf_url,
                    }
                )

            return ToolResult(
                tool="arxiv",
                success=True,
                data=papers,
            )

        except Exception as e:
            return ToolResult(
                tool="arxiv",
                success=False,
                error=str(e),
            )