# ADR-0005: Local Development Environment

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

Developers require a consistent local environment that minimizes onboarding effort and mirrors the project's future deployment model.

## Decision

Development will follow a local-first workflow:

- Repository-local Python virtual environment (`.venv`)
- VS Code as the reference IDE
- Docker Desktop for infrastructure services
- `uv` for Python dependency management

## Rationale

A local-first approach provides rapid feedback, isolates project dependencies, and establishes a consistent developer experience.

## Consequences

### Advantages

- Simple onboarding
- Reproducible environments
- Minimal host system impact
- Strong foundation for future CI/CD

### Trade-offs

Developers must install Docker Desktop and modern Python tooling before contributing.
