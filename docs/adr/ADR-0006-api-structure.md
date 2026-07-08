# ADR-0006: API Layer Structure

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

The API is expected to grow to support multiple functional domains, authentication, AI services, and enterprise integrations.

## Decision

The API will follow a layered architecture:

- `api/` — HTTP routes
- `core/` — configuration, logging, startup
- `services/` — business logic
- `models/` — persistence
- `schemas/` — request and response models

## Rationale

This separation keeps HTTP concerns independent from business logic, improving maintainability, testability, and scalability.

## Consequences

### Advantages

- Thin controllers (routers)
- Reusable business logic
- Clear separation of concerns
- Easier testing

### Trade-offs

The structure introduces additional modules early in the project but avoids significant refactoring as the application grows.
