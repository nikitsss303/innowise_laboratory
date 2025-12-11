from typing import Optional
from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str
    year: Optional[str] = None


class CreateBook(BaseBook):
    pass


class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[str] = None


class ReadBook(BaseBook):
    id: int

    model_config = {
        "from_attributes": True
    }
