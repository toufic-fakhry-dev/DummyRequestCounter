# DummyRequestCounter — FastAPI + Redis (Docker Compose)

A simple multi-container demo:
- **web**: FastAPI app served by Uvicorn
- **redis**: Redis key–value store used to count visits

## Prerequisites
- Docker Desktop (Windows/macOS/Linux)
- Docker Compose v2 (bundled with Docker Desktop)

## Quick Start

```bash
# Build and run (foreground)
docker compose up --build
# or run in background
docker compose up --build -d
