from sqlalchemy.orm import Session
from app.repositories import request_repo, asset_repo
from app.services import assignment_service
from app.models.asset_request import RequestStatus

def submit_request(db: Session, employee_id: int, asset_type: str, reason: str):
    return request_repo.create_request(db, employee_id, asset_type, reason)

def approve_request(db: Session, request_id: int, asset_id: int, admin_id: int):
    asset = asset_repo.get_asset_by_id(db, asset_id)
    if not asset or asset.status != "AVAILABLE":
        return None
    
    request_repo.update_request_status(db, request_id, RequestStatus.APPROVED, admin_id)
    return assignment_service.assign_asset(db, asset_id, admin_id)