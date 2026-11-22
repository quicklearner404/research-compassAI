from types import SimpleNamespace

import pytest

from backend.agent import agent as agent_module
from backend.agent.agent import ResearchAgent
from backend.services.context import ConversationContext


class FakeModel:
    def __init__(self):
        self.calls = []

    def generate(self, messages):
        self.calls.append(messages)
        return SimpleNamespace(content="direct answer")


class FakeToolAgent:
    def __init__(self):
        self.prompts = []

    def run(self, prompt):
        self.prompts.append(prompt)
        return "agent answer"


@pytest.fixture
def live_agent(monkeypatch):
    """A ResearchAgent with mock mode off and fake model/tool-agent injected."""
    monkeypatch.setattr(agent_module, "USE_MOCK_LLM", False)
    agent = ResearchAgent()
    agent._model = FakeModel()
    agent._agent = FakeToolAgent()
    return agent


def test_mock_mode_returns_canned_response_without_llm(monkeypatch):
    monkeypatch.setattr(agent_module, "USE_MOCK_LLM", True)
    agent = ResearchAgent()

    answer = agent.run("hello")

    assert "Mock AI Response" in answer
    assert "> hello" in answer
    assert agent._model is None  # provider never constructed


def test_general_question_goes_to_direct_llm(live_agent):
    answer = live_agent.run("What is backpropagation?")

    assert answer == "direct answer"
    assert live_agent._agent.prompts == []

    system, user = live_agent._model.calls[0]
    assert system.role == "system"
    assert user.role == "user"
    assert "What is backpropagation?" in user.content


def test_research_request_goes_to_tool_agent(live_agent):
    answer = live_agent.run("find recent papers on diffusion models")

    assert answer == "agent answer"
    assert live_agent._model.calls == []
    assert "find recent papers on diffusion models" in live_agent._agent.prompts[0]


def test_accepts_conversation_context(live_agent):
    context = ConversationContext(history=[], current_query="Explain dropout")

    assert live_agent.run(context) == "direct answer"
