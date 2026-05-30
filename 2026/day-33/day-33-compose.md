# Day 33 – Docker Compose: Multi-Container Basics

## Task 1: Install & Verify
1. Check if Docker Compose is available on your machine
2. Verify the version

![image](images/task1.png)
    
---

## Task 2: Your First Compose File
1. Create a folder `compose-basics`
![image](images/task2.2.png)
2. Write a `docker-compose.yml` that runs a single **Nginx** container with port mapping
3. Start it with `docker compose up`
4. Access it in your browser
![image](images/task2.1.png)
5. Stop it with `docker compose down`
   
---

## Task 3: Two-Container Setup
Write a `docker-compose.yml` that runs:
- A **WordPress** container
- A **MySQL** container
![image](images/task3.1.png)
![image](images/task3.2.png)

![image](images/task3.6.png)

They should:
- Be on the same network (Compose does this automatically)
![image](images/task3.3.png)
![image](images/task3.4.2.png)
![image](images/task3.5.png)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name
![image](images/task3.7.png)
![image](images/task3.8.png)
![image](images/task3.9.png)
      
Start it, access WordPress in your browser, and set it up.
  
**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?
   
---

## Task 4: Compose Commands
Practice and document these:

1. Start services in **detached mode**
![image](images/task4.1.png) 
   
2. View running services
![image](images/task4.2.png)
   
3. View **logs** of all services

![image](images/task4.3.png)
   
   
4. View logs of a **specific** service
 
![image](images/task4.4.png)

5. **Stop** services without removing

![image](images/task4.5.png)  
   
6. **Remove** everything (containers, networks)

![image](images/task4.6.png)
  
7. **Rebuild** images if you make a change

![image](images/task4.7.png)
![image](images/task4.8.png) 

---

## Task 5: Environment Variables
1. Add environment variables directly in your `docker-compose.yml`
![image](images/task5.1.png)
![image](images/task5.2.png)
2. Create a `.env` file and reference variables from it in your compose file
3. Verify the variables are being picked up
![image](images/task5.3.png)
![image](images/task5.4.png) 
   
---
