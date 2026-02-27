from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AssignmentBase(BaseModel):
    asset_id: int 
    user_id: int 
    assigned_date: datetime 

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentResponse(AssignmentBase):
    id: int 
    returned_date: Optional[datetime] = None 
    condition_on_return: Optional[str] = None 
    class Config:
        from_attributes = True