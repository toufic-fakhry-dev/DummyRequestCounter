from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def hello():
    redis.incr('hits')
    hits = redis.get('hits').decode('utf-8')
    return f"Hello! This page has been visited {hits} times."

# Remove or comment out the main block if it causes issues
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)