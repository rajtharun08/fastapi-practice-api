from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import manager_controller

router = APIRouter(prefix="/manager", tags=["Manager"])

@router.get("/team-assets")
def view_team_assets(db: Session = Depends(get_db), current_user = Depends(require_roles("Manager"))):
    return manager_controller.get_team_assets(db, current_user.id)