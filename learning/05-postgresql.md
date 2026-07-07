## Async SQLAlchemy and Alembic

Because the application uses FastAPI async endpoints,
the database layer uses SQLAlchemy async support.

Components:

- SQLAlchemy async engine
- asyncpg PostgreSQL driver
- AsyncSession
- Async Alembic migrations

Architecture:
FastAPI
|
AsyncSession
|
SQLAlchemy Async Engine
|
asyncpg
|
PostgreSQL


Alembic must use the async migration template when working with
`postgresql+asyncpg`.
