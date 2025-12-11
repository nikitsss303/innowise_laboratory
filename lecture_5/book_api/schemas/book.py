from typing import Optional
from pydantic import BaseModel


class BaseBook(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[str] = None

class ReadBook(BaseBook):
    class Config:
        from_attributes = True

class CreateBook(BaseBook):
    pass

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[str] = None

class DeleteBook(BaseModel):
    id: int
