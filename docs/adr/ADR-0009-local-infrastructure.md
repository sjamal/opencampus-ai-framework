# ADR-0009: Local Infrastructure

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

The application requires supporting infrastructure including databases, caching, messaging, and future AI services.

Developers need a consistent local environment.

## Decision

The project will use Docker Compose for local infrastructure orchestration.

Initial services:

- PostgreSQL
- Redis

## Rationale

Docker Compose provides:

- Repeatable environments
- Isolation from the host system
- Simple onboarding
- A path toward production container deployments

## Consequences

### Advantages

- Consistent developer experience
- Easy startup/shutdown
- Infrastructure versioning

### Trade-offs

Developers must install Docker Desktop.
