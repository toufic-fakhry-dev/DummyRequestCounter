# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Faster/cleaner Python logs & no .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app source
COPY app/ ./app/

# Expose API port inside the container
EXPOSE 8000

# Launch FastAPI with Uvicorn
# If your entrypoint is not app/main.py with `app`, adjust the module path accordingly.
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
