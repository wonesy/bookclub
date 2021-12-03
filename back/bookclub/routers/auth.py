from fastapi import APIRouter, HTTPException, status
from bookclub.auth.password import verify_password
from bookclub.auth.token import create_tokens
from bookclub.db import database
from bookclub.db.queries import GET_MEMBER_BY_USERNAME
from bookclub.models.auth import LoginDetails, TokenPair

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

@router.post("/invite")


# TODO
@router.get("/logout")
async def logout():
    pass


# TODO
@router.get("/refresh")
async def refresh_tokens():
    pass
