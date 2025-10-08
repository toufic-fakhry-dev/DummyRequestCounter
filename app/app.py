from flask import Flask
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

APP_PORT = int(os.getenv("APP_PORT", "8000"))

@app.route("/")
def hello():
    hits = r.incr("hits")
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=True)



    