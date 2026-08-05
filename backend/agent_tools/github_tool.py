from github import Github, GithubException, Auth

from backend.agent_tools.base_tool import BaseTool
from backend.models.tool_result import ToolResult
from config import GITHUB_TOKEN


class GitHubTool(BaseTool):
    """
    Tool for searching GitHub repositories.
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
        self.max_results = max_results
        self.max_description_length = 200

        if not GITHUB_TOKEN:
            self.github = Github()
            return

        auth = Auth.Token(GITHUB_TOKEN)
        self.github = Github(auth=auth)

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

        if not query.strip():
            return ToolResult(
                tool="github",
                success=False,
                data=[],
                error="Query cannot be empty.",
            )

        try:

            query = self._enrich_query(query)

            # Uncomment while debugging
            # print(f"[GitHub] Searching: {query}")

            repositories = self.github.search_repositories(
                query=query,
                sort="stars",
                order="desc",
            )

            results = []

            for repo in repositories[: self.max_results]:

                description = repo.description or ""

                if len(description) > self.max_description_length:
                    description = (
                        description[: self.max_description_length].rstrip()
                        + "..."
                    )

                results.append(
                    {
                        "name": repo.full_name,
                        "description": description,
                        "stars": repo.stargazers_count,
                        "language": repo.language,
                        "url": repo.html_url,
                    }
                )

            return ToolResult(
                tool="github",
                success=True,
                data=results,
                error=None,
            )

        except GithubException as e:

            return ToolResult(
                tool="github",
                success=False,
                data=[],
                error=str(e),
            )

        except Exception as e:

            return ToolResult(
                tool="github",
                success=False,
                data=[],
                error=str(e),
            )