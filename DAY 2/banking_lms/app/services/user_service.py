from app.models.user import User
from fastapi import HTTPException

class UserService:
    def __init__(self,repository):
        self.repository=repository

    def register_user(self,db,user_data):
        if self.repository.get_by_email(db,user_data.email):
            raise HTTPException(status_code=400,detail="Email already exists")
        new_user=User(
            name=user_data.name,
            email=user_data.email,
            role=user_data.role,
            hashed_password=user_data.password
        )
        return self.repository.create(db,new_user)

    def get_user(self,db,user_id):
        user=self.repository.get_by_id(db,user_id)
        if not user:
            raise HTTPException(status_code=404,detail="User not found")
        return user