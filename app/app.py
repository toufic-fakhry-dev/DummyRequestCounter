from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB   = int(os.getenv("REDIS_DB", "0"))

redis = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

@app.get("/")
def hello():
    redis.incr('hits')
    hits = redis.get('hits')
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)