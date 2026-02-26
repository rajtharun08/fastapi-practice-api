from fastapi import HTTPException
from app.models.loan_application import LoanApplication

class ApplicationService:
    def __init__(self,repo,product_repo):
        self.repo=repo
        self.product_repo=product_repo

    def apply(self,db,data):
        new_app=LoanApplication(
            user_id=data.user_id,
            product_id=data.product_id,
            requested_amount=data.requested_amount,
            status="pending"
        )
        return self.repo.create(db,new_app)

    def update_status(self,db,app_id,data):
        application=self.repo.get_by_id(db,app_id)
        if not application:
            raise HTTPException(status_code=404,detail="Application not found")
        
        product=self.product_repo.get_by_id(db,application.product_id)
        if data.status=="approved":
            if application.requested_amount>product.max_amount:
                raise HTTPException(status_code=400,detail="Amount exceeds product limit") 
        
        update_data=data.model_dump(exclude_unset=True)
        return self.repo.update(db,application,update_data)

    def list_applications(self,db,skip,limit):
        return self.repo.get_all(db,skip,limit)