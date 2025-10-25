from pydantic import BaseModel

class NoteInput(BaseModel):
    title: str = ''
    body: str = ''