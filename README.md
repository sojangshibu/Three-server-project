# Three Backend Servers with Nginx Load Balancing

## Project Overview

This project demonstrates how to deploy a web application across three backend servers using Docker and configure Nginx as a load balancer to distribute incoming HTTP requests between them.

The application is built using Python Flask and runs inside separate Docker containers. Nginx acts as the entry point, forwarding client requests to the backend servers using the round-robin load-balancing algorithm.

## Objectives

- Deploy three independent backend application containers.
- Containerize the Flask application using Docker.
- Configure Nginx as a reverse proxy and load balancer.
- Distribute incoming HTTP requests across multiple backend servers.
- Test application health and verify load-balancing behavior.

## Technologies Used

- **AWS EC2** – Cloud deployment environment
- **Ubuntu Linux** – Server operating system
- **Docker** – Application containerization
- **Docker Compose** – Multi-container management
- **Nginx** – Reverse proxy and load balancer
- **Python Flask** – Backend web application
- **Git and GitHub** – Version control and project hosting

## Architecture

```text
                  Client / Web Browser
                          |
                          v
                  Nginx Load Balancer
                       Port 8080
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
          Backend 1   Backend 2   Backend 3
          Flask App   Flask App   Flask App
          Docker      Docker      Docker
```

## How It Works

1. The client sends an HTTP request to the Nginx load balancer.
2. Nginx forwards the request to one of the three backend containers.
3. The selected Flask application processes the request and returns a response identifying the backend server.
4. Nginx sends the response back to the client.
5. Docker Compose manages the backend containers and the load-balancer service.

By default, Nginx distributes requests using round-robin scheduling when no other balancing method is configured.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sojangshibu/Three-server-project.git
cd Three-server-project
```

### 2. Start the Containers

```bash
docker compose up -d --build
```

### 3. Verify Running Containers

```bash
docker compose ps
```

### 4. Access the Application

Open the following URL in your browser:

```text
http://YOUR_EC2_PUBLIC_IP:8080
```

Replace `YOUR_EC2_PUBLIC_IP` with your EC2 instance's public IPv4 address.

**AWS Security Group:** Allow inbound TCP traffic on port `8080` from your intended client IP addresses. Avoid opening application ports to the entire internet unless necessary.

### 5. Test Load Balancing

Refresh the application several times or send multiple requests to verify that responses come from different backend servers.

```bash
for i in {1..10}; do
  curl -s http://localhost:8080
  echo
done
```

The output should identify the backend handling each request. Actual distribution depends on the Nginx configuration and the availability of the backend containers.

## What I Learned

- Containerizing Python Flask applications using Docker.
- Managing multiple services with Docker Compose.
- Configuring Nginx upstream servers.
- Understanding reverse proxy and load-balancing concepts.
- Deploying applications on AWS EC2.
- Testing backend connectivity and request distribution.

## Project Repository

GitHub: [Three-server-project](https://github.com/sojangshibu/Three-server-project)

## Author

**Sojan Shibu**

GitHub: [@sojangshibu](https://github.com/sojangshibu)
