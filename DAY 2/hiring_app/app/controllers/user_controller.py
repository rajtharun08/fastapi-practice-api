from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_service(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.register_user(user_data)

@router.get("/{user_id}", response_model=UserResponse)
def get_profile(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user_profile(user_id)