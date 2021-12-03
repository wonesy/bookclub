from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from bookclub.models.book import Book
from bookclub.models.member import Member

class Completion(BaseModel):
    member: Member
    score: float
    comment: Optional[str]
    completed_on: datetime
