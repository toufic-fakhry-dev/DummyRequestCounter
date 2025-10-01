## Step-by-Step Lab Checklist

### Part 1: Setting Up the Multi-Container Application

```bash
# Clone repository
git clone <repository-url>
cd DummyRequestCounter

# Optional: update .gitignore (ignore __pycache__, .env, etc.)
# Edit Dockerfile and requirements.txt as needed for FastAPI

# Build and start containers
docker-compose up -d --build

# Verify containers are running
docker-compose ps

# Test API endpoints
curl http://localhost:8000/
curl http://localhost:8000/count
# or open FastAPI docs: http://localhost:8000/docs
```

### Part 2: Adding Persistent Storage and Networks

```bash
# Edit docker-compose.yml:
# - Add a volume for Redis data:
#   volumes:
#     redis_data:
# - Add a custom network:
#   networks:
#     app_network:

# Restart containers to apply changes
docker-compose down
docker-compose up -d --build

# Verify containers and network
docker-compose ps
docker network ls
```

### Part 3: Troubleshooting and Debugging

```bash
# View logs
docker-compose logs -f

# Execute commands inside the web container
docker-compose exec web sh

# Navigate to app folder
cd app

# Start Python REPL
python
>>> from main import get_count
>>> get_count()   # increment counter
>>> get_count()
>>> exit()

# Test Redis connectivity from container
redis-cli -h redis ping  # should return PONG

# Test API endpoints from container or host
curl http://localhost:8000/
curl http://localhost:8000/count

# Exit container shell
exit
```

### Part 4: Clean-Up

```bash
# Stop and remove containers
docker-compose down

# Remove volumes and networks
docker-compose down -v

# Verify cleanup
docker ps -a
docker volume ls
docker network ls
```

### Part 5: Multiple Web Instances and Pull Request

```bash
# Push branch to GitHub
git checkout lab2-ElieRhayem
git add .
git commit -m "Complete TP2 Lab: FastAPI + Redis setup"
git push origin dev
```
