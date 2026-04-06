from fastapi import FastAPI

app = FastAPI()

state = {"step": 0}

@app.post("/reset")
def reset():
    global state
    state = {"step": 0}
    return {"state": state}

@app.post("/step")
def step(action: dict):
    global state
    state["step"] += 1
    return {"state": state, "reward": 1.0, "done": False}

@app.get("/state")
def get_state():
    return state
