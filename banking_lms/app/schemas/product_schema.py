from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name:str
    interest_rate:float
    max_amount:float
    tenure_months:int
    description:str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id:int
    class Config:
        from_attributes=True