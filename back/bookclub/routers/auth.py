from fastapi import APIRouter, HTTPException, status, Depends
from asyncpg.exceptions import ForeignKeyViolationError, NotNullViolationError

from bookclub.auth.dependencies import get_token_from_header
from bookclub.auth.password import verify_password
from bookclub.auth.token import create_registration_token, create_tokens
from bookclub.db import database
from bookclub.db.queries.members import GET_MEMBER_BY_USERNAME
from bookclub.db.queries.registration import INSERT_REGISTRATION_TOKEN
from bookclub.models.auth import DecodedToken, LoginDetails, TokenPair
from bookclub.models.invitation import Invitation, InvitationResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=TokenPair)
async def login(login_details: LoginDetails):
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": login_details.username})
    if row is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")

    try:
        if not verify_password(plain_password=login_details.password, hashed_password=row.get("password")):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")
    except (ValueError, TypeError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")

    tokens = create_tokens({
        "sub": login_details.username,
    })

    return tokens.dict()


@router.post("/invite", response_model=InvitationResponse)
async def create_invite_token(invitation: Invitation, token: DecodedToken = Depends(get_token_from_header)):
    username = token.sub
    d = invitation.dict()
    d.update({"sub": username})
    reg_token = create_registration_token(d)

    print(d)

    try:
        async with database.transaction():
            await database.fetch_one(INSERT_REGISTRATION_TOKEN, {
                "token": reg_token,
                "username": username
            })
    except (NotNullViolationError, ForeignKeyViolationError):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong with the request")

    return InvitationResponse(club=invitation.club, token=reg_token)


# TODO
@router.get("/logout")
async def logout():
    pass


# TODO
@router.get("/refresh")
async def refresh_tokens():
    pass
