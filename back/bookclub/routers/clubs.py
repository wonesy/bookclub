from fastapi import APIRouter, Depends, HTTPException, status
from asyncpg.exceptions import UniqueViolationError

from bookclub.auth.dependencies import get_token_from_header
from bookclub.db import database
from bookclub.db.queries.books import GET_BOOK_CHOICES_BY_CLUB_ID
from bookclub.db.queries.clubs import GET_ALL_CLUBS, GET_CLUB_BY_ID, GET_CLUB_MEMBERS_BY_CLUB_ID, INSERT_CLUB
from bookclub.models.book import BookChoice
from bookclub.models.clubs import Club, NewClub
from bookclub.models.club_info import ClubInfo
from bookclub.models.member import MemberConcise
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

@router.get("/{club_id}", response_model=ClubInfo)
async def get_club_by_(club_id: int):
    by_club_id = {"club_id": club_id}

    row = await database.fetch_one(GET_CLUB_BY_ID, by_club_id)
    club = Club(**row)

    rows = await database.fetch_all(GET_CLUB_MEMBERS_BY_CLUB_ID, by_club_id)
    club_members = [MemberConcise(**row) for row in rows]

    rows = await database.fetch_all(GET_BOOK_CHOICES_BY_CLUB_ID, by_club_id)
    book_choices = [BookChoice(**row) for row in rows]

    return ClubInfo(
        club=club,
        members=club_members,
        books=book_choices
    )
