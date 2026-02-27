from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(20))  # SuperAdmin, IT Admin, Manager, Employee
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="users")
    requests = relationship("AssetRequest", back_populates="employee")