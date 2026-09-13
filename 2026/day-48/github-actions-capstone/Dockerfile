# Stage 1: Build dependencies
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Update Debian packages to latest security patches
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Stage 2: Minimal runtime image
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy Python libraries and app from builder
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /app /app

EXPOSE 5000

CMD ["app/app.py"]

