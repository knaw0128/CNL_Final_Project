from pydantic import BaseModel

class StudentCheckin(BaseModel):
    Coursekey: str
    StudentId: str
    CheckinTime: str

