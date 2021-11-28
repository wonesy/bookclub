from typing import Union
import random
from bookclub.models.book import Book, NewBook

def isvalidchar(c: str) -> bool:
    return c.isalnum() or c in ['_', '-']

def gen_book_slug(book: Union[Book,NewBook]) -> str:
    r = random.randint(0, 9999)
    readable = f"{book.author.lower().replace(' ', '-')}-{book.title.lower().replace(' ', '-')}"
    filtered_readable = ''.join(filter(isvalidchar, readable))
    return f"{r:04d}-{filtered_readable}"
