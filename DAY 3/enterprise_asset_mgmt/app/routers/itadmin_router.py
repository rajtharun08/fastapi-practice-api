from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import itadmin_controller

router = APIRouter(prefix="/itadmin", tags=["IT Admin"])

@router.post("/assets")
def create_asset(asset_data: dict, db: Session = Depends(get_db), current_user = Depends(require_roles("IT Admin", "SuperAdmin"))):
    return itadmin_controller.add_asset(db, asset_data)

@router.get("/assets")
def list_assets(skip: int = 0, limit: int = 20, status: str = None, db: Session = Depends(get_db), current_user = Depends(require_roles("IT Admin", "SuperAdmin"))):
    return itadmin_controller.list_assets(db, skip, limit, status)

@router.post("/requests/{request_id}/approve")
def approve_request(request_id: int, asset_id: int, db: Session = Depends(get_db), current_user = Depends(require_roles("IT Admin", "SuperAdmin"))):
    return itadmin_controller.approve_request(db, request_id, asset_id, current_user.id)

@router.post("/return")
def return_asset(assignment_id: int, condition: str, db: Session = Depends(get_db), current_user = Depends(require_roles("IT Admin", "SuperAdmin"))):
    return itadmin_controller.return_asset(db, assignment_id, condition)