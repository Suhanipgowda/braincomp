from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Add CORS middleware to allow cross-origin requests from any device
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow any method (GET, POST, etc.)
    allow_headers=["*"],  # Allow any headers
)

# Global variables to track running status and activity
running = False
activity = "rest"

@app.get("/start")
def start():
    global running
    running = True
    return {"status": "running"}

@app.get("/stop")
def stop():
    global running
    running = False
    return {"status": "stopped"}

@app.get("/set_activity/{mode}")
def set_activity(mode: str):
    global activity
    activity = mode
    return {"activity": activity}

@app.get("/eeg")
def get_eeg():
    global running, activity

    if not running:
        return {"alpha": 0, "beta": 0, "gamma": 0}

    base_alpha = 20 + random.random() * 5
    base_beta = 10 + random.random() * 4
    base_gamma = 5 + random.random() * 3

    if activity == "rest":
        alpha = base_alpha + 5 * random.random()
        beta = base_beta + random.random()
        gamma = base_gamma + 0.5 * random.random()

    elif activity == "walking":
        alpha = base_alpha - 3 * random.random()
        beta = base_beta + 3 * random.random()
        gamma = base_gamma + 2 * random.random()

    elif activity == "running":
        alpha = base_alpha - 6 * random.random()
        beta = base_beta + 6 * random.random()
        gamma = base_gamma + 4 * random.random()

    return {
        "alpha": round(alpha, 2),
        "beta": round(beta, 2),
        "gamma": round(gamma, 2)
    }
