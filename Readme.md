# Dummy Request Counter

## Overview

This project is a simple multi-container application built using **FastAPI** and **Redis**.
It demonstrates how to use Docker Compose to orchestrate multiple services, implement persistent storage, and configure custom networks.

* **FastAPI** → Web API framework
* **Uvicorn** → ASGI server to run FastAPI
* **Redis** → In-memory data store for caching or counters
* **Docker Compose** → Service orchestration

---


## Prerequisites

* Docker
* Docker Compose
* Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd DummyRequestCounter
```

### 2. Update `.gitignore`

Ensure the following are ignored:

* Local Docker configurations
* Environment variables (to avoid exposing secrets)
* Runtime log files

---

### 3. Build Docker images and start containers

```bash
docker-compose up --build
```

* The `app` service runs the FastAPI server.
* The `redis` service runs the Redis database.

Check running containers:

```bash
docker ps
```

Expected output:

* `dummy-counter-app` → Running and healthy
* `dummy-counter-redis` → Running and healthy

---

### 4. Test the API

Check the health endpoint using Postman, curl, or a browser:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

## Persistent Storage

* Redis data is persisted using a named Docker volume `redis_data`.
* This ensures data remains intact even if the container is removed.

---

## Custom Network

* A custom Docker network is created for service communication.
* Both `app` and `redis` services are attached to this network to isolate traffic and avoid conflicts.

Check networks:

```bash
docker network ls
```

---

## Troubleshooting and Debugging

### 1. View logs

```bash
docker-compose logs app
docker-compose logs redis
```

* Logs show container startup messages and requests.
* Health check requests (`GET /health`) are normal and indicate Docker is monitoring container health.

### 2. Execute commands inside a container

```bash
docker-compose exec app ls
```

* Use this to inspect files, debug, or run commands inside the container.
* Example output: `app.py`, `requirements.txt`, etc.

---

## Notes

* Multiple health check calls in logs are normal; Docker uses them to verify container health.
* Persistent storage and custom networks improve reliability and scalability.

---

## Author

**Myriam Braidi**
LAB2 – Docker Compose  


