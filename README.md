# Task Manager API

A **Task Management API** built with **FastAPI** using a **layered architecture**, **SQLAlchemy** for database operations, and **Redis** for caching. This project demonstrates a clean separation of concerns, maintainable code structure, and scalable design with async/await patterns, environment-based configuration, and Docker deployment.

---

## Table of Contents
- Architecture
- Performance Optimizations
- Environment Configuration
- Requirements
- Local Setup
- Docker Setup
- Running the Application
- Load Testing
- Additional Notes

---

## Architecture

The API is designed using a **layered architecture**, which separates responsibilities into different layers:

1. **Controller** – Handles incoming HTTP requests and responses, validation, and delegates business logic to services.
2. **Service** – Contains the core business logic and orchestrates operations between repositories and other utilities.
3. **DTO (Data Transfer Object)** – Defines the shape of data that flows between layers, ensuring type safety and validation separate from the database model.
4. **Repository** – Handles direct interaction with the database via SQLAlchemy, encapsulating CRUD operations.
5. **Model** – Defines SQLAlchemy models corresponding to database tables.
6. **Data** – Contains tasks.json for initial database population.
7. **Config** – Manages database connection, environment variables, and dependency injection for using same service but different db instance.
8. **Utils** – Contains helper scripts like `clean_tasks` and `seed_data` for database operations or maintenance tasks.

**Why Layered Architecture?**
- **Separation of concerns:** Each layer has a single responsibility.
- **Maintainability:** Easier to modify or extend individual layers without affecting others.
- **Testability:** Layers can be tested independently.
- **Scalability:** Supports larger applications and teams by clearly separating responsibilities.

---

## Performance Optimizations

### Async/Await Implementation
The entire application has been converted to async architecture, enabling non-blocking I/O operations through the event loop. This allows the application to handle multiple concurrent requests efficiently.

### Redis Caching Layer
Redis has been integrated as a caching layer to reduce database load:
- Query results are cached in Redis before hitting the database
- Cache TTL (Time-To-Live) is configured per operation
- Automatic cache invalidation on create/update/delete operations
- Significant latency reduction for read-heavy workloads

### Multi-Worker Configuration
The application uses **Gunicorn** with **21 workers** (CPU Core × 2 + 1) to handle concurrent requests:
- **Formula:** `workers = (CPU cores × 2) + 1`
- On a 10-core system: 21 workers
- Each worker can handle multiple async requests via Uvicorn

### Database Connection Pooling
PostgreSQL connection pool is optimized for production:
- **Pool Size:** 4 connections per worker
- **Overflow:** 5 additional connections
- **Total Capacity:** ~189 concurrent database connections (9 × 21 workers)
- **PostgreSQL Config:** `max_connections` set to 200 for 2-4 GB RAM systems

### Load Testing Results
Using **Locust** load testing with 100 concurrent users:
- **100 GET requests + 100 POST requests:** 99% success rate
- **Horizontal Scaling:** Ready to handle increased load by adding more workers or machines
- **Scalability Option:** Increase PostgreSQL `max_connections` or deploy multiple service instances

---

## Environment Configuration

The application uses environment-based configuration with `.env` files:

- **Local Development:** `.env.dev`
- **Production / Docker:** `.env.prod`

Depending on the environment, the application automatically picks the correct `.env` file to configure the database connection, Redis, and other environment variables.

Example `.env` variables:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=taskdb
POSTGRES_HOST=localhost  # Use 'db' when running in Docker
POSTGRES_PORT=5432

REDIS_HOST=localhost  # Use 'redis' when running in Docker
REDIS_PORT=6379
REDIS_PASSWORD=
```

**Environment Behavior:**
- When running **locally**: `.env.dev` is used with `POSTGRES_HOST=localhost` and `REDIS_HOST=localhost`
- When running with **Docker**: `.env.prod` is used with `POSTGRES_HOST=db` and `REDIS_HOST=redis`

---

## Requirements

- Python 3.13+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis (optional for Docker, falls back to database-only mode)
- Gunicorn (for production)
- Locust (for load testing)

---

## Local Setup

1. Navigate to the API folder:

```bash
cd api
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure environment variables:

