from pydantic import BaseModel
from typing import Union

class UserAccount(BaseModel):
    ID: Union[str, None] = None
    password: str
