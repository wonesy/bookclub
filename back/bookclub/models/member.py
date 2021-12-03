from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Member(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    created_on: Optional[datetime]
    last_login: Optional[datetime]


class NewMember(BaseModel):
    username: str
    password: str
    registration_token: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
