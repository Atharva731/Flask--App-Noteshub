# NotesHub 📝

NotesHub is a simple **Flask-based Notes Management Web Application** with **MySQL** as the database.

The application is containerized using **Docker** and **Docker Compose** and can be deployed using a **Jenkins CI/CD pipeline**.

---

## 🚀 Project Overview

NotesHub allows users to manage their notes through a web interface while storing application data in a MySQL database.

The project demonstrates a basic **two-tier application architecture**:

```text
                    User
                     │
                     ▼
              ┌─────────────┐
              │  Flask App  │
              │  Container  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │    MySQL    │
              │  Container  │
              └─────────────┘
```

---

## ✨ Features

* Create and manage notes
* Flask web application
* MySQL database integration
* HTML/CSS frontend
* Dockerized application
* Docker Compose for application + database
* Persistent MySQL data using Docker volumes
* Jenkins pipeline for Docker build and deployment
* Deployable on AWS EC2

---

## 🛠️ Technologies Used

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python 3.12    | Application runtime        |
| Flask          | Web framework              |
| MySQL 8        | Database                   |
| Flask-MySQLdb  | Flask/MySQL integration    |
| mysqlclient    | MySQL Python driver        |
| HTML/CSS       | Frontend                   |
| Docker         | Containerization           |
| Docker Compose | Multi-container deployment |
| Jenkins        | CI/CD                      |
| Git            | Version control            |
| GitHub         | Source code management     |
| AWS EC2        | Deployment environment     |

---

## 📁 Project Structure

```text
Flask--App-Noteshub/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── README.md
├── .gitignore
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
└── tests/
    └── ...
```

### Important Files

**`app.py`**
Main Flask application.

**`requirements.txt`**
Contains the Python dependencies required by the application.

**`Dockerfile`**
Defines how the Flask application Docker image is built.

**`docker-compose.yml`**
Defines and runs the Flask application and MySQL database containers.

**`Jenkinsfile`**
Defines the Jenkins CI/CD pipeline for building the Docker image and deploying the application.

---

# 💻 Running the Application Locally

## Prerequisites

Make sure the following are installed:

* Git
* Python 3.12+
* MySQL

### 1. Clone the repository

```bash
git clone https://github.com/Atharva731/Flask--App-Noteshub.git
```

```bash
cd Flask--App-Noteshub
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project currently uses Flask, Flask-MySQLdb, mysqlclient, and Pytest.

### 4. Configure MySQL

Create the NotesHub database in MySQL:

```sql
CREATE DATABASE noteshub;
```

Configure the MySQL connection according to your local environment.

### 5. Run the application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

# 🐳 Running with Docker Compose

Docker Compose is the easiest way to run the complete application because it starts both the Flask application and MySQL database.

### 1. Clone the repository

```bash
git clone https://github.com/Atharva731/Flask--App-Noteshub.git
```

```bash
cd Flask--App-Noteshub
```

### 2. Build and start the application

```bash
docker compose up -d --build
```

### 3. Check the containers

```bash
docker compose ps
```

You should have two services running:

```text
app
mysql
```

### 4. Open the application

```text
http://localhost:5000
```

The current Compose configuration maps port `5000` from the container to port `5000` on the host.

### 5. View application logs

```bash
docker compose logs -f app
```

### 6. Stop the application

```bash
docker compose down
```

---

# 🐳 Docker Architecture

The Docker setup contains two services:

```text
                 Docker Compose
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   ┌─────────────┐           ┌─────────────┐
   │     app     │           │    mysql    │
   │   Flask     │──────────▶│   MySQL 8   │
   │   Port 5000 │           │             │
   └─────────────┘           └──────┬──────┘
                                    │
                                    ▼
                              mysql-data
                               volume
```

The MySQL service uses a Docker volume named `mysql-data` so database data can persist beyond the lifetime of the container.

---

# 🔄 Jenkins CI/CD

This project includes a Jenkins pipeline for automated Docker-based deployment.

The **current Jenkinsfile contains two stages**:

```text
GitHub
   │
   ▼
 Jenkins
   │
   ▼
Docker Build
   │
   ▼
Docker Compose Deploy
```

## Pipeline Stages

### 1. Docker Build

Jenkins builds the NotesHub Docker image:

```bash
docker build -t noteshub:latest .
```

### 2. Deploy

Jenkins stops the existing Compose deployment:

```bash
docker compose down || true
```

Then starts the application:

```bash
docker compose up -d
```

These are the stages currently defined in the repository's Jenkinsfile.

> **Note:** The current Jenkins pipeline does **not** contain a separate testing stage. The repository does contain a `tests/` directory, but Jenkins currently focuses on Docker image building and deployment.

---

# ☁️ AWS EC2 Deployment

The application can be deployed on an **AWS EC2 Ubuntu instance** with Docker, Docker Compose, and Jenkins installed.

The deployment workflow is:

```text
Developer
    │
    ▼
  GitHub
    │
    ▼
  Jenkins
    │
    ▼
Docker Build
    │
    ▼
Docker Compose
    │
    ├──────────────┐
    ▼              ▼
 Flask App       MySQL
 Container      Container
    │
    ▼
Application
```

After deployment, the application can be accessed through the EC2 public IP:

```text
http://<EC2-PUBLIC-IP>:5000
```

Make sure the EC2 security group allows inbound traffic on port `5000` if you are accessing the application directly through that port.

---

# 🔧 Dockerfile

The application uses:

```dockerfile
FROM python:3.12-slim
```

The Docker image installs the required MySQL client development packages and build tools needed by the Python MySQL dependencies.

The image then:

1. Sets `/app` as the working directory
2. Installs Python dependencies
3. Copies the application source code
4. Exposes port `5000`
5. Starts the Flask application

---

# 📦 Python Dependencies

The current `requirements.txt` contains:

```text
Flask==3.1.3
Flask-MySQLdb==2.0.0
mysqlclient==2.2.8
pytest
```

These dependencies provide the Flask framework, MySQL integration, MySQL client library, and testing framework.

---

# 🧪 Testing

The repository contains a `tests/` directory and includes **Pytest** as a project dependency.

Tests can be run manually with:

```bash
pytest
```

or:

```bash
python -m pytest
```

### Current CI/CD status

At the moment, **Jenkins does not automatically execute the tests**.

The current Jenkins pipeline is:

```text
Checkout
   ↓
Docker Build
   ↓
Deploy
```

The test files remain available in the repository for manual testing and can be integrated into Jenkins later.

---

# 📚 What This Project Demonstrates

This project provides practical experience with:

* Flask application development
* MySQL database integration
* Git and GitHub
* Linux
* Docker
* Docker Compose
* Jenkins
* CI/CD concepts
* Containerized deployment
* AWS EC2
* Application and database containers
* Basic DevOps workflow

---

# 🔄 Complete Project Workflow

```text
Write / Modify Application
          │
          ▼
       Git Commit
          │
          ▼
       GitHub
          │
          ▼
       Jenkins
          │
          ▼
     Docker Build
          │
          ▼
 Docker Compose Deploy
          │
     ┌────┴────┐
     ▼         ▼
 Flask App   MySQL
     │
     ▼
  Users
```

---

## 👨‍💻 Author

**Atharva K**

GitHub:
https://github.com/Atharva731

---

## 📌 Project Status

**Completed**

The project currently demonstrates a Flask + MySQL application running with Docker Compose and a Jenkins pipeline for Docker build and deployment.

---

## 📄 License

This project is created for **learning and educational purposes**.
