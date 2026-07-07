# ADR-0004: Project Configuration

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

Modern Python projects often have multiple configuration files for dependencies, build settings, and tooling. Consolidating configuration improves maintainability and developer onboarding.

## Decision

The project will use `pyproject.toml` as the primary configuration file for project metadata, dependencies, and development tooling.

## Rationale

- Aligns with modern Python packaging standards.
- Simplifies dependency management with `uv`.
- Reduces configuration sprawl.
- Supports future packaging and CI/CD workflows.

## Consequences

### Advantages

- Single source of truth for Python configuration.
- Easier onboarding for new contributors.
- Compatible with modern tooling.

### Trade-offs

Some legacy tools still expect separate configuration files, but most actively maintained tools support `pyproject.toml`.
