import datetime
from typing import Optional
from pydantic import BaseModel


class CoursekeyVerify(BaseModel):
    Coursekey: str
    StartTime: Optional[datetime.datetime]
    EndTime: Optional[datetime.datetime]
    Owner: str
