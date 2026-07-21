from typing import Any
from pydantic import BaseModel


class ToolResult(BaseModel):
    """
    Standard response object returned by every tool.
    """

    tool: str
    success: bool
    data: Any = None
    error: str | None = None