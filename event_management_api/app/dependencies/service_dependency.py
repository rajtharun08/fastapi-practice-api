from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.services.event_service import EventService
from app.services.participants_service import ParticipantService

event_repository=EventRepository()
participant_repository=ParticipantRepository()

event_service=EventService(event_repository)
participant_service=ParticipantService(participant_repository,event_repository)

def get_event_service():
    return event_service

def get_participant_service():
    return participant_service

