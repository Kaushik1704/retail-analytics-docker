# Base image
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src

# Expose API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
