import logging
from typing import Optional
from fastapi import Header, HTTPException, status
from jose import jwt

from bookclub.auth.token import ALGORITHM, SECRET_KEY
from bookclub.models.auth import DecodedToken

logger = logging.getLogger("uvicorn.default")

async def get_token_from_header(authorization: Optional[str] = Header(None)) -> DecodedToken:
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized, provide authorization token")
    try:
        _, token = authorization.split(' ')
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except (ValueError, jwt.JWTError, jwt.JWTClaimsError, jwt.ExpiredSignatureError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized, invalid token")
    return DecodedToken(**decoded_token)
