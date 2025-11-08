from flask import Flask, jsonify
import redis
import os
import logging

# Configure logging BEFORE running the app
logging.basicConfig(filename="/var/log/app/app.log", level=logging.INFO)

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=int(os.getenv("REDIS_PORT", 6379)))

@app.route("/")
def index():
    try:
        count = r.incr("visits")
        logging.info(f"Visit number: {count}")
    except Exception as e:
        logging.error(f"Redis error: {e}")
        return jsonify({"error": str(e)}), 500
    return jsonify({"message": "Hello from Flask + Redis!", "visits": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
