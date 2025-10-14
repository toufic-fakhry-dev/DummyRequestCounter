from flask import Flask
import os
import redis

# Create Flask app
app = Flask(__name__)

# Redis config (use environment variables set in docker-compose)
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


@app.route("/")
def hello():
    hits = r.incr("hits")
    return f"Hello! This page has been visited {hits} times."


if __name__ == "__main__":
    # For local debugging (not used inside Docker)
    app.run(host="0.0.0.0", port=8000, debug=True)
