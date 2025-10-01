# DummyRequestCounter — FastAPI + Redis (Docker Compose)

## Overview
Small multi-container app: **FastAPI** web service + **Redis** counter.

## Prerequisites
- Docker Desktop (Linux containers / WSL2 enabled on Windows)
- curl or a browser/Postman for testing

## Project Structure
```
.
├─ app/
│  ├─ app.py
│  └─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .gitignore
├─ .dockerignore
└─ README.md
```

## Quick Start
```bash
docker compose up -d --build
```

### Test
- Browser: <http://localhost:${PORT:-8000}/health> and <http://localhost:${PORT:-8000}/>
- Curl:
  ```bash
  curl http://localhost:${PORT:-8000}/health
  curl http://localhost:${PORT:-8000}/
  ```
- PowerShell (Invoke-WebRequest):
  ```powershell
  iwr http://localhost:${PORT:-8000}/health -UseBasicParsing
  iwr http://localhost:${PORT:-8000}/ -UseBasicParsing
  ```


## Useful Commands
```bash
# See running services
docker compose ps

# Tail logs
docker compose logs -f web
docker compose logs -f redis

# Exec inside a container
docker compose exec web sh
docker compose exec redis sh -c "redis-cli ping; redis-cli get hits"

# Stop containers (keep volumes)
docker compose down

# Stop and also remove volumes
docker compose down -v
```

## Notes
- Services communicate over an isolated Compose network; the app reaches Redis via hostname **redis**.
- Redis data is persisted to the named volume **redis-data** (defined in `docker-compose.yml`).

---

### For Graders (Part 1)
- **Implemented**: Dockerfile for FastAPI, pinned requirements, docker-compose orchestration, environment overrides (`PORT`, `REDIS_PORT`, `REDIS_DB`), and README.


## Part 2 — Persistence & Networks

The `docker-compose.yml` created in Part 1 already includes the pieces needed for persistence and networking. This section explains them and how to verify.

### What’s configured
- **Persistent Redis data**
  - Named volume **`redis-data`** is mounted at `/data` in the Redis container.
  - Redis snapshots (`--save 60 1`) keep the counter across restarts.
- **Custom network**
  - Both services join a dedicated bridge network **`appnet`**.
  - The app reaches Redis by hostname **`redis`** on port `${REDIS_PORT:-6379}`.

### Verify persistence
```bash
# bump the counter
curl http://localhost:${PORT:-8000}/

# restart containers WITHOUT deleting volumes
docker compose down
docker compose up -d

# confirm the value is still there
docker compose exec redis sh -c "redis-cli get hits"

## Part 3 — Troubleshooting & Debugging Docker Compose

1) View container logs
- All services (timestamps, follow):  docker compose logs --timestamps -f
- Web only:                          docker compose logs -f web
- Redis only:                        docker compose logs -f redis

2) Run commands inside containers (exec)
- Web:
  docker compose exec web python -V
  docker compose exec web sh -c "env | sort | grep -E '^REDIS|^PORT'"
  docker compose exec web python -c "import os,socket; print(socket.gethostbyname(os.getenv('REDIS_HOST','redis')))"
- Redis:
  docker compose exec redis sh -c "redis-cli ping; redis-cli get hits"
  (optional) docker compose exec redis sh -c "redis-cli monitor"
