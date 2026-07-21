from smolagents import CodeAgent, InferenceClientModel

from agent.hf_tools import (
    ArxivSearchTool,
    GitHubSearchTool,
    DuckDuckGoSearchTool,
)
from config import MODEL_ID, HF_TOKEN


class ResearchAgent:
    """
    Main AI agent responsible for deciding which tools to use.
    """

    def __init__(self):

        self.model = InferenceClientModel(
            model_id=MODEL_ID,
            token=HF_TOKEN,
        )

        self.agent = CodeAgent(
            tools=[
                ArxivSearchTool(),
                GitHubSearchTool(),
                DuckDuckGoSearchTool(),
            ],
            model=self.model,
            add_base_tools=False,
        )

    def run(self, query: str):
        return self.agent.run(query)