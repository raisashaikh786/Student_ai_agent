from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# Dummy state
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

# Gradio UI
def respond(message, history):
    return "AI Agent 🤖: " + message

demo = gr.ChatInterface(fn=respond)

# 🔥 THIS IS THE FIX
app = gr.mount_gradio_app(app, demo, path="/")
