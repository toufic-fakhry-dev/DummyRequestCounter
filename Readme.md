# DummyRequestCounter

A dummy FastAPI application that counts  the number of visits using Redis which is running in Docker Desktop containers.

I added a Docker volume (redis_data) to persist Redis data so it remains available even if the container restarts.

Additionally, a custom Docker network (backend) was created to manage communication between the FastAPI and Redis containers.

Using a dedicated network improves isolation, security, and maintainability so both services can communicate internally via their container names while remaining inaccessible from external systems.

This project is a simple FastAPI + Redis multi-container application that counts the number of times a web page is visited. It demonstrates Docker Compose orchestration, persistent storage, environment configuration, automated testing, and CI/CD workflows using GitHub Actions.

## Features
- **FastAPI backend** integrated with Redis for counting visits
- **Dockerized setup** using Docker Compose
- **Persistent Redis storage** using Docker volumes
- **Environment-based configuration** (e.g., Redis host and port)
- **Automated testing** using pytest
- **CI/CD pipeline** for build, test, and deployment to Docker Hub

## Project Structure

```
DummyRequestCounter/
│
├── app/
│   ├── main.py                # FastAPI application
│   └── __init__.py
│
├── tests/
│   ├── test_app.py           # Unit test for FastAPI endpoint
│   └── __init__.py
│
├── Dockerfile                # Image build instructions
├── docker-compose.yml        # Service orchestration
├── requirements.txt          # Python dependencies
├── .gitignore
└── .github/
		└── workflows/
				└── ci-cd.yml         # GitHub Actions workflow
```

## Setup and Installation

### 1. Clone the Repository
```sh
git clone https://github.com/toufic-fakhry-dev/DummyRequestCounter.git
cd DummyRequestCounter
```

### 2. Create and Activate Virtual Environment (optional)
```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Locally (Without Docker)
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Access the app at: [http://localhost:8000](http://localhost:8000)

## Running with Docker Compose

### Build and Start Containers
```sh
docker compose up --build
```

This command will:
- Build the FastAPI app image
- Pull and start the Redis image
- Launch both containers
- Mount a persistent volume for Redis data

### Stop and Remove Containers
```sh
docker compose down -v
```

## Testing

### Run Tests Locally
```sh
python -m pytest tests/ -v
```

### Example Test File (`tests/test_app.py`)
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
		response = client.get("/")
		assert response.status_code == 200
		assert response.json() == {"message": "Hello World"}

def test_count_endpoint():
		response = client.get("/count")
		assert response.status_code == 200
		data = response.json()
		assert "counter" in data
		assert isinstance(data["counter"], int)
```

## Environment Variables

| Variable     | Description      | Default |
|--------------|------------------|---------|
| REDIS_HOST   | Redis hostname   | redis   |
| REDIS_PORT   | Redis port       | 6379    |

These variables are defined in `docker-compose.yml` and can be modified as needed.

## Docker Compose Configuration

The web (FastAPI) and redis services are connected through a custom network named `backend`:

```yaml
networks:
	backend:
		driver: bridge
```

Redis data persistence is managed through a named volume:

```yaml
volumes:
	redis_data:
```

## GitHub Actions CI/CD Pipeline

The workflow file is located in `.github/workflows/ci-cd.yml`.
It automates the following steps:

### Continuous Integration (CI)
- Code quality checks and linting
- Unit and integration testing using pytest
- Building the Docker image to ensure it runs correctly

### Continuous Deployment (CD)
- Builds and pushes the Docker image to Docker Hub using GitHub Secrets:
	- `DOCKER_USERNAME`
	- `DOCKER_PASSWORD` (Docker Hub access token)

## Example API Response

**GET /**

```json
{"message": "Hello World"}
```

**GET /count**

```json
{"counter": 5}
```
