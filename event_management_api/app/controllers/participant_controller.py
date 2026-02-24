from fastapi import APIRouter, Depends
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse
from app.dependencies.service_dependency import get_participant_service

router = APIRouter(prefix="/participants")

@router.post("/", response_model=ParticipantResponse)
def register_participant(participant_data: ParticipantCreate, service=Depends(get_participant_service)):
    return service.register_participant(participant_data)

@router.get("/{id}", response_model=ParticipantResponse)
def get_participant(id: int, service=Depends(get_participant_service)):
    return service.get_participant(id)