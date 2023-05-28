from typing import Optional
from pydantic import BaseModel

class UserAccount(BaseModel):
    ID: str
    Password: Optional[str]
