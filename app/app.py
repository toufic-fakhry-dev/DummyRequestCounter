from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
