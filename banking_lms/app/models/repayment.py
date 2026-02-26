from sqlalchemy import Column,Integer,Float,DateTime,String,ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Repayment(Base):
    __tablename__="repayments"
    id=Column(Integer,primary_key=True,index=True)
    loan_application_id=Column(Integer,ForeignKey("loan_applications.id"))
    amount_paid=Column(Float)
    payment_date=Column(DateTime,default=func.now())
    payment_status=Column(String,default="completed")