from fastapi import FastAPI
from app.controllers import event_controller, participant_controller

app = FastAPI(title="event management system")

app.include_router(event_controller.router)
app.include_router(participant_controller.router)

@app.get("/")
def home():
    return {"message": "welcome to the event management system API"}