# Project Catalog API

Lightweight FastAPI service for managing project entries with CRUD endpoints, health checks, versioning, and SQLite persistence.

## Features

- FastAPI application with OpenAPI documentation
- CRUD endpoints for portfolio projects
- Health and version endpoints for service checks
- SQLAlchemy-based persistence with SQLite by default
- Environment-based configuration through `.env`
- Automated API tests with `pytest`
- Docker and Docker Compose support for local deployment

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- Pydantic Settings
- Uvicorn
- Pytest

## API Overview

Base path: `/api/v1`

| Method | Path                     | Description                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | `/health`                | Service health check         |
| GET    | `/version`               | Application name and version |
| GET    | `/projects`              | List all projects            |
| GET    | `/projects/{project_id}` | Get a project by id          |
| POST   | `/projects`              | Create a project             |
| PUT    | `/projects/{project_id}` | Update a project             |
| DELETE | `/projects/{project_id}` | Delete a project             |

## Project Structure

```text
project-catalog-api/
  app/
    api/routes/
    core/
    models/
    schemas/
    services/
    main.py
  tests/
  Dockerfile
  docker-compose.yml
  pyproject.toml
```

## Architecture

- `app/main.py` creates the FastAPI application and registers routes.
- `app/api/routes/` contains HTTP route handlers.
- `app/schemas/` defines request and response models.
- `app/services/` contains business logic and database operations.
- `app/models/` defines SQLAlchemy models.
- `app/core/` contains configuration and database setup.

## Getting Started

### Prerequisites

- Python 3.11 or later
- `pip`

### Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
copy .env.example .env
python -m uvicorn app.main:app --reload
```

The service will be available at `http://127.0.0.1:8000`.

### Configuration

The application reads settings from `.env`.

```env
APP_NAME=Project Catalog API
APP_VERSION=0.1.0
DATABASE_URL=sqlite:///./portfolio.db
```

On startup, the application initializes the database and creates tables if they do not already exist.

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Example Request

```json
{
  "title": "Recording API Modernization",
  "summary": "Designed and implemented a resilient API for document and workflow operations.",
  "tech_stack": ["FastAPI", "SQLAlchemy", "Docker"],
  "repo_url": "https://github.com/your-user/project-catalog-api",
  "live_url": "https://api.example.com/projects/1",
  "is_featured": true
}
```

## Running Tests

```bash
python -m pytest
```

## Docker

```bash
docker compose up --build
```

The container runs the API on port `8000`.


## License

MIT
