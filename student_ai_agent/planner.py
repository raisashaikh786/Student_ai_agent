from fastapi import APIRouter

router = APIRouter()

@router.get("/plan")
def generate_plan():
    return {
        "schedule": [
            {"time": "9-11", "task": "Study DBMS"},
            {"time": "11-12", "task": "Break"},
            {"time": "2-4", "task": "TOC Practice"}
        ]
    }