"""Main"""

from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    """Root"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Get items"""
    return {"item_id": item_id, "q":q}
