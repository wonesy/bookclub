from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Member(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    created_on: datetime
    last_login: Optional[datetime]
