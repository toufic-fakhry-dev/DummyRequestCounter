# DummyRequestCounter – FastAPI + Redis with Docker Compose

## Part 1: Setting Up a Simple Multi-Container Application
(Already documented in earlier steps...)

## Part 2: Adding Persistent Storage and Networks
(Already documented in earlier steps...)

## Part 3: Troubleshooting and Debugging

### Step 1: Viewing container logs
To troubleshoot issues or monitor application output, use the following command to view logs from all containers:
```bash
docker compose logs -f
```
This will stream logs in real-time. To view logs from a specific service, e.g., the web app:
```bash
docker compose logs -f web
```
Expected output includes FastAPI startup messages and request logs:
```
web_1    | INFO:     Started server process [1]
web_1    | INFO:     Waiting for application startup.
web_1    | INFO:     Application startup complete.
web_1    | INFO:     127.0.0.1:12345 - "GET / HTTP/1.1" 200 OK
```

### Step 2: Executing commands inside containers
To interact directly with a running container, use `docker compose exec`.

- Access the web container’s shell:
```bash
docker compose exec web sh
```
Inside the container, you can run commands like:
```bash
python --version
pip list
```

- Access the Redis container:
```bash
docker compose exec redis redis-cli
```
Inside the Redis CLI, you can run commands such as:
```bash
PING
GET somekey
```
Expected Redis response for `PING`:
```
PONG
```

---

## Part 4: Cleaning Up Resources

### Step 1: Stop and remove containers and networks
To stop running containers and remove them along with the default network, run:
```bash
docker compose down
```
This removes containers and the network but preserves volumes.

### Step 2: Remove volumes to delete persistent data
To also remove named volumes (e.g., `redis-data`) and delete all persisted data, run:
```bash
docker compose down -v
```
Use this command with caution as it erases Redis data.

---

## Part 5: Version Control and Collaboration with GitHub

### Step 1: Create a new branch
Before making changes, create and switch to a new branch:
```bash
git checkout -b feature/your-feature-name
```

### Step 2: Stage and commit changes
Add modified files to staging:
```bash
git add .
```
Commit your changes with a meaningful message:
```bash
git commit -m "Add feature description or fix details"
```

### Step 3: Push the branch to GitHub
Push the branch to the remote repository:
```bash
git push origin feature/your-feature-name
```

### Step 4: Create a Pull Request
- Go to your GitHub repository in a web browser.
- You will see a prompt to create a Pull Request for your pushed branch.
- Click “Compare & pull request”.
- Add a descriptive title and detailed description of your changes.
- Submit the Pull Request for review and merging.

---

✅ With these steps, **Parts 1 through 5 are fully completed**.  
You now have a working FastAPI + Redis app containerized with Docker Compose, persistent storage, networking, debugging tools, clean-up commands, and version control workflows.
