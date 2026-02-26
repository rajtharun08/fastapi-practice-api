from sqlalchemy.orm import Session
from app.models.loan_application import LoanApplication

class ApplicationRepository:
    def create(self,db:Session,application:LoanApplication):
        db.add(application)
        db.commit()
        db.refresh(application)
        return application

    def get_by_id(self,db:Session,application_id:int):
        return db.query(LoanApplication).filter(LoanApplication.id==application_id).first()

    def get_all(self,db:Session,skip:int=0,limit:int=10):
        return db.query(LoanApplication).offset(skip).limit(limit).all()

    def update(self,db:Session,db_obj:LoanApplication,obj_in:dict):
        for field in obj_in:
            setattr(db_obj,field,obj_in[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj