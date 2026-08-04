from backend.providers.huggingface_provider import HuggingFaceProvider
from backend.providers.groq_provider import GroqProvider
from backend.providers.ollama_provider import OllamaProvider

from config import LLM_PROVIDER


def get_provider():
    """
    Returns the configured LLM provider.
    """

    providers = {
        "huggingface": HuggingFaceProvider,
        "groq": GroqProvider,
        "ollama": OllamaProvider,
    }

    provider_class = providers.get(LLM_PROVIDER)

    if provider_class is None:
        raise ValueError(
            f"Unknown LLM provider: {LLM_PROVIDER}"
        )

    return provider_class()