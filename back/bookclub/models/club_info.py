from typing import List
from pydantic import BaseModel

from bookclub.models.member import MemberConcise
from bookclub.models.book import BookChoice
from bookclub.models.clubs import Club

class ClubInfo(BaseModel):
    club: Club
    members: List[MemberConcise]
    books: List[BookChoice]
