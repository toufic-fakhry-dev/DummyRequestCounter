from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

# Optional overrides using environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.get("/")
def hello():
    try:
        redis.incr('hits')
        hits = redis.get('hits').decode('utf-8')
        return f"Hello! This page has been visited {hits} times."
    except Exception as e:
        return {"error": str(e)}




@app.get("/health-check")
def health_check():
    return "service is up and running"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
