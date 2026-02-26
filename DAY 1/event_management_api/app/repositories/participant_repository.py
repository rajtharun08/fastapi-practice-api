from app.core.db import participants_db

class ParticipantRepository:
    def __init__(self):
        self._db = participants_db
        if not self._db:
            self._db.append({"id": 1, "name": "Bhuvaneswari", "email": "bhuvi@email.com", "event_id": 1})

    def get_all(self):
        return self._db

    def create(self, participant_data):
        part_dict = participant_data.model_dump() if hasattr(participant_data, "model_dump") else participant_data.dict()
        part_dict["id"] = len(self._db) + 1
        self._db.append(part_dict)
        return part_dict

    def get_by_email(self, email: str):
        for p in self._db:
            if p["email"] == email:
                return p
        return None

    def get_count_by_event(self, event_id: int):
        return len([p for p in self._db if p["event_id"] == event_id])