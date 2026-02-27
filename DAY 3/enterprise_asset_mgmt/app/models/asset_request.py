from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database.base import Base
import enum

class RequestStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class AssetRequest(Base):
    __tablename__ = "asset_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    asset_type = Column(String(50))
    reason = Column(String(255))
    status = Column(Enum(RequestStatus), default=RequestStatus.PENDING)
    approved_by = Column(Integer, nullable=True)

    employee = relationship("User", back_populates="requests")