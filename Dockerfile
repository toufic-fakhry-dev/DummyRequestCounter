FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1
 
WORKDIR /app
 
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app

EXPOSE 8000
 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]


