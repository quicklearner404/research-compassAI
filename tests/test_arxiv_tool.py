from agent_tools.arxiv_tool import ArxivTool


def test_arxiv_returns_success():

    tool = ArxivTool(max_results=2)

    response = tool.run("Graph Neural Networks")

    assert response.success is True
    assert len(response.data) == 2