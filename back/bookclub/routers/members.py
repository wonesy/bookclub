import logging
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from asyncpg.exceptions import UniqueViolationError
from bookclub.db.queries.registration import DELETE_TOKEN, GET_REGISTRATION_TOKEN
from jose import jwt

from bookclub.auth.dependencies import decode_registration_token, get_token_from_header
from bookclub.auth.password import get_password_hash
from bookclub.models.auth import DecodedToken
from bookclub.models.clubs import Club
from bookclub.models.member import Member, NewMember
from bookclub.db import database
from bookclub.db.queries.members import GET_ALL_MEMBERS, GET_MEMBER_BY_USERNAME, INSERT_MEMBER, UPDATE_MEMBER
from bookclub.db.queries.clubs import GET_CLUBS_BY_USERNAME

logger = logging.getLogger("uvicorn.default")

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

    # validate registration token
    try:
        reg_token = decode_registration_token(new_member.registration_token)

        row = await database.fetch_one(GET_REGISTRATION_TOKEN, {"token": new_member.registration_token})
        if row is None:
           raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Registration token has already been used")

        expiration_date = datetime.utcfromtimestamp(reg_token.exp)
        logger.info(expiration_date)
        if datetime.now() >= expiration_date:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Registration token has expired")
    except jwt.JWTError as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid registration token")


    try:
        hashed_pw = get_password_hash(new_member.password)
        async with database.transaction():

            row = await database.fetch_one(INSERT_MEMBER, {
                "username": new_member.username,
                "password": str(hashed_pw),
                "first_name": new_member.first_name,
                "last_name": new_member.last_name,
                "email": new_member.email,
            })
            await database.execute(DELETE_TOKEN, {"token": new_member.registration_token})
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Member with username {new_member.username} already exists"
        )
    return Member(**row)


@router.get("/me")
async def get_me(token: DecodedToken = Depends(get_token_from_header)):
    member = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": token.sub})
    if member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member associated with token")

    rows = await database.fetch_all(GET_CLUBS_BY_USERNAME, {"username": token.sub})
    clubs = [Club(**row) for row in rows]

    return Member(clubs=clubs, **member)


@router.get("/{username}", response_model=Member)
async def get_member_by_username(username: str, _: DecodedToken = Depends(get_token_from_header)):
    member = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": username})
    if member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such member: {username}")
    rows = await database.fetch_all(GET_CLUBS_BY_USERNAME, {"username": username})
    clubs = [Club(**row) for row in rows]

    return Member(clubs=clubs, **member)


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
