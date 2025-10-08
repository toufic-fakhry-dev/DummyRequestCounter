# Dummy Request Counter

A simple **FastAPI + Redis** app that counts how many times the root page (`/`) is visited.  
The app runs in **Docker containers** managed by **Docker Compose**.

---

## Features
- FastAPI backend (Uvicorn)
- Redis counter storage
- Dockerized with persistent Redis data
- Configurable via `.env`
- Endpoints: `/`, `/health`, `/docs`

---

## Project Structure
