from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from bookclub.models.clubs import Club

class Member(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    created_on: Optional[datetime]
    last_login: Optional[datetime]
    clubs: List[Club]


class NewMember(BaseModel):
    username: str
    password: str
    registration_token: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]


class MemberConcise(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
