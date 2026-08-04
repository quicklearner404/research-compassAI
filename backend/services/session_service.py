from sqlalchemy.orm import Session

from backend.models.session import Session as ResearchSession
from backend.repositories.session_repository import SessionRepository


class SessionService:

    def __init__(self):
        self.repository = SessionRepository()

    def get_all(
        self,
        db: Session,
    ):
        return self.repository.get_all(db)

    def get(
        self,
        db: Session,
        session_id: int,
    ):
        return self.repository.get(
            db,
            session_id,
        )

    def create(
        self,
        db: Session,
        title: str,
    ):
        return self.repository.create(
            db=db,
            title=title,
        )

    def touch(
        self,
        db: Session,
        session: ResearchSession,
    ):
        self.repository.touch(
            db=db,
            session=session,
        )

    def update_title(
        self,
        db: Session,
        session: ResearchSession,
        title: str,
    ):
        return self.repository.update_title(
            db=db,
            session=session,
            title=title,
        )