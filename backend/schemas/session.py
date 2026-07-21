from pydantic import BaseModel


class SessionCreate(BaseModel):
    title: str


class SessionResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True