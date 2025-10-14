# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

# Faster, cleaner Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install deps
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copy source
COPY . .

# App port (matches compose later)
EXPOSE 8000

# Run FastAPI (expects app/main.py with `app`)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
