from pydantic import BaseModel
from typing import Union

class CoursekeyVerify(BaseModel):
    Coursekey: str
    StartTime: Union[str, None] 
    EndTime: Union[str, None] 
    Owner: Union[str, None] 
    
