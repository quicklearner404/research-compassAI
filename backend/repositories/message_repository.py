from sqlalchemy.orm import Session

from backend.models.message import Message


class MessageRepository:

    def get(
        self,
        db: Session,
        message_id: int,
    ) -> Message | None:

        return (
            db.query(Message)
            .filter(Message.id == message_id)
            .first()
        )

    def get_by_session(
        self,
        db: Session,
        session_id: int,
    ) -> list[Message]:

        return (
            db.query(Message)
            .filter(Message.session_id == session_id)
            .order_by(Message.created_at.asc())
            .all()
        )

    def create(
        self,
        db: Session,
        session_id: int,
        role: str,
        content: str,
    ) -> Message:

        message = Message(
            session_id=session_id,
            role=role,
            content=content,
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message