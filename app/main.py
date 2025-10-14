# app/main.py
import os
import redis
from fastapi import FastAPI

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
API_PORT   = int(os.getenv("API_PORT", "8000"))  # optional if you ever run uvicorn from code

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

app = FastAPI()

@app.get("/ping")
def ping():
    try:
        return {"pong": r.ping()}
    except Exception as e:
        return {"error": str(e)}
