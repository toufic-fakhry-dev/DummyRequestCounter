# Dummy Request Counter

A simple FastAPI + Redis demo running with Docker Compose. Each request to `/` increments a counter stored in Redis and returns the total number of visits.

## Run
```bash
docker compose up --build -d
docker compose logs -f api
docker compose down


## Test the API
curl http://localhost:8000/

## Services communicate over a custom bridge network called appnet. The API connects to Redis at redis:6379 inside this network.
docker network ls
docker network inspect dummyrequestcounter_appnet
API Port: 8000 → http://localhost:8000
Redis Port: 6379 → localhost:6379