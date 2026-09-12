
# GitHub Actions Capstone

A simple Flask application designed to demonstrate Docker containerization, automated testing, and GitHub Actions CI/CD.

## Project Overview

This project contains a lightweight Python Flask application with:

* Flask web application
* `/` application endpoint
* `/health` health-check endpoint
* Docker containerization
* Basic shell-based health test
* GitHub Actions CI/CD integration

## Project Structure

```text
github-actions-capstone/
├── app/
│   └── app.py
├── tests/
│   └── test_health.sh
├── Dockerfile
├── requirements.txt
└── README.md
```

## Application Endpoints

### Home

```text
GET /
```

Returns:

```text
GitHub Actions Capstone App is running!
```

### Health Check

```text
GET /health
```

Returns:

```json
{
  "status": "healthy"
}
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/arvindjitendrapatil/github-actions-capstone.git
cd github-actions-capstone
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app/app.py
```

Test the health endpoint:

```bash
curl http://localhost:5000/health
```

## Run with Docker

Build the Docker image:

```bash
docker build -t github-actions-capstone .
```

Run the container:

```bash
docker run -d --name github-actions-capstone -p 5000:5000 github-actions-capstone
```

Test the application:

```bash
curl http://localhost:5000/health
```

## Run Tests

Make sure the application is running and execute:

```bash
./tests/test_health.sh
```

Expected output:

```text
Checking application health...
Health check passed!
```

## Technologies Used

* Python
* Flask
* Docker
* Linux
* Bash
* Git
* GitHub
* GitHub Actions

## Future CI/CD

The next phase of this project will use GitHub Actions to:

1. Trigger workflows on code changes.
2. Install dependencies.
3. Run application tests.
4. Build the Docker image.
5. Validate the Docker image.
6. Push the image to a container registry.
7. Deploy the application.

Day 48 PR Pipeline Test
