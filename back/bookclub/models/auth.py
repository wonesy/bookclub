from pydantic import BaseModel

class LoginDetails(BaseModel):
    username: str
    password: str
