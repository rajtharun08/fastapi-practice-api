from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    role: str 

class UserCreate(UserBase):
    password: str 

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes=True  