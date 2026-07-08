# ADR-0010: Local Service Port Isolation

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

Developers may run multiple containerized projects simultaneously. Default service ports may already be occupied.

## Decision

The project will allow configurable host port mappings for local infrastructure services.

Initial configuration:

- PostgreSQL: 5432
- Redis: 6380 host → 6379 container

## Rationale

Avoids conflicts with existing development environments while preserving standard container configurations.

## Consequences

### Advantages

- Multiple projects can coexist
- No need to stop unrelated services
- Clear ownership of local infrastructure

### Trade-offs

Developers must know the host/container port distinction.
