# DummyRequestCounter

A simple multi-container application using **Flask** and **Redis**, orchestrated with **Docker Compose**.  
The app counts requests and stores the counter in Redis with persistent storage.

## Features

- Flask web application for handling HTTP requests
- Redis for persistent counter storage
- Docker Compose orchestration with custom networking
- Persistent volume for Redis data
- Service discovery via custom bridge network

## Architecture

### Services

**1. web (Flask Application)**
- Built from local Dockerfile
- Exposes port 5000 (configurable via `FLASK_PORT` environment variable)
- Connects to Redis using hostname `redis`
- Runs on custom network `app_network`

**2. redis (Data Store)**
- Uses official Redis 7 Alpine image
- Exposes port 6379 (configurable via `REDIS_PORT` environment variable)
- Persistent storage via named volume `redis_data` mounted at `/data`
- Runs on custom network `app_network`

### Networking

- **Custom Network**: `app_network`
  - Driver: bridge
  - Provides isolated communication between services
  - Enables automatic DNS resolution between containers
  - Services can reference each other by service name (e.g., `redis`, `web`)

### Persistent Storage

- **Volume**: `redis_data`
  - Persists Redis data across container restarts and removals
  - Mounted at `/data` inside the Redis container
  - Uses local driver for host-based storage
  - Data survives `docker-compose down` (but not `docker-compose down -v`)

## Prerequisites

- Docker Desktop or Docker Engine