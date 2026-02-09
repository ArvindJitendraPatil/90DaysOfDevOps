
Step 1: Launch EC2 Instance
1. Open AWS Console → EC2 → Launch Instance
2. Select Ubuntu Server 22.04 LTS
3. Select t2.micro (Free Tier)
4. Create or select key pair
5. Allow ports: SSH (22) and HTTP (80)
6. Launch instance
Step 2: Connect via SSH
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
Step 3: Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
newgrp docker
Step 4: Create Project Folder
mkdir my-nginx-site
cd my-nginx-site
Step 5: Create HTML File using vi
vi index.html
Press i to enter insert mode and paste:
<!DOCTYPE html>
<html>
<head>
<title>Docker Nginx EC2</title>
</head>
<body>
<h1>Success! Docker Nginx running on EC2</h1>
<p>This page is served from Docker container.</p>
</body>
</html>
Save and exit vi:
Press ESC
Type :wq
Press Enter
Step 6: Create Dockerfile using vi
vi Dockerfile
Paste this Dockerfile:
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
Save and exit vi:
Press ESC
Type :wq
Press Enter
Step 7: Build Docker Image
docker build -t my-nginx .
Step 8: Run Docker Container
docker run -d -p 80:80 --name nginx-container my-nginx
Step 9: Verify Running Container
docker ps
Step 10: Access Website
Open browser and go to:
http://YOUR_PUBLIC_IP
Step 11: Save Logs to nginx-logs.txt
docker logs nginx-container > nginx-logs.txt
Step 12: View Logs using vi
vi nginx-logs.txt
