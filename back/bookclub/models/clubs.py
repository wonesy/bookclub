from pydantic import BaseModel

class Club(BaseModel):
    id: int
    name: str
    slug: str

class NewClub(BaseModel):
    name: str
