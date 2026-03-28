from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

tasks = []

class Task(BaseModel):
    title: str
    deadline: str   # format: YYYY-MM-DD
    priority: int = 1

def calculate_priority(deadline):
    today = datetime.today()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
    days_left = (deadline_date - today).days

    if days_left <= 1:
        return 5
    elif days_left <= 3:
        return 4
    elif days_left <= 7:
        return 3
    else:
        return 2

@router.post("/add-task")
def add_task(task: Task):
    task.priority = calculate_priority(task.deadline)
    tasks.append(task)
    return {"message": "Task added with smart priority"}

@router.get("/tasks")
def get_tasks():
    return sorted(tasks, key=lambda x: x.priority, reverse=True)

@router.get("/warnings")
def get_warnings():
    warnings = []
    today = datetime.today()

    for task in tasks:
        deadline_date = datetime.strptime(task.deadline, "%Y-%m-%d")
        days_left = (deadline_date - today).days

        if days_left <= 2:
            warnings.append(f"⚠️ '{task.title}' is due in {days_left} day(s)!")

    return {"warnings": warnings}