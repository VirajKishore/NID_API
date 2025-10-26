from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.database import DBSession
from model import models
from schemas import NoteInput
from datetime import datetime


app = FastAPI()

origins = [
    "http://localhost:5173" # React app,
    "https://note-it-down-gamma.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Returns all notes.
@app.get("/notes")
def get_notes():
    db = DBSession()
    try:
        notes = db.query(models.Note).all()
    finally:
        db.close()
    return notes


@app.post("/note")
def add_note(note: NoteInput):
    db = DBSession()

    try:
        if note.title is None or note.title == "":
            raise HTTPException(status_code=400, detail="Title is required")
        new_note = models.Note(title=note.title, body=note.body)
        db.add(new_note)
        db.commit()
        db.refresh(new_note) # after commit, we need id and datetime fields to be populated in the new_note object
    finally:
        db.close()
    return new_note


@app.put("/note/{note_id}")
def update_note(note_id: int, note: NoteInput):
    db = DBSession()
    try:
        if note_id is None or note_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid note ID")
        if note.title is None or note.title == "":
            raise HTTPException(status_code=400, detail="Title is required")
        
        db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
        if db_note is None:
            raise HTTPException(status_code=404, detail="Note not found")

        db_note.title = note.title
        db_note.body = note.body
        db_note.last_updated = datetime.now()
        db.commit()
        db.refresh(db_note)
    finally:
        db.close()
    return db_note


@app.delete("/note/{note_id}")
def delete_note(note_id: int):
    db = DBSession()

    try:
        if note_id is None or note_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid note ID")

        db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
        if db_note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        
        db.delete(db_note)
        db.commit()
    finally:
        db.close()
    return {
        "status": "200",
        "message": "Note deleted successfully"
    }