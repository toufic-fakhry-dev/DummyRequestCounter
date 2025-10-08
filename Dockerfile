# Use an official Python runtime as a base
FROM python:3.11-slim

# Create working directory inside the container
WORKDIR /code

# Copy dependency list and install
COPY requirements.txt /code/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the whole project into the container
COPY . /code

# Avoid output buffering
ENV PYTHONUNBUFFERED=1 

# Default port (can be overridden)
ENV APP_PORT=8000

# Run FastAPI with Uvicorn
# Important: module path is app.app:app (folder.file:FastAPI instance)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
