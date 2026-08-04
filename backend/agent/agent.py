import re

from backend.providers.factory import get_provider
from backend.agent.agent_factory import build_agent
from backend.services.context import ConversationContext
from backend.services.prompt_service import PromptService
from config import USE_MOCK_LLM


DIRECT_RESPONSE_KEYWORDS = {
    "hello",
    "hi",
    "hey",
    "thanks",
    "thank you",
    "good morning",
    "good evening",
    "good afternoon",
    "how are you",
    "what can you do",
    "who are you",
}

RESEARCH_KEYWORDS = [
    "paper",
    "papers",
    "research",
    "survey",
    "github",
    "repository",
    "repositories",
    "implementations",
    "documentation",
    "tutorial",
    "tutorials",
    "arxiv",
    "recent",
    "latest",
    "find",
    "search",
]


def should_use_direct_response(query: str) -> bool:
    if not query:
        return True

    normalized = re.sub(r"[^a-z0-9]+", " ", query.lower()).strip()
    if not normalized:
        return True

    if normalized in DIRECT_RESPONSE_KEYWORDS:
        return True

    if any(keyword in normalized for keyword in RESEARCH_KEYWORDS):
        return False

    words = normalized.split()
    if len(words) <= 4:
        return True

    return False


class ResearchAgent:
    """
    Main AI agent responsible for deciding which tools to use.
    """

    def __init__(self):
        provider = get_provider()

        self.model = provider.get_model()
        self.agent = build_agent(self.model)

        self.prompt_service = PromptService()

    def run(self, context: ConversationContext):

        if should_use_direct_response(context.current_query):
            return (
                "Hello! I can help with AI research summaries, paper recommendations, "
                "and GitHub resource suggestions. Ask me for a paper, repo, or explanation "
                "and I’ll respond quickly."
            )

        if USE_MOCK_LLM:
            lines = [
                "# Mock AI Response",
                "",
                "This is a simulated response from **Research Compass AI**.",
                "",
                "---",
                "",
                "## User Query",
                "",
                f"> {context.current_query}",
                "",
                "---",
                "",
                "## Explanation",
                "",
                "This is a fake response used during development so no LLM tokens are consumed.",
                "",
                "### Key Points",
                "",
                "- Backend is working ✅",
                "- Database is working ✅",
                "- API is working ✅",
                "- Frontend rendering is working ✅",
                "- Markdown rendering can be tested ✅",
                "",
                "### Example Code",
                "",
                "```python",
                "def vision_transformer():",
                '    return "ViT splits images into patches."',
                "```",
                "",
                "### Example Resources",
                "",
                "| Resource | Type |",
                "|----------|------|",
                "| Attention Is All You Need | Paper |",
                "| Vision Transformer | Paper |",
                "| Hugging Face Transformers | Documentation |",
                "",
                "### References",
                "",
                "- https://arxiv.org",
                "- https://github.com",
                "- https://huggingface.co",
                "",
                "End of mock response.",
            ]

            return "\n".join(lines)

        prompt = self.prompt_service.build(context)

        return self.agent.run(prompt)