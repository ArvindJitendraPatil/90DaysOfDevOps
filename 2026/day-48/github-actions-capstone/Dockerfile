FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Update Debian packages to latest security patches
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

EXPOSE 5000

CMD ["python", "app/app.py"]

