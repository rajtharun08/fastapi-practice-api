from sqlalchemy.orm import Session
from app.repositories import department_repo, user_repo
from app.services import auth_service

def create_department(db: Session, name: str, manager_id: int = None):
    return department_repo.create_department(db, name, manager_id)

def create_user(db: Session, user_data: dict):
    user_data["password"] = auth_service.get_password_hash(user_data["password"])
    return user_repo.create_user(db, user_data)