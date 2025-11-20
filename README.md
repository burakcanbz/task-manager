# Task Manager API

A **Task Management API** built with **FastAPI** using a **layered architecture** and **SQLAlchemy** for database operations. This project demonstrates a clean separation of concerns, maintainable code structure, and scalable design, with support for environment-based configuration and Docker deployment.

---

## Table of Contents

- Environment Configuration
- Requirements
- Local Setup
- Docker Setup
- Usage
- Additional Notes

---

## Architecture

The API is designed using a **layered architecture**, which separates responsibilities into different layers:

1. **Controller** – Handles incoming HTTP requests and responses, validation, and delegates business logic to services.
2. **Service** – Contains the core business logic and orchestrates operations between repositories and other utilities.
3. **DTO (Data Transfer Object)** – Defines the shape of data that flows between layers, ensuring type safety and validation separate from the database model.
4. **Repository** – Handles direct interaction with the database via SQLAlchemy, encapsulating CRUD operations.
5. **Model** – Defines SQLAlchemy models corresponding to database tables.
6. **Data** – Contains seeders for initial database population.
7. **Config** – Manages database connection, environment variables, and dependency injection for using same service but different db instance.
8. **Utils** – Contains helper scripts like `clean_tasks` and `seed_data` for database operations or maintenance tasks.

**Why Layered Architecture?**
- **Separation of concerns:** Each layer has a single responsibility.
- **Maintainability:** Easier to modify or extend individual layers without affecting others.
- **Testability:** Layers can be tested independently.
- **Scalability:** Supports larger applications and teams by clearly separating responsibilities.

---

## Environment Configuration

The application uses environment-based configuration with `.env` files:

- **Local Development:** `.env.dev`
- **Production / Docker:** `.env.prod`

Depending on the environment, the application automatically picks the correct `.env` file to configure the database connection and other environment variables.

Example `.env` variables:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=taskdb
POSTGRES_HOST=localhost  # Use 'db' when running in Docker
POSTGRES_PORT=5432
ENVIRONMENT=dev  # or 'prod' for production
```

**Environment Behavior:**
- When running **locally**: `.env.dev` is used and `POSTGRES_HOST=localhost`
- When running with **Docker**: `.env.prod` is used and `POSTGRES_HOST=db`

---

## Requirements

- Python 3.13+
- FastAPI
- SQLAlchemy
- PostgreSQL

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

Create a `.env.dev` file in the `api` folder with your local database settings.

6. Run the FastAPI server:

```bash
uvicorn app:app --reload
```

The server will start on http://127.0.0.1:8000

---

## Docker Setup

1. Ensure `.env.prod` has the correct database connection settings.

2. From the project root, run:

```bash
docker-compose up -d --build
```

This will build and start both the FastAPI app and the PostgreSQL container.

**Notes:**
- The application requires a PostgreSQL database named `taskdb`
- Docker networking ensures the FastAPI container can communicate with the PostgreSQL container using the host `db`
- The app includes a retry mechanism for database connection to handle startup race conditions

---

## Usage

The API provides full CRUD operations for tasks with the following features:

- Create, read, update, and delete tasks
- Filter tasks by priority and status
- Sort tasks by creation date or priority
- The frontend can connect to the API endpoints as defined in `BASE_URL`

---

## Additional Notes

- The project includes utility scripts for database cleaning and seeding
- Seeders can be found in the `data` folder
- The layered architecture allows you to easily extend functionality without touching unrelated layers
- Use `python -m data.seeder` to populate the database with sample data