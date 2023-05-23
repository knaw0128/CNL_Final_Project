from pydantic import BaseModel
from typing import Union

class StudentCheckin(BaseModel):
    CourseKey: Union[str, None] = None
    StudentId: Union[str, None] = None
    CheckinTime: str
