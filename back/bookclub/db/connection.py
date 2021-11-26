import os
import sys
import logging
from databases import Database
from yoyo import read_migrations, get_backend

logger = logging.getLogger("uvicorn.default")

try:
    DATABASE_USER = os.getenv("POSTGRES_USER")
    DATABASE_PASS = os.getenv("POSTGRES_PASSWORD")
    DATABASE_NAME = os.getenv("POSTGRES_DB")
except KeyError as ke:
    logger.error(f"Environment variables must be defined: {ke}")
    sys.exit(1)

url = f"postgres://{DATABASE_USER}:{DATABASE_PASS}@bkdb:5432/{DATABASE_NAME}"

database = Database(url)

async def init_db():
    logger.info(f"Connecting to database")
    await database.connect()
    migrate()

def migrate():
    logger.info("Applying migrations to database")
    migrations = read_migrations("./migrations")
    backend = get_backend(url)
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
