from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

# Default to the Docker service name "redis"
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Return str automatically (no manual .decode)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/")
def hello():
    hits = redis.incr("hits")  # incr returns the new integer value
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    # This path runs only if you launch "python app.py" locally.
    uvicorn.run(app, host="0.0.0.0", port=8000)
