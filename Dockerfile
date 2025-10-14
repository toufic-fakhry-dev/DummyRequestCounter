FROM python:3.10-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder
COPY app/ ./app

WORKDIR /app/app

EXPOSE 5000

CMD ["python", "app.py"]
