import datetime as dt
from typing import Dict
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime

from . import db


# any uniqueness for attributes?
class Job(db.Model):
    __tablename__ = 'jobs'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(), nullable=False)
    priority = Column(Integer, nullable=False)
    submitterId = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, name, priority, submitterId):
        self.name = name
        self.priority = priority
        self.submitterId = submitterId
        self.created_at = dt.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def serialize_post(self) -> Dict:
        return {
            "jobId": self.id
        }
    
    def serialize_get(self) -> Dict:
        return {
            "jobId": self.id,
            "name": self.name,
            "submitterId": self.submitterId,
            "priority": self.priority
        }
