import requests

BASE_URL = "https://your-space-url"

def reset():
    return requests.post(f"{BASE_URL}/reset").json()

def step(action):
    return requests.post(f"{BASE_URL}/step", json=action).json()
