from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.sessions import router as session_router
from database import Base, engine

# Import models so SQLAlchemy knows about them
from models.session import Session
from models.message import Message

app = FastAPI(
    title="Research Compass AI API",
    version="1.0.0"
)

# Allow the React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router)

# Create all tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Research Compass AI Backend Running"
    }