from pydantic import BaseModel, ConfigDict


class SessionCreate(BaseModel):
    title: str


class SessionResponse(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)