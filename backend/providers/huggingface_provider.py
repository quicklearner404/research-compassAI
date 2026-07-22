from smolagents import InferenceClientModel

from backend.providers.provider import LLMProvider
from config import MODEL_ID, HF_TOKEN


class HuggingFaceProvider(LLMProvider):
    """
    Hugging Face implementation.
    """

    def get_model(self):
        return InferenceClientModel(
            model_id=MODEL_ID,
            token=HF_TOKEN,
        )