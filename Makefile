.PHONY: build up down test logs lint

# Build the Docker images
build:
	docker-compose build

# Start the services
up:
	docker-compose up --build

# Stop all services
down:
	docker-compose down -v

# Run the tests inside the web container
test:
	docker-compose exec web pytest -v

# Show logs
logs:
	docker-compose logs -f

# Run linting (inside container)
lint:
	docker-compose exec web pylint app tests
