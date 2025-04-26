# Hello Birthday API

A simple API to save and retrieve user birthdays, built with Flask and MySQL.

---

## Features

- Save a user's date of birth via `PUT /hello/<username>`
- Get a birthday greeting via `GET /hello/<username>`
- Health check endpoint at `/health`
- Simple SQLite or MySQL backend
- Dockerized with MySQL and healthchecks
- Pytest test suite

---

## Tech Stack

- **Python 3.10**
- **Flask**
- **MySQL (via Docker for testing)**
- **Gunicorn (for production WSGI)**
- **Docker & Docker Compose**

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

## License

This project is licensed under the MIT License.