# Development Standards

This document defines the development conventions used throughout the OpenCampus AI Framework.

---

## Repository

- One Git repository
- One Python project
- One `pyproject.toml`
- One repository-local virtual environment (`.venv`)

---

## Architecture

- Layered architecture
- Thin API routes
- Business logic in services
- Configuration isolated in `core`
- Request/response models separated from persistence models

---

## Documentation

Every significant addition should include:

- Appropriate documentation
- An ADR if an architectural decision is made
- Updates to the learning guides where applicable
- Journal updates at the end of each sprint

---

## Project Principles

- Documentation evolves with the code.
- Prefer open standards.
- Keep components loosely coupled.
- Build incrementally.
- Introduce complexity only when justified.
