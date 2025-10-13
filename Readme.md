# DummyRequestCounter — Part 1

Minimal FastAPI + Redis with Docker Compose.

## Quick Start
- Build & run:
  docker compose up --build -d
  docker compose ps
- Test:
  curl http://localhost:8000/ping
- Docs: http://localhost:8000/docs

## Config (.env)
API_PORT=8000
REDIS_HOST=redis
REDIS_PORT=6379

## Common
docker compose logs -f api
docker compose up -d --build
docker compose down
