from dataclasses import dataclass


@dataclass
class ConversationMessage:
    role: str
    content: str


@dataclass
class ConversationContext:
    history: list[ConversationMessage]
    current_query: str