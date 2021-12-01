from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from asyncpg.exceptions import UniqueViolationError
from bookclub.auth.dependencies import get_token_from_header

from bookclub.auth.password import get_password_hash
from bookclub.models.auth import DecodedToken
from bookclub.models.member import Member, NewMember
from bookclub.db import database
from bookclub.db.queries import GET_ALL_MEMBERS, GET_MEMBER_BY_USERNAME, INSERT_MEMBER, UPDATE_MEMBER

reserved_usernames = ['admin', 'me']

router = APIRouter(
    prefix="/members",
    tags=["members"],
)

@router.get("")
async def get_members(response_model=List[Member], _: DecodedToken = Depends(get_token_from_header)):
    """Get a list of all members"""
    rows = await database.fetch_all(GET_ALL_MEMBERS)
    return [Member(**row) for row in rows]


@router.post("", response_model=Member)
async def create_member(new_member: NewMember):
    if new_member.username in reserved_usernames:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Username is reserved")

    hashed_pw = get_password_hash(new_member.password)
    try:
        async with database.transaction():
            row = await database.fetch_one(INSERT_MEMBER, {
                "username": new_member.username,
                "password": str(hashed_pw),
                "first_name": new_member.first_name,
                "last_name": new_member.last_name,
                "email": new_member.email,
            })
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Member with username {new_member.username} already exists"
        )
    return Member(**row)

@router.get("/me")
async def get_me(token: DecodedToken = Depends(get_token_from_header)):
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": token.sub})
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member: {username}")
    return Member(**row)

@router.get("/{username}", response_model=Member)
async def get_member_by_username(username: str, _: DecodedToken = Depends(get_token_from_header)):
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": username})
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member: {username}")
    return Member(**row)

@router.put("/{username}", response_model=Member)
async def update_member_by_username(
    username: str,
    updated_member_info: Member,
    token: DecodedToken = Depends(get_token_from_header)
):
    if token.sub != username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Member can only update their own information")
    try:
        async with database.transaction():
            row = await database.fetch_one(UPDATE_MEMBER, {
                "new_username": updated_member_info.username,
                "old_username": username,
                "first_name": updated_member_info.first_name,
                "last_name": updated_member_info.last_name,
                "email": updated_member_info.email
            })

            if row is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member: {username}")

    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Member with username {updated_member_info.username} already exists"
        )

    return Member(**row)
