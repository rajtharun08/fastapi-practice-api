from sqlalchemy.orm import Session
from app.services import request_service
from app.models.asset_assignment import AssetAssignment

def request_asset(db: Session, employee_id: int, asset_type: str, reason: str):
    return request_service.submit_request(db, employee_id, asset_type, reason)

def get_my_assets(db: Session, employee_id: int):
    return db.query(AssetAssignment).filter(
        AssetAssignment.user_id == employee_id,
        AssetAssignment.returned_date == None
    ).all()