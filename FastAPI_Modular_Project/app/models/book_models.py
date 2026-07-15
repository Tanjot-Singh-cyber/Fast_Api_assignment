from typing import Optional
from pydantic import BaseModel


# Used when creating a new book
class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str


# Used for PUT (complete update)
class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    language: str


# Used for PATCH (partial update)
class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    language: Optional[str] = None



# Public response returned to the client
# Notice internal fields are hidden
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    language: str


# Used by POST, PUT, PATCH and DELETE
class BookActionResponse(BaseModel):
    message: str
    book: BookResponse