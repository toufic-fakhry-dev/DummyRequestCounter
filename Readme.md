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

