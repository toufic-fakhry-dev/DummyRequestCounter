FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port (default)
EXPOSE 5000

# Allow override of host/port via env vars
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]

