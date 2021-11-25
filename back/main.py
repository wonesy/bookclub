"""Main"""
import os
import sys
import logging
from typing import Optional

from fastapi import FastAPI
from yoyo import read_migrations, get_backend

logger = logging.getLogger("uvicorn.default")

try:
    DATABASE_USER = os.getenv("POSTGRES_USER")
    DATABASE_PASS = os.getenv("POSTGRES_PASSWORD")
    DATABASE_NAME = os.getenv("POSTGRES_DB")
except KeyError as ke:
    logger.error(f"Environment variables must be defined: {ke}")
    sys.exit(1)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    backend = get_backend(f"postgres://{DATABASE_USER}:{DATABASE_PASS}@db/{DATABASE_NAME}")
    migrations = read_migrations("./migrations")

    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))

@app.get("/")
def get_root():
    """Root"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Get items"""
    return {"item_id": item_id, "q":q}
