from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

import book_api.libs.databases.book as book_db
import book_api.schemas.book as schemas_book


class BookController:
    """
    Controller for managing book-related business logic.
    
    This controller handles all book operations including CRUD operations
    and search functionality. It acts as an intermediary layer between
    API endpoints and database operations.
    
    All methods follow a consistent return pattern:
        (success: bool, data: dict | object, status_code: int)
    """
    async def get_all_book(
        self,
        db: AsyncSession
    ):
        books = await book_db.get_all_books(db= db)
        if not books:
            return False, books, status.HTTP_404_NOT_FOUND
        return True, books, status.HTTP_200_OK

    async def get_book_by_title(
        self,
        db: AsyncSession,
        book_title: str
    ):
        books = await book_db.get_book_by_title(db= db, book_title= book_title)
        if not books:
            return False, books, status.HTTP_404_NOT_FOUND
        return True, books, status.HTTP_200_OK

    async def get_book_by_author(
        self,
        db: AsyncSession,
        book_author: str            
    ):
        books = await book_db.get_book_by_author(db= db, book_author= book_author)
        if not books:
            return False, books, status.HTTP_404_NOT_FOUND
        return True, books, status.HTTP_200_OK

    async def get_book_by_year(
        self,
        db: AsyncSession,
        book_year: str
    ):
        books = await book_db.get_book_by_year(db= db, book_year= book_year)
        if not books:
            return False, books, status.HTTP_404_NOT_FOUND
        return True, books, status.HTTP_200_OK

    async def create_new_book(
        self,
        db: AsyncSession,
        book: schemas_book.CreateBook 
    ):
        check_book = await book_db.get_book_by_title(db= db, book_title= book.title)
        if check_book:
            return False, {"message": "Book already exists"}, status.HTTP_400_BAD_REQUEST 
        new_book = await book_db.create_new_book(db= db, book= book) 
        return True, new_book, status.HTTP_201_CREATED

    async def update_book(
        self,
        db: AsyncSession,
        book_id: int,
        book: schemas_book.UpdateBook 
    ):
        check_book = await book_db.get_book_by_id(db= db, book_id= book_id)
        if not check_book:
            return False, {"message": "Book not found"}, status.HTTP_404_NOT_FOUND
        is_book_update = await book_db.update_book(db= db, book= book, book_id= book_id)
        if is_book_update:
            return True, {"message": "Successfully updated book"}, status.HTTP_200_OK

    async def delete_book(
        self,
        db: AsyncSession,
        book_id: int
    ):
        check_book = await book_db.get_book_by_id(db= db, book_id= book_id)
        if not check_book:
            return False, {"message": "Book not found"}, status.HTTP_404_NOT_FOUND
        is_book_deleted = await book_db.delete_book(db= db, book_id= book_id)
        if not is_book_deleted:
            return False, {"message": "Couldn`t to delete book"}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return True, {"message": "Successfully deleted book"}, status.HTTP_200_OK
