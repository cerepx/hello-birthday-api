# 🎂 Hello Birthday API

[![CI - Test & Lint](https://github.com/cerepx/hello-birthday-api/actions/workflows/ci.yml/badge.svg)](https://github.com/cerepx/hello-birthday-api/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A simple birthday reminder API built with Flask, MySQL, and Docker — ready for containerized deployments in cloud-native environments.

---

## ✨ Features

- ✅ Save a user's date of birth via `PUT /hello/<username>`
- ✅ Get a birthday greeting via `GET /hello/<username>`
- ✅ Health check endpoint at `/health`
- 🐳 Dockerized with MySQL
- 🧪 Full Pytest test suite

---

## Tech Stack

- **Python 3.10**
- **Flask**
- **MySQL (via Docker for testing)**
- **Gunicorn (for production WSGI)**
- **Docker & Docker Compose**

---

## ⚙️ Prerequisites

To run or develop this project locally, make sure you have:

| Tool | Version | Purpose |
|------|---------|---------|
| [Docker](https://www.docker.com/) | ≥ 20.x | Run containerized app |
| [Docker Compose](https://docs.docker.com/compose/) | ≥ 1.29 | Start containers locally |
| [Python 3.10+](https://www.python.org/) | Optional | Local test execution |
| [Make](https://www.gnu.org/software/make/) | Optional | Simplify workflows |
| [curl](https://curl.se/) | Optional | Manual endpoint testing |

---

## Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/cerepx/hello-birthday-api.git
cd hello-birthday-api
```

### 2. Create your .env file

```bash
cp .env.example .env
```

**Environment Variables**:
   - MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
   - BASE_URL for tests

### 3. Start the app
   ```bash
   make up
   ```

### 4. Run the tests
   ```bash
   make test
   ```

---

## API Usage

1. **Save a user**:
   ```bash
   curl -X PUT http://localhost:5050/hello/Constantin -H "Content-Type: application/json" -d '{"dateOfBirth":"1985-04-16"}'
   ```

2. **Get a birthday message**:
   ```bash
   curl http://localhost:5050/hello/Constantin
   ```

---

## 🧪 Visual Test Logs

See real request/response examples and screenshots in the [📸 Live Demo Screenshots](docs/demo.md).

---

## 🏗️ Architecture Diagram

![Architecture Diagram](docs/architecture/cicd-hello-birthday-api.svg)

---

## License

This project is licensed under the MIT License.