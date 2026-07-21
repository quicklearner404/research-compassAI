from abc import ABC, abstractmethod

from models.tool_result import ToolResult


class BaseTool(ABC):
    """
    Base class for every agent tool.
    """

    @abstractmethod
    def run(self, query: str) -> ToolResult:
        """
        Execute the tool.

        Parameters
        ----------
        query : str
            User query.

        Returns
        -------
        ToolResult
        """
        pass