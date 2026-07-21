from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.session import SessionCreate, SessionResponse
from dependencies import get_db
from models.session import Session as ResearchSession
from fastapi import HTTPException
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
@router.get("/{session_id}", response_model=SessionResponse)
def get_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    session = (
        db.query(ResearchSession)
        .filter(ResearchSession.id == session_id)
        .first()
    )

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return session