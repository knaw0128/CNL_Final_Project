import datetime
from pydantic import BaseModel

class StudentCheckin(BaseModel):
    Coursekey: str
    StudentId: str
    CheckinTime: datetime.datetime

