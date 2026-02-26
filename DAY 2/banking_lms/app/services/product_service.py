from app.models.loan_product import LoanProduct

class ProductService:
    def __init__(self,repository):
        self.repository=repository

    def create_product(self,db,product_data):
        new_product=LoanProduct(
            product_name=product_data.product_name,
            interest_rate=product_data.interest_rate,
            max_amount=product_data.max_amount,
            tenure_months=product_data.tenure_months,
            description=product_data.description
        )
        return self.repository.create(db,new_product)

    def list_products(self,db,skip,limit):
        return self.repository.get_all(db,skip,limit)