from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.sessions import router as session_router
from backend.database import Base, engine

# Import models so SQLAlchemy registers them before create_all
from backend.models.session import Session  # noqa: F401
from backend.models.message import Message  # noqa: F401
from config import APP_NAME, CORS_ORIGINS, VERSION

app = FastAPI(
    title=f"{APP_NAME} API",
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": f"{APP_NAME} Backend Running"}
