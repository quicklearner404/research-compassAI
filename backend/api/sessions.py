from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.session import SessionCreate, SessionResponse
from dependencies import get_db
from models.session import Session as ResearchSession

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"]
)


@router.get("/")
def get_sessions(db: Session = Depends(get_db)):
    sessions = db.query(ResearchSession).all()

    return sessions

@router.post("/", response_model=SessionResponse)
def create_session(
    session: SessionCreate,
    db: Session = Depends(get_db)
):

    new_session = ResearchSession(
        title=session.title
    )

    db.add(new_session)

    db.commit()

    db.refresh(new_session)

    return new_session