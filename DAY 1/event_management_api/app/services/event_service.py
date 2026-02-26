from fastapi import HTTPException

class EventService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def create_event(self, event_data):
        all_events = self.event_repository.get_all()
        if any(e["name"].lower() == event_data.name.lower() for e in all_events):
            raise HTTPException(status_code=400, detail="Event name already exists")
        return self.event_repository.create(event_data)

    def get_all_events(self):
        return self.event_repository.get_all()

    def get_event_by_id(self, event_id: int):
        event = self.event_repository.get_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    def filter_events(self, location: str):
        return self.event_repository.filter_by_location(location)