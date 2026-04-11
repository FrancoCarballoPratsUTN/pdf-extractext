# PDF ExtractText

A system that allows extracting text from PDF files and converting that content into a Markdown (.md) file, which will also be summarized.

###### Current Status
This system is currently under development.

## Description

PDF ExtractText is a REST API developed in Python that allows:

- **Extracting text** from PDF files.
- **Converting** extracted content into Markdown (.md) format.
- **Storing** documents in MongoDB.
- **Managing** extracted documents through REST endpoints.

## Features
- PDF text extraction.
- Markdown file conversion.
- API REST with FastAPI.
- MongoDB storage.
- Test-Driven Development (TDD).
- Clean code following SOLID principles and Clean Code.

## Technology

| Category | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Framework | FastAPI |
| Database | MongoDB |
| IA | "Update" |
| Dependency management | UV |
| Testing | Pytest |

### Main Dependencies

- **fastapi**: Modern and fast web framework.
- **pydantic**: Data validation.
- **uvicorn**: ASGI server.
- **python-multipart**: Multipart file handling.

## Project Structure

```
pdf-extractext/
├── .agents/
│   └── skills/
│       ├── clean-code/
│       │   └── SKILL.md
│       └── tdd/
│           ├── SKILL.md
│           ├── deep-modules.md
│           ├── interface-design.md
│           ├── mocking.md
│           ├── refactoring.md
│           └── tests.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data/
│   │   ├── database/
│   │   │   └── connection.py
│   │   └── repositories/
│   │       ├── __init__.py
│   │       └── document_repository.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── document.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── document_repository.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       └── document_use_cases.py
│   └── presentation/
│       ├── __init__.py
│       ├── routes/
│       │   ├── __init__.py
│       │   └── document.py
│       └── schemas/
│           ├── __init__.py
│           └── document.py
├── tests/
│   ├── conftest.py
│   ├── data/
│   │   └── test_document_repository.py
│   ├── domain/
│   │   └── test_document.py
│   └── presentation/
│       └── test_routes.py
├── main.py
├── pyproject.toml
├── README.md
└── skills-lock.json
```

#### Description of Folders

- **`app/`**: Main application code.
  - **`config/`**: Centralized application configuration.
  - **`data/`**: Implementations of repositories and data access.
    - **`database/`**: Database connections.
    - **`repositories/`**: Specific implementations of repositories.
  - **`domain/`**: Pure business logic.
    - **`entities/`**: Domain entities.
    - **`repositories/`**: Repository interfaces (contracts).
    - **`use_cases/`**: Application use cases.
  - **`presentation/`**: Presentation layer.
    - **`routes/`**: Definition of routes and endpoints.
    - **`schemas/`**: Pydantic schemes for validation.
- **`tests/`**: Unit and integrated test suite.
- **`.agents/`**: Configuring skills for the AI ​​agent.

### Architecture (Clean Architecture)

The project follows a clean architecture with the following layers:

```
┌─────────────────────────────────────────┐
│           PRESENTATION                  │
│  (Routes, Schemas, API Endpoints)       │
├─────────────────────────────────────────┤
│             DOMAIN                      │
│  (Entities, Use Cases, Repository       │
│   Interfaces)                           │
├─────────────────────────────────────────┤
│              DATA                       │
│  (Repository Implementations, Database  │
│   Connection, External Services)        │
└─────────────────────────────────────────┘
```

## Installation and Configuration

### Prerequisites

- Python 3.10 - 3.13
- UV (package manager and virtual environments)
- MongoDB (local or remote)

### Facility

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FrancoCarballoPratsUTN/pdf-extractext
   cd pdf-extractext
   ```

2. **Install dependencies with UV:**
   ```bash
   uv sync
   ```

3. **Install development dependencies:**
   ```bash
   uv sync --extra dev
   ```

### Execution

**Development mode:**
```bash
uv run python main.py
```

**Production mode:**
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available in `http://localhost:8000`

**Documentación interactive:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API usage

### Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/documents/extract` | Extract text from a PDF and convert to MD |
| GET | `/api/documents/` |List all documents |
| GET | `/api/documents/{id}` | Get a document by ID |
| DELETE | `/api/documents/{id}` | Delete a document |

### Example of Use

**Extracting text from a PDF:**

```bash
curl -X POST "http://localhost:8000/api/documents/extract" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@ruta/al/archive.pdf"
```

**Expected response:**
```json
{
  "id": "60d5ecb74e...",
  "filename": "archive.pdf",
  "markdown_content": "# Document Title\n\nExtracted content...",
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Evidence

### Run all tests:
```bash
uv run pytest
```

### Run with coverage:
```bash
uv run pytest --cov=app --cov-report=html
```

### Linting y type checking:
```bash
uv run ruff check .
uv run mypy app
```

## Methodology

### Test-Driven Development (TDD)

The project follows the Red-Green-Refactor cycle:

1. **Red**: Write tests that initially fail.
2. **Green**: Implement code to make the tests pass.
3. **Refactor**: Improve the code by keeping the tests green.

### Clean Code Principles

- Descriptive names that reflect the intent of the code.
- Single Responsibility Principle.
- DRY Principle.
- Small and organized functions.
- Code geared towards readability and maintainability.

## Programming Principles

| Principle | Description |
|-----------|-------------|
| **KISS** |  Prioritize simple solutions |
| **DRY** | Avoid code duplication |
| **YAGNI** | Do not implement premature features |
| **SOLID** | design rules to make it easier to understand, flexible and maintainable |

### Twelve-Factor App (Parcial)

- **Codebase**: A single versioned codebase.
- **Dependencies**: Declare and isolate the dependencies.
- **Config**: Save configuration in the environment.
- **Backing Services**: Services treated as pluggable resources.
- **Build, Release, Run**: Separate construction from execution.
- **Processes**: Execution as stateless processes.

## License

This project is licensed under the MIT License. See the `LICENSE.txt` file for more details.
