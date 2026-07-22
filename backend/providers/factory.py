from backend.providers.huggingface_provider import HuggingFaceProvider
from config import LLM_PROVIDER
from backend.providers.groq_provider import GroqProvider
def get_provider():
    """
    Returns the configured LLM provider.
    """

    providers = {
        "huggingface": HuggingFaceProvider,
        "groq": GroqProvider,
    }

    provider_class = providers.get(LLM_PROVIDER)

    if provider_class is None:
        raise ValueError(
            f"Unknown LLM provider: {LLM_PROVIDER}"
        )

    return provider_class()