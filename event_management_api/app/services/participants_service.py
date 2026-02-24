from fastapi import HTTPException

class ParticipantService:
    def __init__(self, participant_repository, event_repository):
        self.participant_repository = participant_repository
        self.event_repository = event_repository

    def register_participant(self, participant_data):
        event = self.event_repository.get_by_id(participant_data.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        
        if self.participant_repository.get_by_email(participant_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
            
        current_count = self.participant_repository.get_count_by_event(participant_data.event_id)
        if current_count >= event["capacity"]:
            raise HTTPException(status_code=400, detail="Event capacity exceeded")
            
        return self.participant_repository.create(participant_data)

    def get_participant(self, participant_id: int):
        for p in self.participant_repository.get_all():
            if p["id"] == participant_id:
                return p
        raise HTTPException(status_code=404, detail="Participant not found")