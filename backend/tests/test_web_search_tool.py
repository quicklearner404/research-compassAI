from agent_tools.web_search_tool import WebSearchTool


def test_valid_search():

    tool = WebSearchTool(max_results=2)

    response = tool.run("Large Language Models")

    assert response.success is True
    assert len(response.data) <= 2


def test_empty_query():

    tool = WebSearchTool()

    response = tool.run("")

    assert response.success is False
    assert response.error == "Query cannot be empty."