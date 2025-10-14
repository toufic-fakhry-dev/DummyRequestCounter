from fastapi import FastAPI
from redis import Redis
import os
import uvicorn  # keep this here so uvicorn is defined

app = FastAPI()

# TODO: Configuration from environment variables
REDIS_HOST = "localhost"
REDIS_PORT = 6379

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def hello():
    redis.incr("hits")
    hits = redis.get("hits").decode("utf-8")
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    # noqa: F821 - uvicorn is imported above, Flake8 may incorrectly report F821 otherwise
    uvicorn.run(app, host="0.0.0.0", port=8000)
