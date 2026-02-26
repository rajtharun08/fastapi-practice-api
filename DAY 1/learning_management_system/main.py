from fastapi import FastAPI
from app.controllers import student_controller,course_controller,enrollment_controller

app=FastAPI(title="learning management system")
app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)

@app.get("/")
def home():
    return {"message":"helloworld"}