Create a `.env.dev` file in the `api` folder with your local database and Redis settings.

6. Start Redis (required for caching):

**Using Docker:**
```bash
docker run -d --name redis_local -p 6379:6379 redis:latest
```

**Or using Homebrew (macOS):**
```bash
redis-server
```

---

## Docker Setup

### Prerequisites
- Docker and Docker Compose installed
- `.env.prod` file configured with appropriate settings

### Quick Start

From the project root, run:

```bash
docker-compose up -d --build
```

This will build and start:
- FastAPI application container
- PostgreSQL database container
- Redis cache container

**Notes:**
- The application requires a PostgreSQL database named `taskdb`
- Docker networking ensures containers communicate using service names (`db` and `redis`)
- The app includes a retry mechanism for database connection to handle startup race conditions
- Redis is optional; if unavailable, the app will operate in database-only mode

---

## Running the Application

### Development (Single Worker with Auto-Reload)

Using the provided shell script:

```bash
./start.sh
```

This script automatically:
- Creates/starts Redis Docker container
- Starts Uvicorn with auto-reload on port 8000

**Manual execution:**
```bash
docker start redis_local 2>/dev/null || docker run -d --name redis_local -p 6379:6379 redis:latest
cd ./api
python -m uvicorn app:app --reload
```

### Production (Multi-Worker with Gunicorn)

Using the provided shell script:

```bash
./start_workers.sh
```

**Manual execution:**
```bash
docker start redis_local 2>/dev/null || docker run -d --name redis_local -p 6379:6379 redis:latest
cd ./api
gunicorn app:app -w 21 -k uvicorn.workers.UvicornWorker
```

**Parameters:**
- `-w 21` – Number of workers (adjust based on CPU cores: cores × 2 + 1)
- `-k uvicorn.workers.UvicornWorker` – Use Uvicorn worker for async support

The server will start on http://127.0.0.1:8000

---

## Load Testing

### Using Locust

Locust provides a web-based interface for load testing at `http://localhost:8089`

1. Install Locust:

```bash
pip install locust
```

2. Run load tests:

```bash
cd api/test -f load_test.py 
```

3. Access the Locust UI:

Open http://localhost:8089 in your browser

4. Configure and start tests:
- Set number of users (e.g., 100)
- Set spawn rate (e.g., 10 users/second)
- Monitor real-time metrics and response times

### Example Test Results
- **100 concurrent users:** 100 GET + 100 POST requests
- **Success Rate:** 99%
- **Database Connections Used:** ~189 out of 189 available
- **Response Time:** Varies based on operation complexity

---

## Usage

The API provides full CRUD operations for tasks with the following features:

- Create, read, update, and delete tasks
- Redis caching for improved performance on read operations
- Async processing for non-blocking I/O
- Comprehensive error handling and logging
- The frontend can connect to the API endpoints as defined in `BASE_URL`

---

## Additional Notes

- **Async Logger:** All logging operations are async for non-blocking performance tracking
- **Exception Handling:** All exceptions are handled asynchronously with proper logging
- **Redis Fallback:** If Redis is unavailable (Docker not running), the application operates in database-only mode
- **Utility Scripts:** Database cleaning and seeding scripts are available in the `utils` folder
- **Seeders:** Automatically populate the database on startup or can be manually invoked
- **Shell Scripts:** Two shell scripts provided:
  - `./start.sh` – Starts the application with Uvicorn (single worker, development)
  - `./start_workers.sh` – Starts the application with Gunicorn (21 workers, production)
- **Horizontal Scaling:** Deploy multiple instances behind a load balancer to handle increased traffic
- **Vertical Scaling:** Increase PostgreSQL `max_connections` or adjust worker count based on system resources