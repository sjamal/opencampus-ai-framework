# Documentation

Welcome to the OpenCampus AI Framework documentation.

This directory contains the architectural, technical, and operational documentation for the project. This page indexes **every** document in the repository and shows how far along each one is, so gaps are easy to spot against the [Roadmap](Roadmap.md).

## Philosophy

Documentation is written alongside any code, and major architectural decision should be reflected here.

- If it's explaining a technology (e.g., FastAPI, Docker, MCP), it belongs in [`learning/`](../learning/).
- If it's explaining a project-wide decision or process, it belongs in [`docs/`](.).
- If it's explaining a specific folder or service, it belongs in that folder's `README.md`.

### Status Legend

- ✅ Drafted — substantial content
- 🟡 Started — short or partial
- 📝 Placeholder — file exists but is empty

---

## Roadmap Coverage

How each [Roadmap](Roadmap.md) phase is supported by working software and documentation.

| Phase | Implementation | Documentation | Gaps |
|-------|:--------------:|---------------|------|
| 0 — Foundation | ✅ Complete | [Vision](Vision.md), [Project Philosophy](../PROJECT_PHILOSOPHY.md), [Development Standards](DevelopmentStandards.md), [ADR-0002](adr/ADR-0002.md), [ADR-0003](adr/ADR-0003-project-structure.md) | [ADR-0001](adr/ADR-0001.md) is empty |
| 1 — Platform | 🚧 Mostly complete | [ADR-0004](adr/ADR-0004-project-configuration.md) – [ADR-0011](adr/ADR-0011-database-layer.md), [FastAPI](../learning/04-fastapi.md), [PostgreSQL](../learning/05-postgresql.md), [Docker](../learning/10-docker.md), [API Service](../apps/api/README.md) | [Development](Development.md), [Database](Database.md) and [REST APIs](../learning/03-rest-apis.md) are empty; Redis is provisioned but not yet used |
| 2 — Authentication & Security | 🚧 Audit events only | [ADR-0012](adr/ADR-0012-audit-event-model.md) – [ADR-0014](adr/ADR-0014-audit-api-pattern.md), [Security Policy](../SECURITY.md) | Authentication not started; [Security](Security.md), [Security learning guide](../learning/09-security.md) and [authentication options](decisions/authentication-options.md) are empty |
| 3 — Workflow Engine | ⏳ Planned | — | [Workflow](Workflow.md) and [workflow engines](decisions/workflow-engines.md) are empty |
| 4 — AI Services | ⏳ Planned | [AI Engineering Toolkit](../.ai/README.md) | [AI](AI.md), [LLM provider comparison](decisions/llm-provider-comparison.md) and [Agents](../learning/07-agents.md) are empty |
| 5 — MCP Integration | ⏳ Planned | — | [MCP](MCP.md), [MCP evaluation](decisions/mcp-evaluation.md) and [MCP learning guide](../learning/06-mcp.md) are empty |
| 6 — Knowledge & Documents | ⏳ Planned | — | [RAG](../learning/08-rag.md) is empty; no `docs/` page yet |
| 7 — Example Applications | ⏳ Planned | [Examples](../examples/README.md) | No example applications yet |
| 8 — Production Readiness | 🚧 CI only | [CI workflow](../.github/workflows/ci.yml), [Infrastructure](../infrastructure/README.md) | No docs yet for deployment, monitoring or disaster recovery |

---

## Start Here

| Document | Purpose | Status |
|----------|---------|:------:|
| [Project README](../README.md) | Overview, structure and status | ✅ |
| [Vision](Vision.md) | Project vision | ✅ |
| [Project Philosophy](../PROJECT_PHILOSOPHY.md) | Guiding principles | ✅ |
| [Roadmap](Roadmap.md) | Development roadmap | ✅ |
| [Learning Roadmap](../learning/00-roadmap.md) | Structured learning guide | ✅ |
| [Glossary](Glossary.md) | Common terminology | ✅ |

## Architecture & Design

