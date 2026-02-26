from fastapi import FastAPI
from app.core.database import engine,Base
from app.controllers import user_controller,product_controller,application_controller

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Banking LMS")

app.include_router(user_controller.router)
app.include_router(product_controller.router)
app.include_router(application_controller.router)

@app.get("/")
def root():
    return {"message":"Banking Loan Management System is Online"}