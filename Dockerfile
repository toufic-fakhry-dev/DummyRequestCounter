# Use official Python image
FROM python:3.9-slim

# Workdir inside container
WORKDIR /app

# Install deps (layer-cached)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI/Uvicorn port
EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
