from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def create(self,db:Session,user:User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_id(self,db:Session,user_id:int):
        return db.query(User).filter(User.id==user_id).first()

    def get_by_email(self,db:Session,email:str):
        return db.query(User).filter(User.email==email).first()

    def get_all(self,db:Session,skip:int=0,limit:int=10):
        return db.query(User).offset(skip).limit(limit).all()