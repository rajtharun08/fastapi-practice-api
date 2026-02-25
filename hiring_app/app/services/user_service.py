from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from fastapi import HTTPException

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, user_data: UserCreate):
        if self.repository.get_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.repository.create(user_data)

    def get_user_profile(self, user_id: int):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user