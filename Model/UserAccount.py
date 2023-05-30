from typing import Union
from pydantic import BaseModel

class UserAccount(BaseModel):
    ID: str
    password: Union[str, None]
