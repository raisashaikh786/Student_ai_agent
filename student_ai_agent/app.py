from fastapi import FastAPI
from tasks import router as task_router
from planner import router as planner_router
from notes import router as notes_router
from chat import router as chat_router
from focus import router as focus_router

app = FastAPI()

app.include_router(task_router)
app.include_router(planner_router)
app.include_router(notes_router)
app.include_router(chat_router)
app.include_router(focus_router)

@app.get("/")
def home():
    return {"message": "AI Student Agent Running 🚀"}