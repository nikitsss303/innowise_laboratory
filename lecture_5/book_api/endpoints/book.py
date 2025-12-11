from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

import book_api.schemas.book as schemas_book

from book_api.controllers.book import BookController
from book_api.config.database import get_db


router = APIRouter(prefix="/books", tags=["Books"])

book_controller = BookController()

@router.get("/")
async def get_all_books(
        db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.get_all_book(db= db)
    if not success:
       raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Books not found",
                "status_code": status_code,
            },
        )
    response_content= {
        "data": data,
        "detail": {
            "message": "Books was found",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)
@router.get("/title/{book_title}")
async def get_book_by_title(
    book_title: str,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.get_book_by_title(db=db, book_title=book_title)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Books not found",
                "status_code": status_code,
            },
        )
    response_content= {
        "data": data,
        "detail": {
            "message": "Books was found",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)

@router.get("/author/{book_author}")
async def get_book_by_author(
    book_author: str,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.get_book_by_author(db=db, book_author=book_author)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Books not found",
                "status_code": status_code,
            },
        )
    response_content= {
        "data": data,
        "detail": {
            "message": "Books was found",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)

@router.get("/year/{book_year}")
async def get_book_by_year(
    book_year: str,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.get_book_by_year(db=db, book_year=book_year)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Books not found",
                "status_code": status_code,
            },
        )
    response_content= {
        "data": data,
        "detail": {
            "message": "Books was found",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)
    

@router.post("/", response_model=schemas_book.CreateBook)
async def create_book(
    book: schemas_book.CreateBook,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.create_new_book(db=db, book=book)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Book already exists",
                "status_code": status_code,
            },
        )
    book_dict = schemas_book.ReadBook.model_validate(data).model_dump() 
    response_content= {
        "data": book_dict,
        "detail": {
            "message": "Successfully added book",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)

@router.put("/{book_id}", response_model=schemas_book.UpdateBook)
async def update_book(
    book_id: int,
    book: schemas_book.UpdateBook,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.update_book(db=db, book_id=book_id, book=book)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail= {
                "message": "Book not found",
                "status_code": status_code,
            },
        )
    response_content= {
        "data": data,
        "detail": {
            "message": "Successfully update book",
            "status_code": status_code,
        },
    }   
    return JSONResponse(content=response_content, status_code=status_code)

@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    db: AsyncSession = Depends(get_db)
):
    success, data, status_code = await book_controller.delete_book(db=db, book_id=book_id)
    if not success:
        raise HTTPException(
            status_code= status_code,
            detail=data
        )
    response_content= {
        "detail": data
    }   
    return JSONResponse(content=response_content, status_code=status_code)
