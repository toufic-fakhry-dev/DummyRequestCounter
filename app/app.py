import os
from flask import Flask
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, decode_responses=True
)


@app.get("/")
def hello():
    redis_client.incr('hits')
    hits = redis_client.get('hits')
    return f"Hello! This page has been visited {hits} times."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("FLASK_PORT", 5000))
    )  # nosec B104
