"""Bookclub main entrypoint"""
from fastapi import FastAPI
from bookclub.db import init_db, database

from bookclub.routers import books, members, auth, genres

app = FastAPI()

for router in [
    members.router,
    auth.router,
    genres.router,
    books.router
]:
    app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()
