from datetime import datetime
from pydantic import BaseModel


class Items(BaseModel):
    item: str
    description: str | None = None
