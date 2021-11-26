"""Main"""
import logging
from typing import Optional

from fastapi import FastAPI
from bookclub.db import init_db, database

from bookclub.routers import members, auth

app = FastAPI()

for router in [
    members.router,
    auth.router
]:
    app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()

@app.get("/")
def get_root():
    """Root"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Get items"""
    return {"item_id": item_id, "q":q}
