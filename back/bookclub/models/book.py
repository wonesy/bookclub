from typing import Optional
from pydantic import BaseModel

from bookclub.models.genre import Genre

class Book(BaseModel):
    title: str
    author: str
    genre: str
    slug: str

class NewBook(BaseModel):
    title: str
    author: str
    genre: str


class BookChoice(BaseModel):
    title: str
    author: str
    genre: str
    slug: str
    #
    username: str
    #
    month: int
    year: int
