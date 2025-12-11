from sqlalchemy.ext.asyncio import AsyncSession

import book_api.model.book as book_model
import book_api.schemas.book as book_schemas


async def get_all_books(
        db: AsyncSession 
        ):
    return await db.query(book_model.Book).all()

async def get_book_by_title(
        db: AsyncSession,
        book_title: str
        ):
    return await db.query(book_model.Book).filter(book_model.Book.title == book_title).all()

async def get_book_by_author(
        db: AsyncSession,
        book_author: str
        ):
    return await db.query(book_model.Book).filter(book_model.Book.author == book_author).all()

async def get_book_by_year(
        db: AsyncSession,
        book_year: str
        ):
    return await db.query(book_model.Book).filter(book_model.Book.year == book_year).all()

async def get_book_by_id(
        db: AsyncSession,
        book_id: int
        ):
    return await db.query(book_model.Book).filter(book_model.Book.id == book_id).all()

async def create_new_book(
        db: AsyncSession,
        book: book_schemas.CreateBook 
        ):
    db_book = book_model.Book(title= book.title, author= book.author, year= book.year)

    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)

    return db_book

async def update_book(
        db: AsyncSession,
        book: book_schemas.UpdateBook, 
        book_id: int
        ):
    await db.query(book_model.Book).filter(book_model.Book.id == book_id).update({
        book_model.Book.title: book.title,
        book_model.Book.author: book.author,
        book_model.Book.year: book.year
        })
    await db.commit()

    return True

async def delete_book(
        db: AsyncSession,
        book_id: int
        ):
    await db.query(book_model.Book).filter(book_model.Book.id == book_id).delete()
    await db.commit()

    return True
