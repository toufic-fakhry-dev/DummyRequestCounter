# Dummy Request Counter

A simple FastAPI application that counts HTTP requests using Redis as a backend storage.

## Features

- **Request Counter**: Tracks the number of visits to the main endpoint
- **Health Check**: Endpoint to verify application status
- **Counter Management**: Get current count and reset functionality
- **Redis Integration**: Persistent storage using Redis
- **Docker Support**: Containerized application with Docker Compose
- **Environment Configuration**: Configurable through environment variables
- **Persistent Storage**: Redis data persists across container restarts
- **Custom Network**: Isolated network for secure service communication

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main page that increments and displays visit counter |
| GET | `/health` | Health check endpoint |
| GET | `/count` | Get current counter value |
| GET | `/reset` | Reset counter to zero |

## Quick Start

### Prerequisites

- Docker Desktop
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/toufic-fakhry-dev/DummyRequestCounter
   cd DummyRequestCounter
   ```

2. **Create environment file** (optional)
   ```bash
   cp .env.example .env
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Test the application**
   ```bash
   curl http://localhost:8000/health
   ```

## Configuration

The application can be configured using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `WEB_PORT` | `8000` | External port for the web service |
| `ENV` | `development` | Environment (development/production) |
| `REDIS_HOST` | `redis` | Redis hostname |
| `REDIS_PORT` | `6379` | Redis port |
| `REDIS_DB` | `0` | Redis database number |
| `REDIS_PASSWORD` | `` | Redis password (if authentication needed) |

### Custom Configuration

Create a `.env` file in the project root:

```env
WEB_PORT=8080
REDIS_PORT=6380
ENV=production
```

## Architecture

### Docker Infrastructure

- **Custom Network**: `dummycounter-network` - Isolated bridge network for secure communication
- **Persistent Storage**: Named volume `redis_data` for Redis data persistence
- **Service Discovery**: Containers communicate using service names (`web`, `redis`)

### Project Structure

```
DummyRequestCounter/
├── app/
│   └── app.py              # FastAPI application
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Docker image configuration
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── .env                   # Local environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Usage Examples

### Basic Usage

```bash
# Start the application
docker-compose up -d

# Visit the main page (increments counter)
curl http://localhost:8000/
# Response: {"message":"Hello! This page has been visited 1 times."}

# Get current count
curl http://localhost:8000/count
# Response: {"count":1}

# Reset counter
curl http://localhost:8000/reset
# Response: {"message":"Counter reset","count":0}

# Health check
curl http://localhost:8000/health
# Response: {"status":"healthy"}
```

### Testing Data Persistence

```bash
# Add some data
curl http://localhost:8000/
curl http://localhost:8000/

# Check count
curl http://localhost:8000/count
# Response: {"count":2}

# Restart containers
docker-compose down
docker-compose up -d

# Check count again - data persists!
curl http://localhost:8000/count
# Response: {"count":2}
```

### Using PowerShell (Windows)

```powershell
# Test endpoints
Invoke-RestMethod -Uri "http://localhost:8000/health"
Invoke-RestMethod -Uri "http://localhost:8000/"
Invoke-RestMethod -Uri "http://localhost:8000/count"
Invoke-RestMethod -Uri "http://localhost:8000/reset"
```

## Development

### Running Locally (Development)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Redis** (using Docker)
   ```bash
   docker run -d -p 6379:6379 redis:7-alpine
   ```

3. **Set environment variables**
   ```bash
   set REDIS_HOST=localhost
   ```

4. **Run the application**
   ```bash
   uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
   ```

### Docker Commands

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs
docker-compose logs web
docker-compose logs redis

# Stop services
docker-compose down

# Stop and remove volumes (data will be lost)
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# View running containers
docker-compose ps

# Execute commands in containers
docker-compose exec web bash
docker-compose exec redis redis-cli

# Test network connectivity
docker-compose exec web ping redis
```

### Network and Storage Management

```bash
# List Docker networks
docker network ls

# Inspect the custom network
docker network inspect dummycounter-network

# List Docker volumes
docker volume ls

# Inspect Redis data volume
docker volume inspect dummyrequestcounter_redis_data

# Backup Redis data
docker-compose exec redis redis-cli BGSAVE
```

## Troubleshooting

### Common Issues

1. **Port 8000 already in use**
   ```bash
   # Change port in .env file
   WEB_PORT=8080
   ```

2. **Containers not starting**
   ```bash
   # Check Docker Desktop is running
   # View logs for errors
   docker-compose logs
   ```

3. **Redis connection issues**
   ```bash
   # Check Redis container status
   docker-compose logs redis
   
   # Test Redis connectivity
   docker-compose exec web ping redis
   ```

4. **Application restarting continuously**
   ```bash
   # Check application logs
   docker-compose logs web
   ```

5. **Data not persisting**
   ```bash
   # Verify volume is mounted
   docker-compose exec redis ls -la /data
   
   # Check Redis persistence is enabled
   docker-compose exec redis redis-cli CONFIG GET save
   ```

### Health Checks

- Web application: `http://localhost:8000/health`
- Redis: `docker-compose exec redis redis-cli ping`
- Network connectivity: `docker-compose exec web ping redis`

## Technologies Used

- **FastAPI**: Modern, fast web framework for Python
- **Redis**: In-memory data structure store with persistence
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container Docker applications
- **Uvicorn**: ASGI web server

## License

This project is for educational purposes.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request