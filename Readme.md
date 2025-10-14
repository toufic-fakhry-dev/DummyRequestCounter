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

## Part 2 — Persistence & Networks

### 2.1 Persist Redis data
- Compose uses a named volume:
  - redis service:
    volumes:
      - redis_data:/data
  - bottom of file:
    volumes:
      redis_data:
- Verify:
  docker compose exec redis redis-cli set lab:part2 hello
  docker compose exec redis redis-cli get lab:part2
  docker compose down && docker compose up -d
  docker compose exec redis redis-cli get lab:part2  (=> hello)

### 2.2 Default network
docker network ls | findstr /i dummyrequestcounter
docker network inspect dummyrequestcounter_default

### 2.3 Custom network
- Compose adds:
  networks:
    app_net:
      driver: bridge
- Both services include:
  networks:
    - app_net
- Verify:
  docker network ls | findstr /i dummyrequestcounter
  docker network inspect dummyrequestcounter_app_net
