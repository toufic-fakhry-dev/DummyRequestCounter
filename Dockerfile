FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=app.app:app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=development \
    REDIS_HOST=redis \
    REDIS_PORT=6379

EXPOSE 8000

CMD ["flask", "--app", "app.app:app", "run", "--host=0.0.0.0", "--port=8000"]


