FROM gcr.io/distroless/python3-debian12
WORKDIR /app
COPY requirements.txt .
COPY app/ ./app/
EXPOSE 5000
CMD ["app/app.py"]

