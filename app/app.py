from fastapi import FastAPI
from redis import Redis
import os 
import uvicorn

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost") 
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379)) 

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def hello():
    try:
        redis.incr('hits')
        hits = redis.get('hits')
        if hits:
            hits = hits.decode('utf-8')
        else:
            hits = 0 
        return f"Hello! This page has been visited {hits} times."
    except Exception as e:
        return {"error": f"Could not connect to Redis: {e}"} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)