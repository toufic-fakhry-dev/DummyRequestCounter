# DummyRequestCounter

A dummy FastAPI application that counts  the number of visits using Redis which is running in Docker Desktop containers.

I added a Docker volume (redis_data) to persist Redis data so it remains available even if the container restarts.

Additionally, a custom Docker network (backend) was created to manage communication between the FastAPI and Redis containers.

Using a dedicated network improves isolation, security, and maintainability so both services can communicate internally via their container names while remaining inaccessible from external systems.