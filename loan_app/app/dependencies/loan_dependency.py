from app.respositories.loan_repository import LoanRepository
from app.services.loan_services import LoanService

loan_repository=LoanRepository()
loan_service=LoanService(loan_repository)

def get_loan_service():
    return loan_service