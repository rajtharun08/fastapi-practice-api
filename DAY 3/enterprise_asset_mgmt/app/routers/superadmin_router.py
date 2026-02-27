from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles
from app.controllers import superadmin_controller

router = APIRouter(prefix="/superadmin", tags=["SuperAdmin"])

@router.post("/departments")
def add_department(name: str, manager_id: int = None, db: Session = Depends(get_db), current_user = Depends(require_roles("SuperAdmin"))):
    return superadmin_controller.create_department(db, name, manager_id)

@router.post("/users")
def add_user(user_data: dict, db: Session = Depends(get_db), current_user = Depends(require_roles("SuperAdmin"))):
    return superadmin_controller.create_user(db, user_data)