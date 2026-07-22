from backend.providers.factory import get_provider
from backend.agent.agent_factory import build_agent
from config import USE_MOCK_LLM


class ResearchAgent:
    """
    Main AI agent responsible for deciding which tools to use.
    """

    def __init__(self):
        provider = get_provider()
        self.model = provider.get_model()
        self.agent = build_agent(self.model)

    def run(self, query: str):
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
                f"> {query}",
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

        return self.agent.run(query)