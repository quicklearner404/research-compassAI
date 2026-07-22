from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas.session import SessionCreate, SessionResponse
from backend.schemas.message import MessageCreate, MessageResponse
from backend.schemas.chat import ChatRequest, ChatResponse

from backend.dependencies import get_db

from backend.models.session import Session as ResearchSession
from backend.models.message import Message

from backend.agent.agent_instance import research_agent
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

@router.post(
    "/{session_id}/chat",
    response_model=ChatResponse
)
def chat(
    session_id: int,
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    # 1. Check session exists
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

    # 2. Save user's message
    user_message = Message(
        session_id=session_id,
        role="user",
        content=request.query
    )

    db.add(user_message)
    db.commit()

    # 3. Run the AI agent
    try:
        result = research_agent.run(request.query)

        print("TYPE:", type(result))
        print("RAW:", repr(result))

        answer = str(result)
        print("STRING:", repr(answer))

    except Exception as e:
        print(f"Agent Error: {e}")

        answer = (
            "Sorry, I couldn't generate a response right now. "
            "Please try again later."
        )

    assistant_message = Message(
        session_id=session_id,
        role="assistant",
        content=answer
    )

    db.add(assistant_message)
    db.commit()

    return ChatResponse(response=answer)