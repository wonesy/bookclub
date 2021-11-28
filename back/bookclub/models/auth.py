from pydantic import BaseModel
from enum import Enum

class LoginDetails(BaseModel):
    username: str
    password: str


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


class DecodedToken(BaseModel):
    sub: str
    exp: int
    type: str
