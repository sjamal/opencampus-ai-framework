# ADR-0014: Audit API Pattern

## Status

Accepted

## Context

Audit events are the first complete API implementation within the OpenCampus AI Framework.

## Decision

Adopt a layered architecture:

- Router
- Service
- Repository
- Database

All API endpoints will use Pydantic request and response schemas.

## Consequences

- Consistent endpoint implementation
- Separation of concerns
- Easier testing
- Reusable service layer
