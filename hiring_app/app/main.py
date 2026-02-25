from fastapi import FastAPI
from app.controllers import user_controller, job_controller, application_controller
from app.core.database import engine
from app.models.base import Base
from app.middleware.cors import cors_add
from app.exceptions import HiringAppException
from app.exceptions.exception_handlers import hiring_app_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hiring Application")

cors_add(app)
app.add_exception_handler(HiringAppException, hiring_app_exception_handler)

app.include_router(user_controller.router)
app.include_router(job_controller.router)
app.include_router(application_controller.router)