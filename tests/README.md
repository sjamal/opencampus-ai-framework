# Testing

Automated tests for the platform.

Testing strategy includes:

- Unit Tests
- Integration Tests
- API Tests
- End-to-End Tests
- Performance Tests

Every new feature should include appropriate automated tests.

## Running Tests

Start PostgreSQL and apply migrations, then run pytest from the repository root:

```bash
docker-compose -f infrastructure/docker-compose.yml up -d postgres
(cd apps/api && uv run alembic upgrade head)
uv run pytest
```

The same steps run in [CI](../.github/workflows/ci.yml) on every push and pull request.

## Layout

Tests mirror the API's layered architecture ([ADR-0013](../docs/adr/ADR-0013-repository-service-pattern.md), [ADR-0014](../docs/adr/ADR-0014-audit-api-pattern.md)):

| Folder | Layer | Needs database |
|--------|-------|:--------------:|
| `api/` | HTTP endpoints, request validation, status codes | Yes |
| `services/` | Business logic, using a fake repository | No |
| `repositories/` | Database operations | Yes |
| `schemas/` | Pydantic request/response validation | No |

## Database Isolation

The `db_session` fixture in [`conftest.py`](conftest.py) wraps each test in a transaction that is rolled back afterwards. Commits made by application code become savepoints, so tests never leave data behind in the database.
