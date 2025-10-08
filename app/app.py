from fastapi import FastAPI, HTTPException
from redis import Redis
import uvicorn

app = FastAPI()

REDIS_HOST = "redis"
REDIS_PORT = 6379

try:
    redis = Redis(
        host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=2, socket_timeout=2
    )
    # Test connection
    redis.ping()
except Exception:
    redis = None


@app.get("/")
def hello():
    if redis is None:
        return {"message": "Hello! Redis not available. Page visits not counted."}

    try:
        redis.incr("hits")
        hits = redis.get("hits")
        if isinstance(hits, bytes):
            hits = hits.decode("utf-8")
        return f"Hello! This page has been visited {hits} times."
    except Exception:
        return {"message": "Hello! Redis error. Page visits not counted."}


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
