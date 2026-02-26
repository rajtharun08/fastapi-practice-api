from sqlalchemy.orm import Session
from app.models.loan_product import LoanProduct

class ProductRepository:
    def create(self,db:Session,product:LoanProduct):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get_all(self,db:Session,skip:int=0,limit:int=10):
        return db.query(LoanProduct).offset(skip).limit(limit).all()

    def get_by_id(self,db:Session,product_id:int):
        return db.query(LoanProduct).filter(LoanProduct.id==product_id).first()