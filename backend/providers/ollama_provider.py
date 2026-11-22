from smolagents import LiteLLMModel

from backend.providers.provider import LLMProvider
from config import OLLAMA_BASE_URL, OLLAMA_MODEL


class OllamaProvider(LLMProvider):
    """
    Local Ollama implementation via LiteLLM.
    """

    def get_model(self):
        return LiteLLMModel(
            model_id=f"ollama_chat/{OLLAMA_MODEL}",
            api_base=OLLAMA_BASE_URL,
            api_key="ollama",
            num_ctx=8192,
        )
