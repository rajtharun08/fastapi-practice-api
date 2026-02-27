from pydantic import BaseModel
from datetime import date
from enum import Enum

class AssetStatus(str, Enum):
    AVAILABLE = "AVAILABLE" 
    ASSIGNED = "ASSIGNED" 
    MAINTENANCE = "MAINTENANCE" 
    RETIRED = "RETIRED" 

class AssetBase(BaseModel):
    asset_tag: str 
    asset_type: str 
    brand: str
    model: str 
    purchase_date: date 
    department_id: int 

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int 
    status: AssetStatus 
    class Config:
        from_attributes = True