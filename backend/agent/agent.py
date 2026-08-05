import re

from openai import OpenAI

from backend.agent.agent_factory import build_agent
from backend.agent.prompts import SYSTEM_PROMPT
from backend.providers.factory import get_provider
from backend.services.context import ConversationContext
from backend.services.prompt_service import PromptService
from config import USE_MOCK_LLM


class ResearchAgent:
    """
    Main AI entry point.

    General questions:
        -> Direct LLM

    Research/resource questions:
        -> ToolCallingAgent
    """

    TOOL_KEYWORDS = {
        "paper",
        "papers",
        "research",
        "survey",
        "github",
        "repository",
        "repositories",
        "implementation",
        "implementations",
        "tutorial",
        "tutorials",
        "documentation",
        "docs",
        "latest",
        "recent",
        "find",
        "search",
        "resource",
        "resources",
    }

    def __init__(self):

        provider = get_provider()

        # Shared model for the agent
        self.model = provider.get_model()

        # Tool-calling agent
        self.agent = build_agent(self.model)

        self.prompt_service = PromptService()

        # Fast direct-chat client
        self.chat_client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",
        )

    def _normalize(self, text: str) -> str:
        return " ".join(
            re.findall(r"\w+", text.lower())
        )

    def _needs_tools(self, normalized_query: str) -> bool:
        words = set(normalized_query.split())
        return bool(words & self.TOOL_KEYWORDS)

    def run(self, context: ConversationContext):

        if USE_MOCK_LLM:
            return "\n".join(
                [
                    "# Mock AI Response",
                    "",
                    "This is a simulated response from **Research Compass AI**.",
                    "",
                    "## User Query",
                    "",
                    f"> {context.current_query}",
                    "",
                    "Backend working ✅",
                    "Database working ✅",
                    "API working ✅",
                    "Frontend working ✅",
                ]
            )

        prompt = self.prompt_service.build(context)

        normalized_query = self._normalize(
            context.current_query
        )

        # ---------------------------
        # Fast path
        # ---------------------------
        if not self._needs_tools(normalized_query):

            response = self.chat_client.chat.completions.create(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            return response.choices[0].message.content

        # ---------------------------
        # Agent path
        # ---------------------------
        return self.agent.run(prompt)