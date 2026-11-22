from backend.services.context import ConversationContext


class PromptService:
    """
    Converts structured conversation context into the user prompt sent to
    the LLM. The system prompt is passed separately by the agent.
    """

    def build(self, context: ConversationContext) -> str:

        parts = ["## Conversation History"]

        if context.history:
            for message in context.history:
                role = "User" if message.role == "user" else "Assistant"
                parts.append(f"{role}:")
                parts.append(message.content)
                parts.append("")
        else:
            parts.append("No previous conversation.")
            parts.append("")

        parts.append("## Current User Question")
        parts.append(context.current_query)

        return "\n".join(parts)
