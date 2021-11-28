from fastapi import APIRouter, Depends, HTTPException, status
from asyncpg.exceptions import UniqueViolationError

from bookclub.auth.dependencies import get_token_from_header
from bookclub.db import database
from bookclub.db.queries import GET_ALL_BOOKS, GET_BOOK_BY_SLUG, INSERT_BOOK, INSERT_GENRE
from bookclub.models.book import Book, NewBook
from bookclub.slugs.gen import gen_book_slug

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(get_token_from_header)]
)

@router.get("")
async def get_books():
    rows = await database.fetch_all(GET_ALL_BOOKS)
    return [Book(**row) for row in rows]


@router.post("")
async def create_book(new_book: NewBook):
    try:
        async with database.transaction():
            await database.execute(
                INSERT_BOOK,
                {
                    "title": new_book.title,
                    "author": new_book.author,
                    "genre": new_book.genre.lower(),
                    "slug": gen_book_slug(new_book)
                }
            )
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Book already exists"
        )

@router.get("/{book_slug}", response_model=Book)
async def get_book(book_slug: str):
    row = await database.fetch_one(GET_BOOK_BY_SLUG, {"slug": book_slug})
    if row is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return Book(**row)


@router.get("/{book_slug}", response_model=Book)
async def update_book(book_slug: str, updated_book: NewBook):
    pass
