from fastapi import FastAPI
import gradio as gr
import uvicorn

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

def respond(message, history):
    return "AI Agent 🤖: " + message

demo = gr.ChatInterface(fn=respond)

app = gr.mount_gradio_app(app, demo, path="/")

# 🔥 THIS FIXES YOUR ERROR
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
    
