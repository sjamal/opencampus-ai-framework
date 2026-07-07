# ADR-0011: Database Layer

- Status: Accepted
- Date: 2026-07-07

## Context

The application requires persistent storage for workflows, petitions, users, audit history, and AI-generated artifacts.

## Decision

The project will use:

- SQLAlchemy 2.x ORM
- asyncpg PostgreSQL driver
- Alembic migrations

## Architecture

```
API Router
    |
Service Layer
    |
Database Session
    |
SQLAlchemy ORM
    |
PostgreSQL
```

## Rationale

Provides:

- Async database access
- Explicit migrations
- Strong Python integration
- Production-proven patterns

## Consequences

### Advantages

- Maintainable schema evolution
- Testable data layer
- Clear separation of concerns

### Trade-offs

Adds additional abstraction compared with raw SQL.
