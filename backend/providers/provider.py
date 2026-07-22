from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Base interface for all LLM providers.

    Every provider must return a model object
    compatible with SmolAgents.
    """

    @abstractmethod
    def get_model(self):
        """
        Return a configured model instance.
        """
        pass