| Document | Purpose | Status |
|----------|---------|:------:|
| [Architecture](Architecture.md) | System architecture | 🟡 |
| [Architecture Decision Records](adr/README.md) | Index of all ADRs | ✅ |
| [Database](Database.md) | Data model and persistence | 📝 |
| [Security](Security.md) | Security architecture | 📝 |
| [Workflow](Workflow.md) | Workflow engine | 📝 |
| [AI](AI.md) | AI service layer | 📝 |
| [MCP](MCP.md) | Model Context Protocol integration | 📝 |

### Technology Evaluations

Research that feeds into future ADRs.

| Document | Status |
|----------|:------:|
| [Authentication Options](decisions/authentication-options.md) | 📝 |
| [LLM Provider Comparison](decisions/llm-provider-comparison.md) | 📝 |
| [MCP Evaluation](decisions/mcp-evaluation.md) | 📝 |
| [Workflow Engines](decisions/workflow-engines.md) | 📝 |

## Development

| Document | Purpose | Status |
|----------|---------|:------:|
| [Development Standards](DevelopmentStandards.md) | Coding and documentation standards | ✅ |
| [Development](Development.md) | Developer guide | 📝 |
| [Development Environment](development/DevelopmentEnvironment.md) | Tool versions | 🟡 |
| [Contributing](../CONTRIBUTING.md) | How to contribute | ✅ |
| [Testing](../tests/README.md) | Test layout and how to run tests | ✅ |
| [CI Workflow](../.github/workflows/ci.yml) | Lint, migrations and tests on every push | ✅ |
| [Pull Request Template](../.github/pull_request_template.md) | PR checklist | ✅ |
| [Bug Report](../.github/ISSUE_TEMPLATE/bug_report.md) / [Feature Request](../.github/ISSUE_TEMPLATE/feature_request.md) | Issue templates | ✅ |

## Learning Guide

See the [Learning Roadmap](../learning/00-roadmap.md) for how these map to learning stages.

| Guide | Status |
|-------|:------:|
| [01 — Git & Development Environment](../learning/01-git.md) | ✅ |
| [02 — Python](../learning/02-python.md) | 🟡 |
| [03 — REST APIs](../learning/03-rest-apis.md) | 📝 |
| [04 — FastAPI](../learning/04-fastapi.md) | ✅ |
| [05 — PostgreSQL](../learning/05-postgresql.md) | ✅ |
| [06 — MCP](../learning/06-mcp.md) | 📝 |
| [07 — Agents](../learning/07-agents.md) | 📝 |
| [08 — RAG](../learning/08-rag.md) | 📝 |
| [09 — Security](../learning/09-security.md) | 📝 |
| [10 — Docker](../learning/10-docker.md) | ✅ |

## Journals & History

| Document | Purpose | Status |
|----------|---------|:------:|
| [Engineering Journal](Journal.md) | Why decisions were made, sprint by sprint | ✅ |
| [Project Journal](Project_Journal.md) | Early Sprint 0 notes (overlaps the Engineering Journal) | 🟡 |
| [2026-07-07](journal/2026-07-07.md) | Daily development journal | ✅ |
| [Changelog](../CHANGELOG.md) | What changed | 🟡 |

## Component READMEs

| Folder | Status |
|--------|:------:|
| [apps/](../apps/README.md) | 🟡 |
| [apps/api/](../apps/api/README.md) | ✅ |
| [services/](../services/README.md) | 🟡 |
| [shared/](../shared/README.md) | 🟡 |
| [infrastructure/](../infrastructure/README.md) | 🟡 |
| [scripts/](../scripts/README.md) | 🟡 |
| [examples/](../examples/README.md) | 🟡 |
| [tests/](../tests/README.md) | ✅ |

## AI Engineering Toolkit

| Document | Status |
|----------|:------:|
| [AI Engineering Toolkit](../.ai/README.md) | 🟡 |
| [Prompts](../.ai/prompts/README.md) | 🟡 |
| [Playbooks](../.ai/playbooks/README.md) | 📝 |
| [Checklists](../.ai/checklists/README.md) | 📝 |

## Project Policies

| Document | Status |
|----------|:------:|
| [Code of Conduct](../CODE_OF_CONDUCT.md) | 🟡 |
| [Security Policy](../SECURITY.md) | ✅ |
| [License](../LICENSE) | ✅ |
