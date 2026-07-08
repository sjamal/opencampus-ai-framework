# Docker Development Environment

## Docker Compose

Docker Compose defines and runs multi-container applications.

The project uses Docker Compose to manage local infrastructure services.

Current services:

```text
FastAPI Application
        |
        |
Docker Compose
        |
        +---- PostgreSQL
        |
        +---- Redis
```

Benefits:

- Reproducible environments
- Service isolation
- Easier onboarding
- Production alignment

## Docker Desktop on macOS

Docker commands require both:

1. Docker CLI
2. Docker Engine (Docker Desktop)

The CLI communicates with Docker Desktop through the Docker API socket.

Verify Docker Desktop is running:

```bash
docker info
```

A working installation should show both:

- Client information
- Server information

If Docker Desktop is not running, commands such as:

```bash
docker-compose up -d
```

will fail because the Docker daemon is unavailable.

## Project Port Isolation

Multiple development projects may run Docker services simultaneously.

Each project should avoid assuming default ports are always available.

Example:

```yaml
redis:
  ports:
    - "6380:6379"
```

The first value is the host machine port.

The second value is the container port.

This allows multiple Redis containers to coexist:

```text
Project A
Redis
Host: 6379
Container: 6379


OpenCampus AI Framework
Redis
Host: 6380
Container: 6379
```


