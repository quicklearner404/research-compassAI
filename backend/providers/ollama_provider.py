from smolagents import LiteLLMModel

from backend.providers.provider import LLMProvider
from config import OLLAMA_MODEL


class OllamaProvider(LLMProvider):

    def get_model(self):
        return LiteLLMModel(
            model_id=f"ollama_chat/{OLLAMA_MODEL}",
            api_base="http://localhost:11434",
            api_key="ollama",
            num_ctx=8192,
        )