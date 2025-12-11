from sqlalchemy.ext.asyncio import AsyncSession

import book_api.model.book as book_model
import book_api.schemas.book as book_schemas


def get_all_books(
        db: AsyncSession 
        ):
    return db.query(book_model.Book).all()

def get_book_by_title(
        db: AsyncSession,
        book_title: str
        ):
    return db.query(book_model.Book).filter(book_model.Book.title == book_title).all()

def get_book_by_author(
        db: AsyncSession,
        book_author: str
        ):
    return db.query(book_model.Book).filter(book_model.Book.author == book_author).all()

def get_book_by_year(
        db: AsyncSession,
        book_year: str
        ):
    return db.query(book_model.Book).filter(book_model.Book.year == book_year).all()

def create_new_book(
        db: AsyncSession,
        book: book_schemas.CreateBook 
        ):
    db_book = book_model.Book(title= book.title, author= book.author, year= book.year)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

def update_book(
        db: AsyncSession,
        book: book_schemas.UpdateBook, 
        book_id: int
        ):
    db.query(book_model.Book).filter(book_model.Book.id == book_id).update({
        book_model.Book.title: book.title,
        book_model.Book.author: book.author,
        book_model.Book.year: book.year
        })
    db.commit()

    return True

def delete_book(
        db: AsyncSession,
        book_id: int
        ):
    db.query(book_model.Book).filter(book_model.Book.id == book_id).delete()
    db.commit()

    return True
