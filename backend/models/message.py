from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("sessions.id"),
        nullable=False
    )

    role = Column(String, nullable=False)

    content = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    session = relationship(
    "Session",
    back_populates="messages"
)