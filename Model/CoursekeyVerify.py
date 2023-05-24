from pydantic import BaseModel

class CoursekeyVerify(BaseModel):
    Coursekey: str
    StartTime: str
    EndTime: str
    Owner: str
