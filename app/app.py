import os
from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/count", methods=["POST"])
def count():
    key = request.json.get("key")
    if not key:
        return jsonify({"error": "Missing key"}), 400

    new_count = redis_client.incr(key)
    return jsonify({"key": key, "count": new_count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT", 5000)))
