<<<<<<< HEAD
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
=======
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
>>>>>>> 526b8f3 (Save all local changes before pull)
