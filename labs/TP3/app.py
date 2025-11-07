from flask import Flask, Response
import redis, os, time, pathlib

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

# ensure logs dir exists
pathlib.Path("/logs").mkdir(parents=True, exist_ok=True)

@app.route("/favicon.ico")
def favicon():
    return Response(status=204)

@app.route("/")
def index():
    count = r.incr("hits")
    with open("/logs/access.log", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} HIT={count}\n")
    return f"Hello — Hits: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
