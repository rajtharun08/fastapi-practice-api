from pydantic import BaseModel, Field

class EventCreate(BaseModel):
    name: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    capacity: int = Field(..., gt=0)

class EventResponse(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    capacity: int = Field(..., gt=0)