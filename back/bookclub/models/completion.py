from datetime import datetime
from pydantic import BaseModel

from bookclub.models.book import Book
from bookclub.models.member import Member

class Completion(BaseModel):
    member: Member
    book: Book
    score: float
    completed_on: datetime
