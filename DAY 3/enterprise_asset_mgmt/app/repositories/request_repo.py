from sqlalchemy.orm import Session
from app.models.asset_request import AssetRequest, RequestStatus

def create_request(db: Session, request_data: dict):
    db_request = AssetRequest(**request_data)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request 

def get_request_by_id(db: Session, request_id: int):
    return db.query(AssetRequest).filter(AssetRequest.id == request_id).first() 

def update_request_status(db: Session, request_id: int, status: RequestStatus, approved_by: int):
    request = db.query(AssetRequest).filter(AssetRequest.id == request_id).first()
    if request:
        request.status = status
        request.approved_by = approved_by
        db.commit()
    return request