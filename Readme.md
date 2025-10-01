
````markdown
# DummyRequestCounter — FastAPI + Redis (Docker Compose)

A simple multi-container demo:
- **web**: FastAPI app served by Uvicorn
- **redis**: Redis key–value store used to count visits

## Prerequisites
- Docker Desktop (Windows/macOS/Linux) with Docker Compose v2
- WSL2 enabled on Windows

## Quick Start

```bash
# Build and run (foreground)
docker compose up --build

# Or run in background
docker compose up --build -d
````

---

## App Endpoints

* `GET /` → increments and returns page visit count
* Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Configuration (Environment Variables)

The app reads configuration from environment variables (with defaults):

* `REDIS_HOST` (default: `redis`)
* `REDIS_PORT` (default: `6379`)

**Override example (Windows PowerShell):**

```powershell
$env:REDIS_PORT="6380"
docker compose up --build
```

**docker-compose.yml excerpt:**

```yaml
services:
  web:
    environment:
      REDIS_HOST: redis
      REDIS_PORT: ${REDIS_PORT:-6379}
```

---

## Useful Commands

```bash
# Stop and remove containers
docker compose down

# View logs (follow)
docker compose logs -f

# Exec into containers
docker compose exec web sh
docker compose exec redis sh
```

---

## Notes

* Tech stack: **FastAPI**, **Uvicorn**, **Redis**
* Ports:

  * Web: `8000:8000`
  * Redis: `${REDIS_PORT:-6379}:6379` (optional external access)

---

## Persistence (Docker Volume)

Redis data is persisted via a named Docker volume so counters survive container restarts.

* Volume name: `redis_data`
* Mounted at: `/data` inside the `redis` container

**docker-compose.yml excerpt:**

```yaml
redis:
  image: redis:7-alpine
  volumes:
    - redis_data:/data

volumes:
  redis_data:
```

---

## Networks

Services communicate over a custom bridge network for clarity and isolation.

* Network name: `app_net`
* Both `web` and `redis` are attached to `app_net`

**docker-compose.yml excerpt:**

```yaml
services:
  web:
    networks:
      - app_net
  redis:
    networks:
      - app_net

networks:
  app_net:
    driver: bridge
```

