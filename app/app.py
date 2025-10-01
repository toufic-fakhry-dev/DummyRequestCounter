from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

# Read from env with sane defaults
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

# decode_responses=True returns str instead of bytes
redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/")
def hello():
    hits = redis.incr("hits")
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("API_PORT", "8000")))
