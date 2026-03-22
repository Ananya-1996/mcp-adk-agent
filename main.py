from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP + ADK Agent Running 🚀"}

@app.get("/agent")
def agent(city: str):
    return run_agent(city)
