from fastapi import Depends, status, HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from bookclub.db.queries.members import GET_MEMBER_BY_USERNAME
from bookclub.models.auth import TokenPair
from bookclub.db import database
from bookclub.models.member import Member

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300000
REFRESH_TOKEN_EXPIRE_MINUTES = 1800000
REGISTRATION_TOKEN_EXPIRE_MINUTES = 10080 # one week

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_registration_token(data: dict) -> str:
    reg = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    reg.update({"exp": expire})
    return jwt.encode(reg, SECRET_KEY, algorithm=ALGORITHM)


def create_tokens(data: dict) -> TokenPair:
    access_encode = data.copy()
    refresh_encode = data.copy()

    access_expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_encode.update({"exp": access_expire, "type": "access"})
    access_token = jwt.encode(access_encode, SECRET_KEY, algorithm=ALGORITHM)

    refresh_expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_encode.update({"exp": refresh_expire, "type": "refresh"})
    refresh_token = jwt.encode(refresh_encode, SECRET_KEY, algorithm=ALGORITHM)

    return TokenPair(access_token=access_token, refresh_token=refresh_token)


async def get_current_member_from_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    row = await database.fetch_one(GET_MEMBER_BY_USERNAME, {"username": payload.get("sub", "")})
    if row is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized access")
    return Member(**row)
