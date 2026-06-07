# Day 37 – Docker Revision & Cheat Sheet

## Self Assessment Checklist

| Topic | Status |
|---------|---------|
| Run a container from Docker Hub | ✅ Can Do |
| List, stop, remove containers and images | ✅ Can Do |
| Explain image layers and caching | ✅ Can Do |
| Write Dockerfile from scratch | ✅ Can Do |
| Explain CMD vs ENTRYPOINT | ✅ Can Do |
| Build and tag custom image | ✅ Can Do |
| Create and use named volumes | ✅ Can Do |
| Use bind mounts | ✅ Can Do |
| Create custom networks | ✅ Can Do |
| Write docker-compose.yml | ✅ Can Do |
| Use .env files in Compose | ✅ Can Do |
| Write multi-stage Dockerfile | ✅ Can Do |
| Push image to Docker Hub | ✅ Can Do |
| Use healthchecks and depends_on | ✅ Can Do |

---

## Quick-Fire Questions

### 1. Difference between Image and Container?

An image is a read-only blueprint used to create containers.

A container is a running instance of an image.

---

### 2. What happens to data when a container is removed?

Container data is lost unless stored in a volume or bind mount.

---

### 3. How do containers communicate on the same network?

Using container names as hostnames through Docker DNS.

Example:

```bash
ping database
```

---

### 4. Difference between:

```bash
docker compose down
```

and

```bash
docker compose down -v
```

down:
Removes containers and networks.

down -v:
Removes containers, networks, and volumes.

---

### 5. Why use Multi-Stage Builds?

- Smaller image size
- Better security
- Faster deployments
- Removes unnecessary build tools

---

### 6. Difference between COPY and ADD?

COPY:
Copies files/directories only.

ADD:
Copies files and can extract archives or download URLs.

COPY is preferred in most cases.

---

### 7. What does:

```bash
-p 8080:80
```

mean?

Maps:

Host Port = 8080

Container Port = 80

Access application:

```bash
http://localhost:8080
```

---

### 8. Check Docker Disk Usage

```bash
docker system df
```

---

## Docker Concepts Revision

### Image Layers

Docker images are built using layers.

Each instruction creates a new layer.

Docker reuses unchanged layers to speed up builds.

---

### CMD vs ENTRYPOINT

CMD:
Default command that can be overridden.

ENTRYPOINT:
Fixed executable that always runs.

Example:

```Dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Runs:

```bash
python app.py
```

---

## Revisited Topics

### Topic 1: Multi-Stage Builds

Benefits:

- Small image size
- Production ready
- Better security

Example:

```Dockerfile
FROM node:18 AS builder

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html
```

---

### Topic 2: Docker Compose

Benefits:

- Manage multiple containers
- Single command deployment
- Environment management

Example:

```yaml
services:
  web:
    image: nginx

  db:
    image: postgres
```

Start:

```bash
docker compose up -d
```

---

## Day 37 Summary

Today I revised Docker fundamentals from Days 29–36 including:

- Containers
- Images
- Dockerfile
- Volumes
- Networks
- Docker Compose
- Multi-Stage Builds
- Docker Hub
- Healthchecks
