from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Starter Data
notes = [
    {
        "id": 1,
        "title": "FastAPI Intro",
        "content": "FastAPI is used to build backend APIs in Python.",
        "category": "Backend",
        "priority": "High"
    },
    {
        "id": 2,
        "title": "Request Body",
        "content": "A request body carries data sent by the client.",
        "category": "API",
        "priority": "Medium"
    }
]

# Request Body Model
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    priority: str

# Home Route
@app.get("/")
def home():
    return {
        "message": "Notes API is running"
    }

# Get All Notes
@app.get("/notes")
def get_notes():
    return notes

# Create a New Note
@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    # Generate next ID
    new_id = max([note["id"] for note in notes], default=0) + 1

    # Create new note dictionary
    new_note = {
        "id": new_id,
        "title": note.title,
        "content": note.content,
        "category": note.category,
        "priority": note.priority
    }

    # Add new note to list
    notes.append(new_note)

    # Return success response
    return {
        "message": "Note added successfully",
        "note": new_note
    }
