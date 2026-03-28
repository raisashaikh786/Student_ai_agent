from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Note(BaseModel):
    text: str

@router.post("/summarize")
def summarize(note: Note):
    summary = note.text[:100]   # simple version
    return {"summary": summary}