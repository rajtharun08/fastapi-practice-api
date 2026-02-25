from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate):
        db_user = User(
            name=user.name,
            email=user.email,
            role=user.role,
            hashed_password=user.password 
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()