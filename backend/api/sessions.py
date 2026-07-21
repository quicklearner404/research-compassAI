from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.session import SessionCreate, SessionResponse
from dependencies import get_db
from models.session import Session as ResearchSession
from fastapi import HTTPException
from models.message import Message
from schemas.message import MessageCreate, MessageResponse
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
@router.post(
    "/{session_id}/messages",
    response_model=MessageResponse
)
def create_message(
    session_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db)
):
    # Make sure the session exists
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

    db_message = Message(
        session_id=session_id,
        role=message.role,
        content=message.content
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message
@router.get(
    "/{session_id}/messages",
    response_model=list[MessageResponse]
)
def get_messages(
    session_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Message)
        .filter(Message.session_id == session_id)
        .order_by(Message.created_at.asc())
        .all()
    )