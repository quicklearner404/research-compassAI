from github import Github, GithubException, Auth

from backend.agent_tools.base_tool import BaseTool
from backend.models.tool_result import ToolResult
from config import GITHUB_TOKEN

class GitHubTool(BaseTool):
    """
    Tool for searching GitHub repositories.
    """

    def __init__(self, max_results: int = 3):
        from github import Github, Auth

        self.max_results = max_results

        if not GITHUB_TOKEN:
            self.github = Github()
            return

        auth = Auth.Token(GITHUB_TOKEN)
        self.github = Github(auth=auth)

    def run(self, query: str) -> ToolResult:

        if not query.strip():
            return ToolResult(
                tool="github",
                success=False,
                data=[],
                error="Query cannot be empty."
            )

        try:

            repositories = self.github.search_repositories(
                query=query,
                sort="stars",
                order="desc"
            )

            results = []

            for repo in repositories[:self.max_results]:

                results.append(
                    {
                        "name": repo.full_name,
                        "description": repo.description,
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