from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
# Use env vars with defaults
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    count = r.incr('hits')
    return jsonify({"message": f"Hello! This page has been visited {count} times."})

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
