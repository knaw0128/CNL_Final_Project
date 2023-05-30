from typing import Union
from pydantic import BaseModel

class StudentCheckIn(BaseModel):
    Coursekey: str
    StudentId: Union[str, None] 
    CheckinTime: Union[str, None] 
    Name: Union[str, None]

