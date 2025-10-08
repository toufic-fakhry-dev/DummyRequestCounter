from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI(title="Dummy Request Counter")

# Configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

# Redis connection
try:
    redis = Redis(
        host=REDIS_HOST, 
        port=REDIS_PORT, 
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
except Exception as e:
    print(f"Redis connection failed: {e}")
    redis = None

@app.get("/")
def hello():
    if redis:
        try:
            redis.incr('hits')
            hits = redis.get('hits')
            return {"message": f"Hello! This page has been visited {hits} times."}
        except Exception as e:
            return {"error": f"Redis error: {e}", "hits": 0}
    return {"error": "Redis not available", "hits": 0}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/count")
def get_count():
    if redis:
        try:
            hits = redis.get('hits') or 0
            return {"count": int(hits)}
        except Exception as e:
            return {"error": f"Redis error: {e}", "count": 0}
    return {"error": "Redis not available", "count": 0}

@app.get("/reset")
def reset_count():
    if redis:
        try:
            redis.delete('hits')
            return {"message": "Counter reset", "count": 0}
        except Exception as e:
            return {"error": f"Redis error: {e}"}
    return {"error": "Redis not available"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)