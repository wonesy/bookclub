from fastapi import APIRouter, Depends, HTTPException, status
from asyncpg.exceptions import UniqueViolationError

from bookclub.auth.dependencies import get_token_from_header
from bookclub.db import database
from bookclub.db.queries.clubs import GET_ALL_CLUBS, INSERT_CLUB
from bookclub.models.clubs import Club, NewClub
from bookclub.slugs.gen import gen_club_slug


router = APIRouter(
    prefix="/clubs",
    tags=["clubs"],
    dependencies=[Depends(get_token_from_header)]
)

@router.get("")
async def get_clubs():
    rows = await database.fetch_all(GET_ALL_CLUBS)
    return [Club(**row) for row in rows]


@router.post("")
async def create_club(club: NewClub):
    try:
        async with database.transaction():
            await database.execute(
                INSERT_CLUB,
                {
                    "name": club.name,
                    "slug": gen_club_slug(club)
                }
            )
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Club already exists with this name"
        )
