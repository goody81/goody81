FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Set Python path
ENV PYTHONPATH=/app/src

# Default command
ENTRYPOINT ["python", "/app/src/main.py"]
CMD ["--help"]
