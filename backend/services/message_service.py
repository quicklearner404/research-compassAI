from sqlalchemy.orm import Session

from backend.repositories.message_repository import MessageRepository
from backend.repositories.session_repository import SessionRepository


class MessageService:

    def __init__(self):
        self.messages = MessageRepository()
        self.sessions = SessionRepository()

    def create(
        self,
        db: Session,
        session_id: int,
        role: str,
        content: str,
    ):

        session = self.sessions.get(
            db=db,
            session_id=session_id,
        )

        if session is None:
            raise ValueError("Session not found")

        return self.messages.create(
            db=db,
            session_id=session_id,
            role=role,
            content=content,
        )

    def get_by_session(
        self,
        db: Session,
        session_id: int,
    ):

        session = self.sessions.get(
            db=db,
            session_id=session_id,
        )

        if session is None:
            raise ValueError("Session not found")

        return self.messages.get_by_session(
            db=db,
            session_id=session_id,
        )