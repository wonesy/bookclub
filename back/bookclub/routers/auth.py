from fastapi import APIRouter, HTTPException, status
from bookclub.auth.password import get_password_hash, verify_password
from bookclub.db import database
from bookclub.db.queries import GET_MEMBER_BY_USERNAME
from bookclub.models.auth import LoginDetails
from bookclub.routers.members import get_member_by_username

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(login_details: LoginDetails):
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": login_details.username})
    if row is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")

    try:
        if not verify_password(plain_password=login_details.password, hashed_password=row.get("password")):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")
    except (ValueError, TypeError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username and password do not match")

    return {"status", "ok"}
