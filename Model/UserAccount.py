from pydantic import BaseModel

class UserAccount(BaseModel):
    ID: str
    password: str
