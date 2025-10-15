from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/count")
def get_count():
    count = r.incr("counter")
    return {"counter": count}