from fastapi import FastAPI
from redis import Redis
import uvicorn

app = FastAPI()

# TODO: Configuration from environment variables
REDIS_HOST = "redis"
REDIS_PORT = 6379

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.get("/")
def hello():
    redis.incr("hits")
    hits = redis.get("hits")
    # Handle both bytes and string responses
    if isinstance(hits, bytes):
        hits = hits.decode("utf-8")
    return f"Hello! This page has been visited {hits} times."


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
