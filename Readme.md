# 🐳 Dummy Request Counter — FastAPI + Redis (Multi-Container App)

This project demonstrates how to build, run, and manage a simple multi-container application using **FastAPI** and **Redis** with **Docker Compose**.  
The app counts how many times its root endpoint (`/`) has been visited and stores that count in Redis.

---

## ⚙️ Part 1: Setting Up a Simple Multi-Container Application

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/toufic-fakhry-dev/DummyRequestCounter.git
cd DummyRequestCounter
2️⃣ Update .gitignore
Ignore unnecessary files and directories:

bash
Copy code
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment & secrets
.env
*.env

# Logs
*.log

# Docker / Compose
docker-compose.override.yml
.docker/
3️⃣ FastAPI Application (app/app.py)
python
Copy code
from fastapi import FastAPI
from redis import Redis
import os
import uvicorn

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def hello():
    redis.incr('hits')
    hits = redis.get('hits').decode('utf-8')
    return f"Hello! This page has been visited {hits} times."

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
4️⃣ Dockerfile
dockerfile
Copy code
# Use an official Python runtime
FROM python:3.11-slim

# Create app directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code

# Set environment variable to avoid buffered output
ENV PYTHONUNBUFFERED=1
ENV APP_PORT=8000

# Run FastAPI app with uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
5️⃣ docker-compose.yml
yaml
Copy code
services:
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - redis-data:/data
    networks:
      - my-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  web:
    build: .
    restart: unless-stopped
    volumes:
      - ./:/code
    ports:
      - "${APP_PORT:-8000}:8000"
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=${REDIS_PORT:-6379}
      - APP_PORT=${APP_PORT:-8000}
    depends_on:
      redis:
        condition: service_healthy
    networks:
      - my-network

volumes:
  redis-data:

networks:
  my-network:
    driver: bridge
6️⃣ Run Containers Locally
bash
Copy code
docker compose up -d --build
✅ This builds both containers (web, redis) and starts them.

7️⃣ Test the API
Visit:

arduino
Copy code
http://localhost:8000
You should see:

bash
Copy code
Hello! This page has been visited 1 times.
Refresh to see the counter increase.

8️⃣ Update README.md
Document setup steps (done ✅).

💾 Part 2: Persistent Storage and Custom Networks
1️⃣ Add Volume for Redis Data
Added in docker-compose.yml:

yaml
Copy code
volumes:
  - redis-data:/data
Ensures data persists even after container restarts.

2️⃣ Check Network Communication
List networks:

bash
Copy code
docker network ls
✅ Found custom network:

Copy code
dummyrequestcounter_my-network
Both web and redis communicate via this network.

Inspect details:

bash
Copy code
docker network inspect dummyrequestcounter_my-network
3️⃣ Custom Network
Defined as:

yaml
Copy code
networks:
  my-network:
    driver: bridge
Isolates containers and allows inter-container communication via service names.

4️⃣ Update README.md
Documented persistence and networking configuration ✅.

🔍 Part 3: Troubleshooting & Debugging Docker Compose
1️⃣ View Container Logs
bash
Copy code
# show logs for all services
docker compose logs

# follow live logs for web service
docker compose logs -f web

# show only Redis logs
docker compose logs redis
✅ Useful for debugging startup or connection issues.

2️⃣ Run Commands Inside Containers
You can open an interactive shell inside containers.

FastAPI container:
bash
Copy code
docker compose exec web sh
ls
python --version
exit
Redis container:
bash
Copy code
docker compose exec redis sh
redis-cli
GET hits
exit
exit
✅ Allows you to test connectivity and inspect data directly inside containers.

🧹 Part 4: Clean-Up
When finished testing, stop and remove all resources created by Docker Compose.

1️⃣ Stop and Remove Containers
bash
Copy code
docker compose down
✅ Stops and removes all running containers for the project.

2️⃣ Remove Volumes and Networks
bash
Copy code
docker compose down --volumes --remove-orphans
✅ Removes:

Containers (web, redis)

Volumes (redis-data)

Networks (dummyrequestcounter_my-network)

Any orphaned services

✅ Verification
After running:

bash
Copy code
docker compose down --volumes --remove-orphans
The following commands returned no project resources:

bash
Copy code
docker ps -a
docker volume ls
docker network ls
✅ All containers, volumes, and networks removed successfully.

🎯 Final Summary
Part 1: Built and ran FastAPI + Redis using Docker Compose

Part 2: Added persistent storage and a custom network

Part 3: Learned to debug containers via logs and exec

Part 4: Cleaned up containers, volumes, and networks

✅ All parts completed successfully!