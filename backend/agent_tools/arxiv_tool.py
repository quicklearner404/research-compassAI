from arxiv import Client, Search, SortCriterion

from backend.agent_tools.base_tool import BaseTool
from backend.models.tool_result import ToolResult


class ArxivTool(BaseTool):
    """
    Tool for searching research papers on arXiv.
    """

    QUERY_ENRICHMENTS = {
        "transformer": '"transformer" machine learning',
        "transformers": '"transformer" machine learning',
        "cnn": '"convolutional neural network" deep learning',
        "bert": '"bert" natural language processing',
        "gpt": '"gpt" large language model',
        "llm": '"large language model"',
        "vit": '"vision transformer"',
        "clip": '"clip" vision language model',
        "gan": '"generative adversarial network"',
        "diffusion": '"diffusion model"',
        "rag": '"retrieval augmented generation"',
    }

    def __init__(self, max_results: int = 3):
        self.client = Client()
        self.max_results = max_results
        self.max_summary_length = 300

    def _enrich_query(self, query: str) -> str:
        normalized = query.lower().strip()

        # Only enrich ambiguous one-word queries
        if len(normalized.split()) == 1:
            return self.QUERY_ENRICHMENTS.get(
                normalized,
                query,
            )

        return query

    def run(self, query: str) -> ToolResult:
        try:
            query = self._enrich_query(query)

            # Uncomment while debugging
            # print(f"[Arxiv] Searching: {query}")

            search = Search(
                query=query,
                max_results=self.max_results,
                sort_by=SortCriterion.Relevance,
            )

            papers = []

            for result in self.client.results(search):

                summary = result.summary.strip()

                if len(summary) > self.max_summary_length:
                    summary = (
                        summary[: self.max_summary_length].rstrip()
                        + "..."
                    )

                papers.append(
                    {
                        "title": result.title,
                        "authors": [author.name for author in result.authors],
                        "summary": summary,
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