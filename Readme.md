A small FastAPI service that counts visits using redis.
Runs with Docker and Docker Compose.

## How to Run

1. Make sure Docker Desktop is running.
2. Open a terminal in the project folder :
    docker compose -up build
3. The API will start on http://localhost:8000

## How to test

In browser open http://localhost:8000 
Each request increases the counter:
Hello! This page has been visited 1 times.
Hello! This page has been visited 2 times.

## Environment Variables

You can override ports and Redis settings by creating a .env file:
API_PORT=5000
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

Then run again:
docker compose up --build

Now the API will be available at http://localhost:5000
