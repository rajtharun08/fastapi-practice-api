from app.models.loan_model import LoanApplication
from app.core.db import loans_db

class LoanRepository:
    def __init__(self):
        self.db = loans_db

    def create(self, loan: LoanApplication):
        self.db.append(loan)
        return loan

    def get_by_id(self, loan_id: int):
        for loan in self.db:
            if loan.id == loan_id:
                return loan
        return None

    def get_all(self):
        return self.db

    def update_status(self, loan_id: int, new_status: str):
        loan = self.get_by_id(loan_id)
        if loan:
            loan.status = new_status
            return loan
        return None