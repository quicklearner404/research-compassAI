from smolagents import OpenAIServerModel

from backend.providers.provider import LLMProvider
from config import GROQ_API_KEY, GROQ_MODEL


class GroqProvider(LLMProvider):
    """
    Groq implementation using the OpenAI-compatible API.
    """

    def get_model(self):
        return OpenAIServerModel(
            model_id=GROQ_MODEL,
            api_key=GROQ_API_KEY,
            api_base="https://api.groq.com/openai/v1",
        )