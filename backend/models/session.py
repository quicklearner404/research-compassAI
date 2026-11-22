from sqlalchemy import Column, Integer, String, DateTime
from backend.models.utils import utcnow
from sqlalchemy.orm import relationship
from backend.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    created_at = Column(DateTime, default=utcnow)

    updated_at = Column(
        DateTime,
        default=utcnow,
        onupdate=utcnow
    )
    messages = relationship(
    "Message",
    back_populates="session",
    cascade="all, delete-orphan"
)