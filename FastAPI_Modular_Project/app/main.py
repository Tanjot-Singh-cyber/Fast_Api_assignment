from fastapi import FastAPI

from app.routers.book_routes import router as books_router

app = FastAPI(
    title="Library API",
    description="A modular FastAPI CRUD application",
    version="1.0.0"
)

app.include_router(books_router)


@app.get("/", tags=["Root"])
def home():
    return {
        "message": "Library API is running"
    }