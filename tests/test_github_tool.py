from agent_tools.github_tool import GitHubTool


def test_valid_search():

    tool = GitHubTool(max_results=2)

    response = tool.run("Graph Neural Networks")

    assert response.success is True
    assert len(response.data) <= 2


def test_empty_query():

    tool = GitHubTool()

    response = tool.run("")

    assert response.success is False
    assert response.error == "Query cannot be empty."