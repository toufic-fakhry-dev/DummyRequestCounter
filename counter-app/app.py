from flask import Flask
import os
import redis
import logging
import sys

# --- Logging to file (/logs/app.log) and stdout ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("/logs/app.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)

@app.route("/")
def index():
    count = r.incr("hits")
    app.logger.info(f"handled request #{count}")
    return f"Hello from Kubernetes! This page has been visited {count} times.\n"

@app.route("/healthz")
def healthz():
    try:
        r.ping()
        return "ok", 200
    except Exception:
        app.logger.exception("redis unreachable")
        return "redis unreachable", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
