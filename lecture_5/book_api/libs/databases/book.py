from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

import book_api.models.book as book_model
import book_api.schemas.book as book_schemas


async def get_all_books(db: AsyncSession):
    result = await db.execute(select(book_model.Book))
    return result.scalars().all()


async def get_book_by_title(db: AsyncSession, book_title: str):
    result = await db.execute(select(book_model.Book).where(book_model.Book.title == book_title))
    return result.scalars().all()


async def get_book_by_author(db: AsyncSession, book_author: str):
    result = await db.execute(select(book_model.Book).where(book_model.Book.author == book_author))
    return result.scalars().all()


async def get_book_by_year(db: AsyncSession, book_year: str):
    result = await db.execute(select(book_model.Book).where(book_model.Book.year == book_year))
    return result.scalars().all()


async def get_book_by_id(db: AsyncSession, book_id: int):
    result = await db.execute(select(book_model.Book).where(book_model.Book.id == book_id))
    return result.scalar_one_or_none() 


async def create_new_book(db: AsyncSession, book: book_schemas.CreateBook):
    db_book = book_model.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def update_book(db: AsyncSession, book: book_schemas.UpdateBook, book_id: int):
    stmt = (
        update(book_model.Book)
        .where(book_model.Book.id == book_id)
        .values(title=book.title, author=book.author, year=book.year)
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()
    return True


async def delete_book(db: AsyncSession, book_id: int):
    stmt = delete(book_model.Book).where(book_model.Book.id == book_id)
    await db.execute(stmt)
    await db.commit()
    return True
