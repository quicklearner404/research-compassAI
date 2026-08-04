from backend.agent.prompts import SYSTEM_PROMPT
from backend.services.context import ConversationContext


class PromptService:
    """
    Responsible for converting structured conversation
    context into the final prompt sent to the LLM.
    """

    def build(self, context: ConversationContext) -> str:

        parts = [
            SYSTEM_PROMPT.strip(),
            "",
            "## Conversation History",
        ]

        if context.history:
            for message in context.history:

                role = (
                    "User"
                    if message.role == "user"
                    else "Assistant"
                )

                parts.append(f"{role}:")
                parts.append(message.content)
                parts.append("")

        else:
            parts.append("No previous conversation.")
            parts.append("")

        parts.append("## Current User Question")
        parts.append(context.current_query)

        return "\n".join(parts)