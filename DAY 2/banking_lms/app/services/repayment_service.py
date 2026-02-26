from app.models.repayment import Repayment

class RepaymentService:
    def __init__(self,repository):
        self.repository=repository

    def add_repayment(self,db,repayment_data):
        new_repayment=Repayment(
            loan_application_id=repayment_data.loan_application_id,
            amount_paid=repayment_data.amount_paid
        )
        return self.repository.create(db,new_repayment)

    def get_history(self,db,loan_id):
        return self.repository.get_by_loan_id(db,loan_id)