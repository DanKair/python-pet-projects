# This is my first REST API app that I built on my own
# Used only YouTube, Medium and docs for reference

from typing import Optional, Annotated
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from .schemas import Items


app = FastAPI (title="To-Do App",
               description="This experiment app have CRUD functionality, "
                           "but doesn't have database functionality. "
                           "So it can't store information after reloading page"
               )


items = []


@app.post("/items")
def add_items(item: Annotated[Items, Depends()]):
    items.append(item)
    return items


@app.delete("/items")
def delete_items(id: int):
    items.remove(items[id])
    return items


@app.put("/items")
def update_item(id: int, new_item: Annotated[Items, Depends()]):
    items[id] = new_item
    return items


@app.get("/items")
def get_items():
    return items


# This part of code made to check whether item exist or not
@app.get("/items/{item_id}")
def get_items(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")