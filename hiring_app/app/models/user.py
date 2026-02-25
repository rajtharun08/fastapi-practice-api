from app.models.base import Base
from sqlalchemy import Column,Integer,Float,String,Enum
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"   
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String, unique=True, index=True)
    role=Column(String) 
    hashed_password=Column(String)
    applications=relationship("Application", back_populates="user")