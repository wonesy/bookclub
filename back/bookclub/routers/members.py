from typing import List
from fastapi import APIRouter, HTTPException, status

from bookclub.models.member import Member
from bookclub.db import database
from bookclub.db.queries import GET_ALL_MEMBERS, GET_MEMBER_BY_USERNAME

router = APIRouter(
    prefix="/members",
    tags=["members"],
)

@router.get("")
async def get_members(response_model=List[Member]):
    members = []
    rows = await database.fetch_all(GET_ALL_MEMBERS)
    for row in rows:
        members.append(
            Member(**row)
        )
    return members

@router.get("/{username}", response_model=Member)
async def get_member_by_username(username: str):
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": username})
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member {username}")
    return Member(**row)
