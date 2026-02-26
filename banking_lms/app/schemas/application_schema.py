from pydantic import BaseModel
from typing import Optional

class ApplicationBase(BaseModel):
    user_id:int
    product_id:int
    requested_amount:float

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdateStatus(BaseModel):
    status:str
    processed_by:int
    approved_amount:Optional[float]=None

class ApplicationResponse(ApplicationBase):
    id:int
    status:str
    approved_amount:Optional[float]=None
    processed_by:Optional[int]=None
    class Config:
        from_attributes=True