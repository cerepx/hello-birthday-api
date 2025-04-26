FROM python:3.10-slim

LABEL org.opencontainers.image.title="hello-birthday-api"
LABEL org.opencontainers.image.description="A Flask-based API that stores user birthdays and returns personalized messages."
LABEL org.opencontainers.image.authors="Constantin Cirimpei <constantin.cirimpei@gmail.com>"

WORKDIR /app

# Install dependencies
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy all project files
COPY . .

# Disable log buffering
ENV PYTHONUNBUFFERED=1

# Expose app port
EXPOSE 5000

# Default 4 workers is a reasonable default for most small-to-medium apps
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:5000", "--workers", "${GUNICORN_WORKERS:-4}"]
