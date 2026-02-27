from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.base import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    manager_id = Column(Integer, nullable=True)

    users = relationship("User", back_populates="department")
    assets = relationship("Asset", back_populates="department")