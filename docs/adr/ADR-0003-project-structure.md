# ADR-0003: Repository Structure

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

The project is expected to grow into a modular framework consisting of multiple applications, shared libraries, services, documentation, and infrastructure components.

A clear and scalable repository structure is required from the outset.

## Decision

The repository will adopt a top-level structure separating:

- Applications (`apps/`)
- Business services (`services/`)
- Shared components (`shared/`)
- Infrastructure (`infrastructure/`)
- Documentation (`docs/`)
- Learning materials (`learning/`)
- Tests (`tests/`)
- AI development resources (`.ai/`)

## Rationale

Separating concerns at the repository level improves maintainability, onboarding, and future extensibility while allowing independent evolution of applications and services.

## Consequences

### Advantages

- Clear separation of responsibilities
- Scalable organization
- Easier navigation
- Supports multiple deployable applications

### Trade-offs

The structure introduces additional directories early in the project, but avoids disruptive reorganization as the codebase grows.
