from backend.models.message import Message
from backend.services.context import (
    ConversationContext,
    ConversationMessage,
)


class MemoryService:
    """
    Handles construction of conversation context.

    Future responsibilities:
    - Recent message window
    - Conversation summarization
    - Topic memory retrieval
    """

    def __init__(self, max_recent_messages: int = 2):
        self.max_recent_messages = max_recent_messages

    def build_context(
        self,
        messages: list[Message],
    ) -> ConversationContext:

        if not messages:
            return ConversationContext(
                history=[],
                current_query="",
            )

        # Keep only recent messages
        recent = messages[-self.max_recent_messages:]

        # Find the latest user message
        latest_user_index = None

        for i in range(len(recent) - 1, -1, -1):
            if recent[i].role == "user":
                latest_user_index = i
                break

        # No user message found
        if latest_user_index is None:
            return ConversationContext(
                history=[],
                current_query="",
            )

        current_query = recent[latest_user_index].content.strip()

        history = []

        for message in recent[:latest_user_index]:
            history.append(
                ConversationMessage(
                    role=message.role,
                    content=message.content.strip(),
                )
            )

        return ConversationContext(
            history=history,
            current_query=current_query,
        )