from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from book_api.init_db import init_models 
from book_api.routers.api import router as api_router


@asynccontextmanager
async def lifespan(book_api: FastAPI):
    await init_models()
    yield

book_api = FastAPI(title="Book API", version="1.0", lifespan= lifespan)


book_api.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:book_api",
        host="127.0.0.1",   
        port=8000,          
        reload=True,        
    )
