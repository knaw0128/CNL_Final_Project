from typing import Optional
from pydantic import BaseModel

class UserAccount(BaseModel):
    ID: str
    password: Optional[str]
