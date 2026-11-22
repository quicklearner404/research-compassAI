from backend.models.utils import utcnow
from sqlalchemy.orm import Session

from backend.models.session import Session as ResearchSession


class SessionRepository:

    def get_all(
        self,
        db: Session,
    ):
        return (
            db.query(ResearchSession)
            .order_by(ResearchSession.updated_at.desc())
            .all()
        )

    def get(
        self,
        db: Session,
        session_id: int,
    ):
        return (
            db.query(ResearchSession)
            .filter(ResearchSession.id == session_id)
            .first()
        )

    def create(
        self,
        db: Session,
        title: str,
    ):
        session = ResearchSession(
            title=title,
        )

        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    def touch(
        self,
        db: Session,
        session: ResearchSession,
    ):
        session.updated_at = utcnow()

        db.commit()

        db.refresh(session)

    def update_title(
        self,
        db: Session,
        session: ResearchSession,
        title: str,
    ):
        session.title = title
        db.add(session)
        db.commit()
        db.refresh(session)

        return session