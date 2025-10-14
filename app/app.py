import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis.asyncio import Redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

redis_client: Redis | None = None


@asynccontextmanager
async def lifespan(_: FastAPI):
    global redis_client
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    try:
        # best-effort ping; don't crash if redis not ready yet
        try:
            await redis_client.ping()
        except Exception:
            pass
        yield
    finally:
        if redis_client:
            await redis_client.aclose()


app = FastAPI(title="FastAPI + Redis", lifespan=lifespan)


@app.get("/")
async def index():
    if not redis_client:
        return JSONResponse(
            {"message": "Redis client not ready"},
            status_code=503
        )
    try:
        hits = await redis_client.incr("hits")
        return {"message": "Hello from FastAPI via Redis!", "hits": hits}
    except Exception as e:
        return JSONResponse(
            {"status": "error", "detail": str(e)},
            status_code=500
        )


@app.get("/health")
async def health():
    try:
        if redis_client and await redis_client.ping():
            return {"status": "ok"}
        return JSONResponse({"status": "degraded"}, status_code=200)
    except Exception as e:
        return JSONResponse(
            {"status": "error", "detail": str(e)},
            status_code=500
        )
