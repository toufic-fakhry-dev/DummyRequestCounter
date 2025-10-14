# DummyRequestCounter

A simple multi-container FastAPI application with Redis to count page visits. This project demonstrates Docker Compose orchestration, persistent storage, networking, and multiple web instances.

## Project Structure

```
.
├── app/                 # FastAPI application code
│   └── app.py
├── Dockerfile
├── requirements.txt
└── docker-compose.yml
```

## Setup and Run

1. **Build and start containers**

```bash
docker compose up --build -d
```

2. **Check running containers**

```bash
docker compose ps
```

You should see 3 web containers (`web1`, `web2`, `web3`) and 1 Redis container running.

## Web Endpoints

* `http://localhost:8000/` → web1
* `http://localhost:8001/` → web2
* `http://localhost:8002/` → web3

> All web instances share the same Redis backend, so the page visit counter is global across all instances.

## Test API

You can test using `curl` or Postman:

```bash
curl http://localhost:8000/
curl http://localhost:8001/
curl http://localhost:8002/
```

You should see the visit counter increment globally, no matter which web instance you hit.

## Redis CLI (optional)

Check the current hits count:

```bash
docker compose exec redis redis-cli GET hits
```

## Clean-Up

Stop and remove all containers, networks, and volumes:

```bash
docker compose down -v
```
