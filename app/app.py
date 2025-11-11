import logging, os
from flask import Flask, jsonify
import redis

# === LOGGING VERS FICHIER (pour le sidecar) ===
LOG_PATH = os.getenv("LOG_PATH", "/var/log/app/app.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def home():
    logging.info("Hit /")
    return "Requests Counter is running. Try /count"

@app.route("/count")
def count():
    value = r.incr("hits")
    logging.info("Hit /count -> %s", value)
    return jsonify({"hits": int(value)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)