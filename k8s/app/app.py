from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route('/')
def hello():
    count = r.incr('hits')
    return f'Requests Counter: {count}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)