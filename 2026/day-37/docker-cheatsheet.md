# Docker Cheat Sheet 🚀

## Container Commands

| Command | Description |
|----------|-------------|
| docker run nginx | Run container |
| docker run -d nginx | Run in detached mode |
| docker run -it ubuntu bash | Interactive container |
| docker ps | Running containers |
| docker ps -a | All containers |
| docker stop <container_id> | Stop container |
| docker start <container_id> | Start container |
| docker restart <container_id> | Restart container |
| docker rm <container_id> | Remove container |
| docker exec -it <container_id> bash | Access container shell |
| docker logs <container_id> | View logs |

---

## Image Commands

| Command | Description |
|----------|-------------|
| docker pull nginx | Download image |
| docker images | List images |
| docker build -t myapp:v1 . | Build image |
| docker tag myapp:v1 username/myapp:v1 | Tag image |
| docker push username/myapp:v1 | Push image |
| docker rmi <image_id> | Remove image |

---

## Volume Commands

| Command | Description |
|----------|-------------|
| docker volume create myvolume | Create volume |
| docker volume ls | List volumes |
| docker volume inspect myvolume | Volume details |
| docker volume rm myvolume | Remove volume |

---

## Network Commands

| Command | Description |
|----------|-------------|
| docker network create mynetwork | Create network |
| docker network ls | List networks |
| docker network inspect mynetwork | Inspect network |
| docker network connect mynetwork container1 | Connect container |

---

## Docker Compose Commands

| Command | Description |
|----------|-------------|
| docker compose up | Start services |
| docker compose up -d | Detached mode |
| docker compose down | Stop services |
| docker compose down -v | Remove volumes too |
| docker compose ps | List services |
| docker compose logs | Show logs |
| docker compose build | Build services |

---

## Cleanup Commands

| Command | Description |
|----------|-------------|
| docker system df | Disk usage |
| docker container prune | Remove stopped containers |
| docker image prune | Remove unused images |
| docker volume prune | Remove unused volumes |
| docker network prune | Remove unused networks |
| docker system prune -a | Clean everything |

---

## Dockerfile Instructions

| Instruction | Purpose |
|-------------|---------|
| FROM | Base image |
| RUN | Execute commands |
| COPY | Copy files |
| ADD | Copy files & URLs |
| WORKDIR | Set working directory |
| EXPOSE | Open port |
| ENV | Environment variable |
| CMD | Default command |
| ENTRYPOINT | Fixed executable |
| USER | Run as specific user |

---

## Common Examples

### Port Mapping

```bash
docker run -p 8080:80 nginx
```

Host Port = 8080

Container Port = 80

---

### Volume Mount

```bash
docker run -v myvolume:/data nginx
```

---

### Bind Mount

```bash
docker run -v $(pwd):/app nginx
```

---

### Custom Network

```bash
docker network create devops-net
docker run -d --network devops-net --name app1 nginx
docker run -d --network devops-net --name app2 nginx
```

Containers can communicate using container names.

---
