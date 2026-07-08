# 01 - Development Environment

## Objective

Establish a consistent, reproducible local development environment for the OpenCampus AI Framework.

By the end of this guide you will have:

- A cloned GitHub repository
- A Python virtual environment
- Modern Python tooling (`uv`)
- Visual Studio Code configured
- Docker Desktop installed
- Project dependencies installed
- A foundation ready for FastAPI development

---

## Reference Platform

| Component | Version |
|-----------|---------|
| macOS | Tahoe 26.5.1 |
| Hardware | Apple Silicon (M1 Pro) |
| Python | 3.14.4 |
| Git | 2.45.2 |
| Docker | 29.6.1 |
| Docker Compose | 5.3.0 |
| VS Code | 1.127.0 |
| uv | 0.11.27 |

---

## Repository

Repository Root

```text
opencampus-ai-framework
```

All project commands are executed from this directory unless otherwise specified.

---

## Python Virtual Environment

Create:

```bash
uv venv
```

Activate:

```bash
source .venv/bin/activate
```

Verify:

```bash
which python
python --version
```

Expected interpreter:

```text
<repository>/.venv/bin/python
```

---

## Dependency Management

Project dependencies are defined in:

```text
pyproject.toml
```

Install or synchronize dependencies:

```bash
uv sync
```

View installed packages:

```bash
uv pip list
```

---

## Visual Studio Code

Workspace configuration is stored in:

```text
.vscode/settings.json
```

VS Code should use:

```text
<repository>/.venv/bin/python
```

Verify from:

Command Palette → **Python: Select Interpreter**

---

## Current Sprint Progress

- Repository initialized
- Virtual environment configured
- VS Code configured
- Project configuration established
- Dependencies installed

Next:

- Create FastAPI application
- Add Docker Compose
- Configure PostgreSQL
- Configure Redis
- Implement Health endpoint

---

## Related Documentation

- docs/Journal.md
- docs/Roadmap.md
- docs/Vision.md
- docs/adr/
