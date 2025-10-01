# DummyRequestCounter

A simple FastAPI application that counts the number of visits using Redis, running in Docker containers.

## Features

- **FastAPI** - Modern Python web framework
- **Redis** - In-memory data store for visit counting
- **Docker** - Containerized deployment
- **Docker Compose** - Multi-container orchestration
- **Environment Variables** - Configurable settings

## Quick Start

```bash
# Clone and run
git clone <repository-url>
cd DummyRequestCounter
docker-compose up --build

# Access the application
curl http://localhost:8000

## Project Structure

DummyRequestCounter/
├── app/
│   └── app.py              # FastAPI application
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-service orchestration
├── requirements.txt        # Python dependencies
├── .env                    # Environment configuration
└── README.md              # Project documentation