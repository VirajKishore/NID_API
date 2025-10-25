from fastapi import FastAPI
from model.database import DBSession
from model import models

app = FastAPI()

# Returns all notes.
@app.get("/notes")
def get_notes():
    db = DBSession()
    try:
        notes = db.query(models.Note).all()
    finally:
        db.close()
    return notes