from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.models.base import Base

class Job(Base):
    __tablename__="jobs"

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    description=Column(String)
    salary=Column(Float)
    company_id=Column(Integer)

    applications=relationship("Application", back_populates="job")