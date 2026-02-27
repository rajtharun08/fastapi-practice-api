from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database.base import Base
import enum

class AssetStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    ASSIGNED = "ASSIGNED"
    MAINTENANCE = "MAINTENANCE"
    RETIRED = "RETIRED"

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_tag = Column(String(50), unique=True, index=True)
    asset_type = Column(String(50))
    brand = Column(String(50))
    model = Column(String(50))
    purchase_date = Column(Date)
    status = Column(Enum(AssetStatus), default=AssetStatus.AVAILABLE)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="assets")
    assignments = relationship("AssetAssignment", back_populates="asset")