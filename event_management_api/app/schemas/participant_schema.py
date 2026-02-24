from pydantic import BaseModel, Field

class ParticipantCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    event_id: int = Field(..., gt=0)

class ParticipantResponse(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    event_id: int = Field(..., gt=0)