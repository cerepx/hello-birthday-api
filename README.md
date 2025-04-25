# Hello Birthday API

A simple API to save and retrieve user birthdays, built with Flask and SQLite.

---

## Features

- Save a user's date of birth via `PUT /hello/<username>`
- Get a birthday greeting via `GET /hello/<username>`
- Health check endpoint at `/health`
- Simple SQLite or MySQL backend
- Ready for Docker and production (via Gunicorn)

---

## Requirements

- Python 3.10+
- pip (Python package installer)
- MySQL (or SQLite for quick testing)

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/cerepx/hello-birthday-api.git
cd hello-birthday-api
pip install -r requirements.txt
```

---

## Run Locally

Follow these steps to run the project locally:

1. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Run the Application**:
   ```bash
   python app/main.py
   ```

4. **Access the API**:
   The API will be available at `http://localhost:5050`.

---

## Run Tests

To run the test suite:

1. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run Tests with `pytest`**:
   ```bash
   pytest
   ```
