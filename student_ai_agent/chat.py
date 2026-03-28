from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/chat")
def chat(q: Query):
    return {"answer": f"You asked: {q.question}"}