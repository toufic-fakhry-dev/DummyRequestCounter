# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app
# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

