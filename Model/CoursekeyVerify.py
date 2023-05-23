from pydantic import BaseModel
from typing import Union

class CoursekeyVerify(BaseModel):
    CourseKey: Union[str, None] = None
    StartTime: str
    EndTime: str
    Owner: str
