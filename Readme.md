# Simple Multi-Container Web Counter

This project demonstrates a simple web application consisting of two services:
1.  **web**: A Python FastAPI application that serves as a simple hit counter.
2.  **redis**: A Redis database used to persistently store the hit count.

## Getting Started

1.  **Prerequisites**: Ensure you have Docker and Docker Compose installed.
2.  **Clone the Repository** (already done).
3.  **Build and Run the Services**:
    ```bash
    docker compose up -d --build
    ```

## Testing the Application

The web service is exposed on `http://localhost:8000`.

To test the counter, use `curl`:

```bash
curl http://localhost:8000
# The hit count will increment with each request.