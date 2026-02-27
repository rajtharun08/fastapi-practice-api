from pydantic import BaseModel
from enum import Enum
from typing import Optional

class RequestStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class RequestBase(BaseModel):
    asset_type: str
    reason: str

class RequestCreate(RequestBase):
    pass

class RequestResponse(RequestBase):
    id: int
    employee_id: int
    status: RequestStatus
    approved_by: Optional[int] = None
    class Config:
        from_attributes = True