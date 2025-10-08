# Dummy Request Counter

A simple FastAPI application that counts page visits using Redis as a backend store.

## Features

- FastAPI web framework
- Redis for persistent counter storage with data volume persistence
- Docker containerization with custom network isolation
- Environment variable configuration
- Multi-container setup with docker-compose

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

## Quick Start

1. Clone the repository:
```bash
git clone <your-repo-url>
cd DummyRequestCounter
```

2. Copy the environment file:
```bash
cp env.example .env
```

3. Build and run the containers:
```bash
docker-compose up --build -d
```

4. Test the API:
```bash
curl http://localhost:8000/
```

## Configuration

You can customize the application using environment variables:

- `REDIS_PORT`: Redis port (default: 6379)
- `APP_PORT`: Application port (default: 8000)

Create a `.env` file based on `env.example` to override these values.

### Docker Configuration

The application uses:
- **Custom Network**: Services communicate on a dedicated `app-network` for isolation
- **Data Persistence**: Redis data is persisted using a Docker volume (`redis_data`)
- **Service Discovery**: Services can reach each other using service names as hostnames

## API Endpoints

- `GET /`: Returns a greeting with the current visit count
- `GET /health`: Health check endpoint that verifies Redis connectivity

## Development

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Redis:
```bash
docker run -d -p 6379:6379 redis:7-alpine
```

3. Run the application:
```bash
uvicorn app.app:app --reload
```

### Docker Commands

- Start services: `docker-compose up -d`
- Stop services: `docker-compose down`
- View logs: `docker-compose logs -f`
- Rebuild: `docker-compose up --build`
- Remove volumes: `docker-compose down -v` (⚠️ This will delete Redis data)
- View networks: `docker network ls`
- Inspect custom network: `docker network inspect dummyrequestcounter_app-network`

## Project Structure

```
├── app/
│   ├── __init__.py
│   └── app.py          # FastAPI application
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-container orchestration
├── requirements.txt    # Python dependencies
├── env.example        # Environment variables template
└── README.md          # This file
```
