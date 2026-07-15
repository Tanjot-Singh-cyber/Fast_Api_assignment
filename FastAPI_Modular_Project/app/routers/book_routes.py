from typing import Optional

from fastapi import APIRouter, HTTPException, status

# Shared data
from app.data.book_data import books

# Pydantic models
from app.models.book_models import (
    BookActionResponse,
    BookCreate,
    BookPatch,
    BookResponse,
    BookUpdate,
)

# Every route in this file starts with /books
router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get(
    "",
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK
)
def get_books(
    genre: Optional[str] = None,
    language: Optional[str] = None
):
    # Start with all books
    filtered_books = books

    # Filter by genre
    if genre is not None:
        filtered_books = [
            book
            for book in filtered_books
            if book["genre"].lower() == genre.lower()
        ]

    # Filter by language
    if language is not None:
        filtered_books = [
            book
            for book in filtered_books
            if book["language"].lower() == language.lower()
        ]

    return filtered_books


@router.get(
    "/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK
)
def get_book_by_id(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
    
    
    
@router.post(
    "",
    response_model=BookActionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(book: BookCreate):

    # Check for duplicate title (case-insensitive)
    for existing_book in books:
        if existing_book["title"].lower() == book.title.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A book with this title already exists"
            )

    # Generate new ID
    new_id = max(
        (existing_book["id"] for existing_book in books),
        default=0
    ) + 1

    # Create dictionary
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "language": book.language,
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }

    books.append(new_book)

    return {
        "message": "Book created successfully",
        "book": new_book
    }
    
    
@router.put(
    "/{book_id}",
    response_model=BookActionResponse,
    status_code=status.HTTP_200_OK
)
def update_book(book_id: int, book: BookUpdate):

    for existing_book in books:

        if existing_book["id"] == book_id:

            existing_book.update(book.model_dump())

            return {
                "message": "Book updated successfully",
                "book": existing_book
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
    
@router.patch(
    "/{book_id}",
    response_model=BookActionResponse,
    status_code=status.HTTP_200_OK
)
def patch_book(book_id: int, book: BookPatch):

    for existing_book in books:

        if existing_book["id"] == book_id:

            update_data = book.model_dump(exclude_none=True)

            existing_book.update(update_data)

            return {
                "message": "Book partially updated successfully",
                "book": existing_book
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
    
@router.delete(
    "/{book_id}",
    response_model=BookActionResponse,
    status_code=status.HTTP_200_OK
)
def delete_book(book_id: int):

    for existing_book in books:

        if existing_book["id"] == book_id:

            books.remove(existing_book)

            return {
                "message": "Book deleted successfully",
                "book": existing_book
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )