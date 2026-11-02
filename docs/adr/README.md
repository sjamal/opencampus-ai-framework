# Architecture Decision Records

Capture Architecture Decision Records (ADRs) for important technical decisions.

Each ADR explains:

- The problem
- Available options
- The chosen solution
- Why it was selected
- Future implications

These ADRs help preserve project knowledge over time.

## Index

| ADR | Decision | Roadmap Phase | Status |
|-----|----------|---------------|:------:|
| [ADR-0001](ADR-0001.md) | Project Philosophy | 0 — Foundation | 📝 Empty — see [Project Philosophy](../../PROJECT_PHILOSOPHY.md) |
| [ADR-0002](ADR-0002.md) | Python Tooling | 0 — Foundation | ✅ |
| [ADR-0003](ADR-0003-project-structure.md) | Repository Structure | 0 — Foundation | ✅ |
| [ADR-0004](ADR-0004-project-configuration.md) | Project Configuration | 1 — Platform | ✅ |
| [ADR-0005](ADR-0005-local-development.md) | Local Development Environment | 1 — Platform | ✅ |
| [ADR-0006](ADR-0006-api-structure.md) | API Layer Structure | 1 — Platform | ✅ |
| [ADR-0007](ADR-0007-fastapi-lifespan.md) | FastAPI Application Lifecycle | 1 — Platform | ✅ |
| [ADR-0008](ADR-0008-configuration-management.md) | Configuration Management | 1 — Platform | ✅ |
| [ADR-0009](ADR-0009-local-infrastructure.md) | Local Infrastructure | 1 — Platform | ✅ |
| [ADR-0010](ADR-0010-local-service-port-isolation.md) | Local Service Port Isolation | 1 — Platform | ✅ |
| [ADR-0011](ADR-0011-database-layer.md) | Database Layer | 1 — Platform | ✅ |
| [ADR-0012](ADR-0012-audit-event-model.md) | Audit Event Model | 2 — Authentication & Security | ✅ |
| [ADR-0013](ADR-0013-repository-service-pattern.md) | Repository and Service Pattern | 2 — Authentication & Security | ✅ |
| [ADR-0014](ADR-0014-audit-api-pattern.md) | Audit API Pattern | 2 — Authentication & Security | ✅ |

### Upcoming Decisions

Research in progress that is expected to become ADRs:

- [Authentication Options](../decisions/authentication-options.md) — Phase 2
- [Workflow Engines](../decisions/workflow-engines.md) — Phase 3
- [LLM Provider Comparison](../decisions/llm-provider-comparison.md) — Phase 4
- [MCP Evaluation](../decisions/mcp-evaluation.md) — Phase 5

See the [Documentation index](../README.md) for overall roadmap coverage.
