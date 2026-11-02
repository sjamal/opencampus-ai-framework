# OpenCampus AI Framework (OCAF)

> A modular, open-source framework for building secure, AI-assisted enterprise workflows using Agentic AI, Model Context Protocol (MCP), and modern software engineering practices.

> **Project Status:** 🚧 Early Development (Foundation Phase)

---

## Vision

The OpenCampus AI Framework (OCAF) is an educational and reference implementation for designing enterprise-grade AI workflow systems.

Although the first reference implementation focuses on higher education administration (registrar services, admissions, and academic workflows), the architecture is intentionally designed to support a wide range of enterprise domains.

The project emphasizes:

- Modular architecture
- AI-assisted workflow automation
- Human-in-the-loop decision making
- Secure enterprise integration
- Production-quality engineering practices
- Comprehensive documentation

---

## Why This Project Exists

Modern organizations have mature systems of record but often lack intelligent orchestration between them.

This project explores how Large Language Models (LLMs), Model Context Protocol (MCP), APIs, workflow engines, and modern software engineering can be combined to create secure, maintainable, and explainable AI-enabled business applications.

The goal is to demonstrate best practices—not just build another AI chatbot.

---

## Current Status

The project is currently focused on establishing:

- Repository structure
- Architecture documentation
- Development standards
- Learning materials
- Initial platform foundation

Application development is underway: the FastAPI backend, PostgreSQL persistence and the first audit events API are in place.

---

## Planned Features

- REST API Platform
- AI Service Layer
- MCP Server
- Workflow Engine
- Authentication & Authorization
- Document Processing
- Policy Search (RAG)
- Registrar Reference Application
- Additional Enterprise Examples

---

## Repository Structure

```text
apps/             Deployable applications
services/         Business services
shared/           Shared libraries
docs/             Project documentation
learning/         Learning materials
.ai/              AI development toolkit
tests/            Automated tests
infrastructure/   Deployment resources
```

---

## Documentation

The [Documentation index](docs/README.md) lists every document in the repository, its status, and how it maps to the roadmap.

| Document | Purpose |
|----------|---------|
| [Documentation index](docs/README.md) | Every document, its status, and roadmap coverage |
| [Vision](docs/Vision.md) | Project vision |
| [Project Philosophy](PROJECT_PHILOSOPHY.md) | Guiding principles |
| [Roadmap](docs/Roadmap.md) | Development roadmap |
| [Architecture](docs/Architecture.md) | System architecture |
| [Glossary](docs/Glossary.md) | Common terminology |
| [Learning Roadmap](learning/00-roadmap.md) | Structured learning guide |
| [Architecture Decision Records](docs/adr/README.md) | Architecture Decision Records |
| [Engineering Journal](docs/Journal.md) | Why decisions were made, sprint by sprint |
| [API Service](apps/api/README.md) | API structure and request flow |
| [Testing](tests/README.md) | How to run the tests |

If it's explaining a technology (e.g., FastAPI, Docker, MCP), it belongs in learning/.
If it's explaining a project-wide decision or process, it belongs in docs/.
If it's explaining a specific folder or service, it belongs in that folder's README.md.

---

## Technology Stack (Planned)

- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- Model Context Protocol (MCP)
- OpenAI-compatible APIs
- Ollama
- GitHub Actions

---

## Guiding Principles

- Documentation evolves with the software.
- AI is a replaceable component.
- Security is designed in from the beginning.
- Build incrementally with working software.
- Prefer open standards over vendor lock-in.

---

## Roadmap

The project roadmap is maintained in [docs/Roadmap.md](docs/Roadmap.md).

---

## Contributing

Contributions are welcome.

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Project Status

This project is under active development. The table below tracks the high-level progress of major components.

| Area | Status | Notes |
|------|:------:|------|
| Repository Structure | ✅ Complete | Initial project organization established |
| Project Documentation | 🚧 In Progress | Core documentation created; will evolve with the project |
| Learning Materials | 🚧 In Progress | Initial learning roadmap created |
| Architecture | 🚧 In Progress | High-level architecture and vision defined |
| Development Environment | ✅ Complete | Python, VS Code, Docker, uv, PostgreSQL |
| FastAPI Backend | 🚧 In Progress | Health and audit events APIs |
| Authentication & Authorization | ⏳ Planned | OAuth2 / OpenID Connect / RBAC |
| Workflow Engine | ⏳ Planned | Generic approval and routing engine |
| AI Service Layer | ⏳ Planned | Multi-provider LLM abstraction |
| Model Context Protocol (MCP) | ⏳ Planned | MCP server and business tools |
| Document Processing | ⏳ Planned | OCR, ingestion, metadata extraction |
| Knowledge & RAG | ⏳ Planned | Enterprise knowledge retrieval |
| Reference Applications | ⏳ Planned | Registrar, Admissions, HR, and additional examples |
| Testing & CI/CD | 🚧 In Progress | pytest suite and GitHub Actions CI |
| Production Deployment | ⏳ Planned | Containerized deployment and monitoring |

### Status Legend

- ✅ Complete
- 🚧 In Progress
- ⏳ Planned
- ⚠️ Under Review
- ❌ Deferred

---

## License

Released under the [MIT License](LICENSE).

