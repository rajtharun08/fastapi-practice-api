from pydantic import BaseModel
from datetime import datetime

class RepaymentBase(BaseModel):
    loan_application_id:int
    amount_paid:float

class RepaymentCreate(RepaymentBase):
    pass

class RepaymentResponse(RepaymentBase):
    id:int
    payment_date:datetime
    payment_status:str
    class Config:
        from_attributes=True