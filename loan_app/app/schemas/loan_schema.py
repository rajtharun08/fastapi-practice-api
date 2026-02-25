from pydantic import BaseModel,field_validator,Field
from typing import Optional

class LoanCreate(BaseModel):
    applicant_name: str = Field(...,min_length=1)
    income : float = Field(...,ge=0)
    loan_amount : float=Field(... ,ge=0)
    
class LoanResponse(BaseModel):
    id: int
    applicant_name: str
    income: float
    loan_amount: float
    status: str 
    class Config:
        from_attributes = True
    
class LoanStatusUpdateResponse(BaseModel):
    message: str
    status: str