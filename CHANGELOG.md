# Changelog

All notable changes to this project will be documented in this file.

The project generally follows the principles of:

- Semantic Versioning
- Conventional Commits

---

## Unreleased

### Added

- Initial repository structure
- Documentation framework
- Learning roadmap
- Architecture documentation
- AI engineering toolkit
- Audit events API with router, service and repository layers (ADR-0014)
- Test suite covering audit event API, service, repository and schemas
- GitHub Actions CI: lint, migrations and tests against PostgreSQL
- Issue and pull request templates
- Documentation index with roadmap coverage

### Fixed

- Health check crashed when the database was unavailable
- Database URL was printed at startup
- Alembic now reads the database URL from application settings
