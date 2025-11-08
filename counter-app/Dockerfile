FROM python:3.11-slim

# create non-root user & writable dirs
RUN useradd -m -u 10001 appuser && \
    mkdir -p /app /logs && \
    chown -R appuser:appuser /app /logs

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

ENV PORT=8080
EXPOSE 8080

# drop root
USER appuser

CMD ["python", "app.py"]
