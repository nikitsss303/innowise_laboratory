from sqlalchemy import Integer 
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from book_api.config.database import Base



class Book(Base):
    __tablename__ = "books" 

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
