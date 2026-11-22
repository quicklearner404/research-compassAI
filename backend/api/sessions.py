import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.dependencies import get_db

from backend.schemas.session import SessionCreate, SessionResponse
from backend.schemas.message import MessageCreate, MessageResponse
from backend.schemas.chat import ChatRequest, ChatResponse

from backend.services.session_service import SessionService
from backend.services.message_service import MessageService
from backend.services.chat_service import ChatService


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"],
)

session_service = SessionService()
message_service = MessageService()
chat_service = ChatService()


@router.get("/")
def get_sessions(
    db: Session = Depends(get_db),
):
    return session_service.get_all(db)


@router.post(
    "/",
    response_model=SessionResponse,
)
def create_session(
    session: SessionCreate,
    db: Session = Depends(get_db),
):
    return session_service.create(
        db=db,
        title=session.title,
    )


@router.get(
    "/{session_id}",
    response_model=SessionResponse,
)
def get_session(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = session_service.get(
        db=db,
        session_id=session_id,
    )

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    return session


@router.post(
    "/{session_id}/messages",
    response_model=MessageResponse,
)
def create_message(
    session_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
):
    try:
        return message_service.create(
            db=db,
            session_id=session_id,
            role=message.role,
            content=message.content,
        )

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )


@router.get(
    "/{session_id}/messages",
    response_model=list[MessageResponse],
)
def get_messages(
    session_id: int,
    db: Session = Depends(get_db),
):
    try:
        return message_service.get_by_session(
            db=db,
            session_id=session_id,
        )

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )


@router.post(
    "/{session_id}/chat",
    response_model=ChatResponse,
)
def chat(
    session_id: int,
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    try:
        return chat_service.chat(
            session_id=session_id,
            query=request.query,
            db=db,
        )

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    except Exception:
        logger.exception("Chat request failed for session %s", session_id)

        raise HTTPException(
            status_code=500,
            detail="Failed to generate response.",
        )