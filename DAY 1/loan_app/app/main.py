from fastapi import FastAPI
from app.controllers import loan_controller
from app.middleware.cors import add_cors_middleware

app=FastAPI(title="loan application system")
add_cors_middleware(app)
app.include_router(loan_controller.router)

@app.get("/")
def root():
    return {"message": "Loan Application API is running"}