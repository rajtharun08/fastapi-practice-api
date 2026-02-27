from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import employee_controller

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/request-asset")
def request_asset(asset_type: str, reason: str, db: Session = Depends(get_db), current_user = Depends(require_roles("Employee"))):
    return employee_controller.request_asset(db, current_user.id, asset_type, reason)

@router.get("/my-assets")
def view_own_assets(db: Session = Depends(get_db), current_user = Depends(require_roles("Employee"))):
    return employee_controller.get_my_assets(db, current_user.id)