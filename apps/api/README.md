# API Service

## Purpose

The API Service is the primary entry point for the OpenCampus AI Framework.

It exposes REST endpoints used by administrative applications, web clients, external integrations, and future AI agents.

The service is intentionally organized using a layered architecture to separate HTTP concerns from business logic and data access.

---

## Responsibilities

- REST API
- Authentication & Authorization
- Request Validation
- Workflow Orchestration
- AI Service Integration
- OpenAPI Documentation
- Health & Diagnostics

---

## Directory Structure

| Directory | Responsibility |
|-----------|----------------|
| `app/api/` | HTTP endpoints and route definitions |
| `app/core/` | Configuration, logging, application startup |
| `app/services/` | Business logic and workflow orchestration |
| `app/models/` | Database models and persistence |
| `app/schemas/` | Request and response models (Pydantic) |

---

## Request Flow

```text
HTTP Request
      │
      ▼
API Router
      │
      ▼
Service Layer
      │
      ▼
Models / External Systems
      │
      ▼
Database / APIs / AI Services
      │
      ▼
HTTP Response
```

Business logic should reside in the **Service Layer**, keeping API routes thin and focused on request handling.

---

## Technology Stack

- FastAPI
- Pydantic
- Uvicorn

Future additions:

- SQLAlchemy
- Alembic
- PostgreSQL
- Redis
- OpenTelemetry
- MCP
- AI Provider Abstraction Layer

---

## Status

🚧 Under Development
