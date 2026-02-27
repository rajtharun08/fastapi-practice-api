from fastapi import FastAPI
from app.routers import (
    auth_router, 
    superadmin_router, 
    itadmin_router, 
    manager_router, 
    employee_router
)
from app.database.session import engine
from app.database.base import Base
from app.middleware.logging import log_requests
from app.middleware.exception_handler import global_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise Asset Management System (EAMS)")

app.middleware("http")(log_requests)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(auth_router.router)
app.include_router(superadmin_router.router)
app.include_router(itadmin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)

@app.get("/")
def health_check():
    return {"status": "EAMS API is running"}