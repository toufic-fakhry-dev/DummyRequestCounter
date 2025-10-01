# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# (Optional) build tools for any deps that need compiling
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Run as non-root
RUN useradd -m appuser
USER appuser

# Copy app code
COPY . /app

EXPOSE 8000
CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port ${API_PORT:-8000}"]
