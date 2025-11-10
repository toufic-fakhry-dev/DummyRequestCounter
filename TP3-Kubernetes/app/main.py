from flask import Flask
import os, redis, logging

# logging to file (for Part 4 sidecar later)
os.makedirs("/var/log/app", exist_ok=True)
app = Flask(__name__)
fh = logging.FileHandler("/var/log/app/app.log")
fh.setLevel(logging.INFO)
app.logger.addHandler(fh); app.logger.setLevel(logging.INFO)

r = redis.Redis(host=os.getenv("REDIS_HOST","redis"), port=int(os.getenv("REDIS_PORT","6379")), db=0)

@app.route("/")
def index():
    count = r.incr("hits")
    app.logger.info("Handled request %s", count)
    return f"Hello! I have been seen {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
