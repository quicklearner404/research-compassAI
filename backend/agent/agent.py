import logging
import re

from smolagents.memory import ActionStep
from smolagents.models import ChatMessage, MessageRole

from backend.agent.agent_factory import build_agent
from backend.agent.prompts import SYSTEM_PROMPT
from backend.providers.factory import get_provider
from backend.services.citations import check_citations, unverified_links_note
from backend.services.context import ConversationContext
from backend.services.prompt_service import PromptService
from config import USE_MOCK_LLM

logger = logging.getLogger(__name__)

TOOL_KEYWORDS = frozenset(
    {
        "paper", "papers", "research", "survey",
        "github", "repository", "repositories", "repo", "repos",
        "implementation", "implementations",
        "tutorial", "tutorials", "documentation", "docs",
        "latest", "recent", "find", "search",
        "resource", "resources",
    }
)


def normalize(text: str) -> str:
    """Lowercase and strip punctuation, keeping word tokens only."""
    return " ".join(re.findall(r"\w+", text.lower()))


def needs_tools(query: str) -> bool:
    """
    Route a query: True -> tool-calling agent, False -> direct LLM answer.

    Research/resource requests ("find papers on ...", "github repos for ...")
    need external tools; general knowledge questions do not.
    """
    return bool(set(normalize(query).split()) & TOOL_KEYWORDS)


def mock_response(query: str) -> str:
    return "\n".join(
        [
            "# Mock AI Response",
            "",
            "This is a simulated response from **Research Compass AI**.",
            "",
            "## User Query",
            "",
            f"> {query}",
        ]
    )


class ResearchAgent:
    """
    Main AI entry point.

    General questions       -> direct call to the configured LLM (fast path)
    Research/resource asks  -> smolagents ToolCallingAgent with arXiv/GitHub/web tools
    """

    def __init__(self):
        self.prompt_service = PromptService()
        self._model = None
        self._agent = None

    # Built lazily so importing the app (or running in mock mode)
    # never requires provider credentials.
    @property
    def model(self):
        if self._model is None:
            self._model = get_provider().get_model()
        return self._model

    @property
    def agent(self):
        if self._agent is None:
            self._agent = build_agent(self.model)
        return self._agent

    def run(self, context: ConversationContext | str) -> str:
        if isinstance(context, str):
            context = ConversationContext(history=[], current_query=context)

        if USE_MOCK_LLM:
            return mock_response(context.current_query)

        prompt = self.prompt_service.build(context)

        if not needs_tools(context.current_query):
            response = self.model.generate(
                [
                    ChatMessage(role=MessageRole.SYSTEM, content=SYSTEM_PROMPT),
                    ChatMessage(role=MessageRole.USER, content=prompt),
                ]
            )
            return response.content

        answer = str(self.agent.run(prompt))
        return self._verify_citations(answer)

    def _tool_observations(self) -> str:
        """Concatenated tool outputs from the agent's most recent run."""
        return "\n".join(
            step.observations
            for step in self.agent.memory.steps
            if isinstance(step, ActionStep) and step.observations
        )

    def _verify_citations(self, answer: str) -> str:
        """Flag links in the answer that no tool actually returned."""
        report = check_citations(answer, self._tool_observations())

        if report.is_grounded:
            return answer

        logger.warning(
            "Answer cited %d link(s) not returned by any tool: %s",
            len(report.ungrounded),
            report.ungrounded,
        )
        return answer + unverified_links_note(report)
