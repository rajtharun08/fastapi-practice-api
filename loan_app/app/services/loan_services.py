from fastapi import HTTPException
from app.models.loan_model import LoanApplication

class LoanService:
    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def apply_for_loan(self, loan_data):
        eligibility_limit = loan_data.income * 10 
        status = "PENDING"
        
        if loan_data.loan_amount > eligibility_limit:
            status = "REJECTED"

        new_loan = LoanApplication( 
            id=len(self.loan_repository.get_all()) + 1,
            applicant_name=loan_data.applicant_name,
            income=loan_data.income,
            loan_amount=loan_data.loan_amount,
            status=status
        )
        
        return self.loan_repository.create(new_loan)

    def get_all_applications(self):
        return self.loan_repository.get_all()

    def get_application_by_id(self, loan_id: int):
        loan = self.loan_repository.get_by_id(loan_id)
        if not loan:
            raise HTTPException(status_code=404, detail="Loan application not found") 
        return loan

    def approve_loan(self, loan_id: int):
        loan = self.get_application_by_id(loan_id)
        
        if loan.status != "PENDING": 
            raise HTTPException(status_code=400, detail="Only pending loans can be approved")
            
        if loan.loan_amount > (loan.income * 10): 
            raise HTTPException(status_code=400, detail="Loan amount exceeds eligibility limit")

        self.loan_repository.update_status(loan_id, "APPROVED")
        return {"message": "Loan approved successfully", "status": "APPROVED"} 

    def reject_loan(self, loan_id: int):
        loan = self.get_application_by_id(loan_id)
        
        if loan.status != "PENDING":
            raise HTTPException(status_code=400, detail="Only pending loans can be rejected")
            
        self.loan_repository.update_status(loan_id, "REJECTED") 
        return {"message": "Loan rejected", "status": "REJECTED"} 