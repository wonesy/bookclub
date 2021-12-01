"""Bookclub main entrypoint"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()
