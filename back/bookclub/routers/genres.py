from fastapi import APIRouter, Depends, HTTPException, status
from asyncpg.exceptions import UniqueViolationError

from bookclub.auth.dependencies import get_token_from_header
from bookclub.db import database
from bookclub.db.queries import GET_ALL_GENRES, INSERT_GENRE
from bookclub.models.genre import Genre

router = APIRouter(
    prefix="/genres",
    tags=["genres"],
    dependencies=[Depends(get_token_from_header)]
)

@router.get("")
async def get_genres():
    rows = await database.fetch_all(GET_ALL_GENRES)
    return [Genre(**row) for row in rows]


@router.post("")
async def create_genre(new_genre: Genre):
    try:
        async with database.transaction():
            await database.execute(INSERT_GENRE, {"name": new_genre.name.lower()})
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Genre with name {new_genre.name} already exists"
        )
