from fastapi import APIRouter
from book_api.endpoints import book

router = APIRouter()
router.include_router(book.router)
