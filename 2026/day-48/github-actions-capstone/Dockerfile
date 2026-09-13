FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Update Debian packages to latest security patches
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 5000

CMD ["python", "app/app.py"]

