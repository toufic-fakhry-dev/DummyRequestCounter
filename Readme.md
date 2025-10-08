# DummyRequestCounter

A simple FastAPI application that counts page visits using Redis.  
This project is containerized with Docker and orchestrated using Docker Compose.

---

## 📦 Requirements

- Docker
- Docker Compose

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/toufic-fakhry-dev/DummyRequestCounter.git
cd DummyRequestCounter

2. Build and start the containers
docker-compose up --build

This starts:
FastAPI app at http://localhost:8000
Redis running internally on port 6379

Configuration

The app uses environment variables defined in docker-compose.yml.

Variable	Default	Description
WEB_PORT	8000	Port for FastAPI container
REDIS_HOST	redis	Redis service hostname
REDIS_PORT	6379	Redis port

Example: run on custom ports

WEB_PORT=9000 REDIS_PORT=6380 docker-compose up --build

Testing the API
Root endpoint
curl http://localhost:8000/

Expected output:

Hello! This page has been visited X times.

Interactive API docs

FastAPI automatically generates Swagger UI:

http://localhost:8000/docs

http://localhost:8000/redoc

Stopping Containers

Press CTRL+C or run:

docker-compose down
```

## 💾 Persistent Storage & Networking

### Redis Data Persistence

The Redis service now uses a named Docker volume to persist data across container restarts.

Defined in `docker-compose.yml`:

```yaml
volumes:
  redis_data:

Data is stored inside this volume and mounted to /data in the Redis container.

You can list volumes with:

docker volume ls

Custom Network

Both services communicate through a custom bridge network called appnet.

Defined in docker-compose.yml:

networks:
  appnet:
    driver: bridge


Inspect it:

docker network inspect dummyrequestcounter_appnet

🔄 Rebuild & Run
docker-compose down
docker-compose up --build


Redis data will now persist even after docker-compose down (unless you use --volumes to delete it).
```

---

## 🧰 Part 3 — Troubleshooting & Debugging with Docker Compose

### View Logs

To view logs from all containers:

```bash
docker compose logs
To stream logs continuously:

bash
Copy code
docker compose logs -f
To view logs for a specific service (replace names if different):

bash
Copy code
docker compose logs web
docker compose logs redis
Run Commands Inside Containers
Open a shell inside the FastAPI container:

bash
Copy code
docker compose exec web sh
Check environment variables or Python version:

bash
Copy code
python --version
env
Open Redis CLI to inspect data:

bash
Copy code
docker compose exec redis redis-cli
GET hits
If GET hits returns (nil), open http://localhost:8000/ once to increment the counter, then try again.

```
---

## 🧹 Part 4 — Clean-Up

To stop and remove all running containers:
```bash
docker compose down
To remove containers and persistent data volumes:

bash
Copy code
docker compose down -v
To remove any unused networks or volumes globally:

bash
Copy code
docker network prune
docker volume prune
⚠️ Be careful with prune — it deletes all unused Docker resources on your system.


⚖️ Part 5 – Multiple Web Instances (Scaling)

Since we use ports configuration in our docker-compose.yml, each FastAPI instance is automatically mapped to a unique port on your host machine.

After scaling with:


docker compose up --scale web=3 -d
Run:


docker compose ps
You'll see output like:


dummyrequestcounter-web-1   running   0.0.0.0:57578->8000/tcp
dummyrequestcounter-web-2   running   0.0.0.0:57579->8000/tcp  
dummyrequestcounter-web-3   running   0.0.0.0:57580->8000/tcp
dummyrequestcounter-redis-1 running   0.0.0.0:6379->6379/tcp
Now you can access all instances:

http://localhost:57578

http://localhost:57579

http://localhost:57580

Alternative: Using expose
During development, I also experimented with expose instead of ports. The key differences:

expose: Only exposes ports to other Docker containers (internal networking)

ports: Publishes ports to the host machine (external access)

With expose, you would need a load balancer (like nginx) or use docker compose port command to access the services from outside Docker.

Why we use ports in this project:

Allows direct access to each scaled instance from the host

Easier testing and demonstration

No additional load balancer configuration needed

🧠 Notes
Each scaled instance shares the same Redis database, so visit counts are synchronized between instances. Docker automatically load-balances internal requests across containers.

🧹 Clean Exit
When done:


docker compose down -v