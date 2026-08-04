from sqlalchemy.orm import Session

from backend.schemas.chat import ChatResponse

from backend.agent.agent_instance import research_agent

from backend.services.memory import MemoryService
from backend.services.session_service import SessionService
from backend.services.message_service import MessageService


class ChatService:

    def __init__(self):
        self.memory = MemoryService()

        self.sessions = SessionService()
        self.messages = MessageService()

        self.agent = research_agent

    def chat(
        self,
        session_id: int,
        query: str,
        db: Session,
    ) -> ChatResponse:

        session = self.sessions.get(
            db=db,
            session_id=session_id,
        )

        if session is None:
            raise ValueError("Session not found")

        # Rename default sessions using the first user message
        if session.title in ["Untitled Research", "New Research"]:
            title = query.strip()

            if len(title) > 60:
                title = title[:60].rstrip() + "..."

            self.sessions.update_title(
                db=db,
                session=session,
                title=title,
            )

        # Save user's message
        self.messages.create(
            db=db,
            session_id=session_id,
            role="user",
            content=query,
        )

        # Load conversation history
        previous_messages = self.messages.get_by_session(
            db=db,
            session_id=session_id,
        )

        # Build prompt
        context = self.memory.build_context(
            previous_messages
        )

        # Run the agent
        answer = str(
            self.agent.run(context)
        )

        # Save assistant response
        self.messages.create(
            db=db,
            session_id=session_id,
            role="assistant",
            content=answer,
        )

        # Update last-opened timestamp
        self.sessions.touch(
            db=db,
            session=session,
        )

        return ChatResponse(
            response=answer
        )