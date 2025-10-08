from fastapi import FastAPI, HTTPException
import os
import redis
import uvicorn

app = FastAPI()

def create_redis_client():
    # 1) Prefer a full URL if provided, e.g. redis://:pass@redis:6379/0
    url = os.getenv("REDIS_URL", "").strip()
    if url:
        return redis.from_url(url, decode_responses=True)

    # 2) Otherwise, build from parts (all overridable)
    host = os.getenv("REDIS_HOST", "redis")         # default works in Docker network
    port = int(os.getenv("REDIS_PORT", "6379"))
    db = int(os.getenv("REDIS_DB", "0"))
    password = os.getenv("REDIS_PASSWORD") or None

    return redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)

r = create_redis_client()

@app.get("/")
def hello():
    try:
        visits = r.incr("hits")
        return {"message": f"Hello! This page has been visited {visits} times."}
    except Exception as e:
        # Don’t crash; return a friendly 500 so /docs still works
        raise HTTPException(status_code=500, detail=f"Redis error: {e}")

@app.get("/health")
def health():
    try:
        r.ping()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Redis not ready: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", "8000")))
