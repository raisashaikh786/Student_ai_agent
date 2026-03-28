from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/focus-score")
def get_focus():
    score = random.randint(50, 100)

    if score > 80:
        message = "🔥 Excellent focus!"
    elif score > 60:
        message = "👍 Good, but can improve"
    else:
        message = "⚠️ You are distracted!"

    return {"score": score, "message": message}from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/focus-score")
def get_focus():
    score = random.randint(50, 100)

    if score > 80:
        message = "🔥 Excellent focus!"
    elif score > 60:
        message = "👍 Good, but can improve"
    else:
        message = "⚠️ You are distracted!"

    return {"score": score, "message": message}