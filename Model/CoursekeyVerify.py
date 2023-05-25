from typing import Optional
from pydantic import BaseModel


class CoursekeyVerify(BaseModel):
    Coursekey: str
    StartTime: Optional[str]
    EndTime: Optional[str]
    Owner: str
