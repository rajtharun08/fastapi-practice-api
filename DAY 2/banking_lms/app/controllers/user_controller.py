from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate,UserResponse
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router=APIRouter(prefix="/users",tags=["Users"])
repo=UserRepository()
service=UserService(repo)

@router.post("/",response_model=UserResponse)
def create(user:UserCreate,db:Session=Depends(get_db)):
    return service.register_user(db,user)

@router.get("/{user_id}",response_model=UserResponse)
def get_one(user_id:int,db:Session=Depends(get_db)):
    return service.get_user(db,user_id)