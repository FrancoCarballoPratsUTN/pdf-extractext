# PDF ExtractText

A REST API system that extracts text from PDF files and converts the content into text (.txt) format.

**Developers:** 
* Franco Carballo Prats - https://github.com/FrancoCarballoPratsUTN
* Daiana Macarena Michaux - https://github.com/Macamichaux

###### Current Status
This project is currently under development.

## Overview

PDF ExtractText is a REST API developed in Python that enables:

- **Uploading** PDF files via REST API
- **Extracting text** from PDF files using pypdf
- **Converting** extracted content into text (.txt) format
- **Validating** PDF files through multiple security checks
- **Auditing** all operations with an integrated audit log system

## Features

- PDF text extraction with pypdf
- Text file conversion
- REST API with FastAPI
- PDF security validations:
  - File type verification
  - File size validation (max 15MB)
  - PDF signature validation
  - Encryption detection
  - Liveness check
  - Trailer validation
- CRUD operations (Create, Read, Update, Delete)
- Audit logging for all document operations
- Standardized error responses using RFC 9457 (Problem Details)
- Test-Driven Development (TDD)
- Clean Architecture
- Clean code following SOLID principles

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14.4 |
| Framework | FastAPI |
| PDF Processing | pypdf |
| Dependency Management | UV |
| Testing | Pytest, Pytest-asyncio, httpx |
| Linting | Ruff |
| Type Checking | MyPy |
| Database | MongoDB (with mongomock for testing) |

### Main Dependencies

- **fastapi v0.135.3**: Modern and fast web framework
- **pydantic v2.13.1**: Data validation
- **pydantic-settings v2.13.1**: Settings management
- **uvicorn v0.44.0**: ASGI server
- **python-multipart v0.0.26**: Multipart file handling
- **pypdf v6.10.1**: PDF processing and text extraction
- **pymongo 4.17.0**: MongoDB database driver
- **python-dotenv v1.2.2**: Environment variable loading
- **python-json-logger v4.1.0**: JSON formatting for logs

### Development Dependencies

- **pytest v9.0.3**: Testing framework
- **pytest-asyncio v1.3.0**: Async support for pytest
- **pytest-cov v7.1.0**: Code coverage reports
- **httpx v0.27.0**: HTTP client for testing
- **ruff v0.6.0**: Code linting
- **mypy v1.11.0**: Static type checking
- **reportlab v4.4.10**: PDF generation for tests
- **mongomock v4.3.0**: MongoDB mock for testing

## Project Structure

```
pdf-extractext/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   └── settings.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   ├── audit_log.py
│   │   │   └── document.py
│   │   ├── exceptions/
│   │   │   └── domain_exceptions.py
│   │   ├── interfaces/
│   │   ├── contracts/
│   │   │   ├── __init__.py
│   │   │   └── document_converter.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── audit_log_repository.py
│   │   │   └── document_repository.py
│   │   ├── mappers/
│   │   │   └── to_dto.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       ├── checksum.py
│   │       ├── converter.py
│   │       ├── crud/
│   │       │   ├── delete_use_case.py
│   │       │   ├── find_use_case.py
│   │       │   ├── save_use_case.py
│   │       │   └── update_use_case.py
│   │       ├── flows/
│   │       │   ├── flow_building.py
│   │       │   └── flow_validation.py
│   │       ├── verifications/
│   │       │   ├── encryption_check.py
│   │       │   ├── file_only_has_images.py
│   │       │   ├── file_signature_validator.py
│   │       │   ├── file_size_validator.py
│   │       │   ├── liveness_check.py
│   │       │   ├── trailer_check.py
│   │       │   └── type_check.py
│   │       └── audit/
│   │           ├── audit_decorator.py
│   │           ├── find_audit_use_case.py
│   │           └── find_audit_by_checksum_use_case.py
│   ├── infrastructure/
│   │   ├── converters/
│   │   │   └── extract_text.py
│   │   ├── dependencies/
│   │   │   └── dependencies.py
│   │   └── persistence/
│   │       ├── database/
│   │       │   └── connection.py
│   │       └── repositories/
│   │           ├── __init__.py
│   │           ├── mongo_repository.py
│   │           └── mongo_audit_repository.py
│   └── presentation/
│       ├── __init__.py
│       ├── middleware/
│       │   ├── check_middleware.py
│       │   └── error_handler.py
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── audit_routes.py
│       │   ├── document_delete.py
│       │   ├── document_find_by_checksum.py
│       │   ├── document_save.py
│       │   ├── document_update.py
│       │   └── document_upload.py
│       └── schemas/
│           ├── __init__.py
│           ├── audit_log_response.py
│           ├── document.py
│           └── exception_response.py
├── docs/
│   └── diagrams/
│       ├── class_diagram/
│       │   ├── class_diagram_code.puml
│       │   └── document_class.png
│       ├── sequence_diagram/
│       │   ├── DS_delete.png
│       │   ├── DS_find.png
│       │   ├── DS_save.png
│       │   ├── DS_update.png
│       │   ├── DS_upload.png
│       │   └── sequence-diagrams_code.puml
│       └── use_case_diagram/
│           ├── use_case_code.puml
│           └── use_case.png
├── tests/
│   ├── conftest.py
│   ├── data/
│   │   ├── mock_repository.py
│   │   ├── test_delete.py
│   │   ├── test_find_by_checksum.py
│   │   ├── test_mongo_audit_repository.py
│   │   ├── test_save.py
│   │   └── test_update.py
│   ├── domain/
│   │   ├── mock_pdf.py
│   │   ├── test_audit_decorator.py
│   │   ├── test_checksum.py
│   │   ├── test_convert.py
│   │   ├── test_encryption_check.py
│   │   ├── test_file_only_has_images.py
│   │   ├── test_file_signature_validator.py
│   │   ├── test_file_size_validator.py
│   │   ├── test_find_audit_by_checksum_use_case.py
│   │   ├── test_find_audit_use_case.py
│   │   ├── test_liveness_check.py
│   │   └── test_trailer_check.py
│   └── presentation/
│       ├── test_audit_routes.py
│       ├── test_document_delete.py
│       ├── test_document_find_by_checksum.py
│       ├── test_document_save.py
│       ├── test_document_update.py
│       └── test_document_upload.py
├── .agents/
│   └── skills/
│       ├── tdd/
│       └── clean-code/
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── .python-version
├── compose.yaml
├── Dockerfile
├── LICENSE
├── plantuml.jar
├── pyproject.toml
├── README.Docker.md
├── README.md
├── skills-lock.json
└── uv.lock
```

### Layer Descriptions

- **`app/config/`**: Environment management (Settings based on `.env`)
- **`app/domain/`**: Core business logic (framework-agnostic)
  - **`entities/`**: Domain entities (`Document`, `AuditLog` dataclasses)
  - **`exceptions/`**: Custom errors following RFC 9457 (Problem Details)
  - **`contracts/`**: Contracts/ports for external dependencies (e.g., `Converter`)
  - **`repositories/`**: Repository interfaces (`DocumentRepository`, `AuditLogRepository`)
  - **`mappers/`**: DTO converters between dicts and domain entities
  - **`use_cases/`**: Application business rules
    - **`crud/`**: Basic database operations (save, find, update, delete)
    - **`flows/`**: Validation pipeline and document building flows
    - **`verifications/`**: PDF validation checks
    - **`audit/`**: Audit logging decorator and query use cases
- **`app/infrastructure/`**: External implementations
  - **`converters/`**: PDF to Text converter implementation (pypdf)
  - **`dependencies/`**: Use case dependency injection (including AuditDecorator)
  - **`persistence/`**: Database connections and repository implementations
    - **`database/`**: MongoDB connection
    - **`repositories/`**: MongoRepository and MongoAuditLogRepository
- **`app/presentation/`**: API layer
  - **`middleware/`**: Request validation middleware and global error handler
  - **`routes/`**: API endpoint definitions (documents + audit)
  - **`schemas/`**: Pydantic schemas for request/response validation
- **`tests/`**: Test suite by layer (unit + integration)
- **`docs/`**: Project documentation and UML diagrams (PlantUML + PNG)
- **`.agents/skills/`**: Agent skill definitions for TDD and Clean Code workflows

### Architecture (Clean Architecture)

```
┌────────────────────────────────────────────┐
│              PRESENTATION                  │
│  (Routes, Schemas, Middleware,             │
│   Error Handler)                           │
├────────────────────────────────────────────┤
│               DOMAIN                       │
│  (Entities, Interfaces, Use Cases,         │
│   Mappers, Verifications, Audit)           │
├────────────────────────────────────────────┤
│            INFRASTRUCTURE                  │
│  (Converters, Persistence,                 │
│   External Services)                       │
└────────────────────────────────────────────┘
```

### Design Patterns

| Pattern | Implementation |
|---------|---------------|
| **Decorator** | `AuditDecorator` transparently wraps use cases to add audit logging after each operation |
| **Repository** | Abstract interfaces (`DocumentRepository`, `AuditLogRepository`) with MongoDB implementations |
| **Pipeline / Chain of Responsibility** | `flow_validation.py` chains 5 sequential PDF verification checks |
| **DTO / Mapper** | `to_dto.py` converts between raw dicts (from MongoDB) and domain entities |
| **Dependency Injection** | FastAPI `Depends()` with factory functions in `dependencies.py` |
| **Singleton** | MongoDB connection managed as a module-level singleton (`mongo_connection`) |

## Documentation / Diagrams

The project includes UML diagrams generated with PlantUML located in `docs/diagrams/`:

| Diagram | Description | Source |
|---------|-------------|--------|
| Class Diagram | Entity and use case relationships | `docs/diagrams/class_diagram/class_diagram_code.puml` |
| Sequence Diagrams | Interaction flows for each CRUD operation | `docs/diagrams/sequence_diagram/sequence-diagrams_code.puml` |
| Use Case Diagram | System actors and use cases | `docs/diagrams/use_case_diagram/use_case_code.puml` |

To regenerate the diagrams, use:
```bash
java -jar plantuml.jar docs/diagrams/**/*.puml
```

## Database Schema

The application uses MongoDB with two collections:

### Collection: `file`

| Field | Type | Description |
|-------|------|-------------|
| `file_name` | string | Original PDF filename |
| `checksum` | string | SHA-256 hash of extracted text (unique index) |
| `text` | string | Extracted text content |
| `date` | datetime | UTC timestamp of creation |

A **unique index** on the `checksum` field is created automatically on first connection to prevent duplicate documents.

### Collection: `audit_logs`

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | Auto-generated MongoDB ID |
| `action` | string | One of: `save`, `update`, `delete`, `process` |
| `entity_type` | string | Always `Document` |
| `checksum` | string | The document's checksum |
| `details` | dict or null | Optional additional details |
| `performed_at` | datetime | UTC timestamp of the action |

## Requirements

### System Requirements

- **Operating System**: Cross-platform (Linux, Windows, macOS) — containerized via Docker
- **Python**: Version 3.14.4
- **UV**: Latest version (package manager)
- **MongoDB**: Required for document persistence (local or remote instance)
- **Docker** (optional): For containerized deployment

### Prerequisites

- Python 3.14.4
- UV (package manager and virtual environments)
- MongoDB instance (local or remote)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FrancoCarballoPratsUTN/pdf-extractext
   cd pdf-extractext
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB credentials
   ```

3. **Install dependencies with UV:**
   ```bash
   uv sync
   ```

4. **Install development dependencies:**
   ```bash
   uv sync --extra dev
   ```

## Environment Variables

All configuration is managed through environment variables defined in `.env`. Copy `.env.example` to `.env` and customize as needed:

| Variable | Default | Description |
|----------|---------|-------------|
| `MONGO_USER` | `user_name` | MongoDB authentication username |
| `MONGO_PASSWORD` | `user_password` | MongoDB authentication password |
| `MONGO_PORT` | `27017` | MongoDB port |
| `MONGO_HOST` | `localhost` | MongoDB host |
| `MONGO_CLIENT` | `mongo_client` | MongoDB database name |
| `MONGO_COLLECTION_FILE` | `file` | Collection name for documents |
| `MONGO_COLLECTION_AUDIT_LOGS` | `audit_logs` | Collection name for audit logs |
| `MAX_BYTES` | `15728640` (15 MB) | Maximum allowed file size in bytes |
| `MIN_BYTES` | `0` | Minimum allowed file size in bytes |
| `AUDIT_SAVE_ACTION` | `save` | Audit action label for save operations |
| `AUDIT_UPDATE_ACTION` | `update` | Audit action label for update operations |
| `AUDIT_DELETE_ACTION` | `delete` | Audit action label for delete operations |
| `AUDIT_PROCESS_ACTION` | `process` | Audit action label for process/upload operations |
| `AUDIT_ENTITY_TYPE` | `Document` | Entity type for audit logs |
| `LOG_LEVEL` | `INFO` | Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) |

## Running

**Development mode:**
```bash
uv run python app/main.py
```

**Production mode:**
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Docker mode:**

> **Prerequisite:** The `compose.yaml` uses an external Docker network named `mired`. Create it first if it doesn't exist:
> ```bash
> docker network create mired
> ```

```bash
docker compose up --build
```

> For Docker deployment details (multi-stage build, non-root user, healthcheck), see [`README.Docker.md`](README.Docker.md).

The API will be available at `http://localhost:8000`

**Interactive documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Usage

### Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| POST | `/upload` | Upload a PDF file and extract text | 201 Created |
| PUT | `/update/{checksum}` | Update a document by checksum | 200 OK |
| POST | `/save` | Create and register a new document | 201 Created |
| GET | `/find/{checksum}` | Find a document by checksum | 200 OK |
| DELETE | `/delete/{checksum}` | Delete a document by checksum | 200 OK |
| GET | `/audit/logs` | List all audit logs (paginated) | 200 OK |
| GET | `/audit/logs/checksum/{checksum}` | Find audit logs by document checksum | 200 OK |

### Upload Flow (Two-Step Design)

The upload process is split into two independent steps:

1. **`POST /upload`** — Validates the PDF (security checks), extracts text, and returns the result. **Does NOT persist** to the database.
2. **`POST /save`** — Takes the document data and persists it to MongoDB.

This design allows the client to review the extracted text before deciding to store it.

### Checksum

Documents are identified by a **SHA-256 checksum** computed from the **extracted text content** (not the raw PDF bytes). This means two different PDFs containing identical text will share the same checksum. The checksum serves as the unique identifier for all CRUD operations.

### Error Responses

All errors follow RFC 9457 (Problem Details) format:

```json
{
  "type": "/errors/not-found",
  "title": "Document Not Found",
  "status": 404,
  "detail": "The requested document does not exist.",
  "instance": "/find/nonexistent-checksum"
}
```

Standard error codes:

| Status | Title | Description |
|--------|-------|-------------|
| 400 | Invalid Document Data / Document Checksum Error | Invalid input or checksum mismatch |
| 404 | Document Not Found | No document matches the given checksum |
| 409 | Document Already Exists | A document with the same checksum already exists |
| 422 | Document Validation Error | The PDF failed security validation checks |
| 500 | Document Processing Error / Document Storage Error | Internal server or storage failure |

### Example Requests

**Upload a PDF file:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/document.pdf"
```

**Response** (201 Created):
```json
{
  "file_name": "document.pdf",
  "checksum": "a1b2c3d4e5f6...",
  "text": "Text extracted from PDF document...",
  "date": "2026-06-15T10:30:00"
}
```

**Update a document:**

```bash
curl -X PUT "http://localhost:8000/update/a1b2c3d4e5f6" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "new_name.pdf",
    "text": "new content updated"
  }'
```

**Response** (200 OK):
```json
{
  "file_name": "new_name.pdf",
  "text": "new content updated",
  "checksum": "a1b2c3d4e5f6",
  "date": "2026-06-15T10:30:00"
}
```

**Save a document:**

```bash
curl -X POST "http://localhost:8000/save" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "document.pdf",
    "checksum": "a1b2c3d4e5f6",
    "text": "full text extracted from the document",
    "date": "2026-06-15T10:30:00"
  }'
```

**Response** (201 Created):
```json
{
  "file_name": "document.pdf",
  "checksum": "a1b2c3d4e5f6",
  "text": "Full text extracted from the document",
  "date": "2026-06-15T10:30:00"
}
```

**Find a document:**

```bash
curl -X GET "http://localhost:8000/find/a1b2c3d4e5f6"
```

**Response** (200 OK):
```json
{
  "file_name": "document.pdf",
  "checksum": "a1b2c3d4e5f6",
  "text": "Full text extracted from the document",
  "date": "2026-06-15T10:30:00"
}
```

**Delete a document:**

```bash
curl -X DELETE "http://localhost:8000/delete/a1b2c3d4e5f6"
```

**Response** (200 OK):
```json
{
  "file_name": "document.pdf",
  "checksum": "a1b2c3d4e5f6",
  "text": "full text extracted from the document",
  "date": "2026-06-15T10:30:00"
}
```

**List audit logs:**

```bash
curl -X GET "http://localhost:8000/audit/logs?skip=0&limit=10"
```

**Response** (200 OK):
```json
[
  {
    "action": "save",
    "entity_type": "Document",
    "checksum": "a1b2c3d4e5f6",
    "details": null,
    "performed_at": "2026-06-15T10:30:00",
    "_id": "abc123def456"
  }
]
```

**Find audit logs by checksum:**

```bash
curl -X GET "http://localhost:8000/audit/logs/checksum/a1b2c3d4e5f6"
```

**Response** (200 OK):
```json
[
  {
    "action": "save",
    "entity_type": "Document",
    "checksum": "a1b2c3d4e5f6",
    "details": null,
    "performed_at": "2026-06-15T10:30:00",
    "_id": "abc123def456"
  }
]
```

### Validation Rules

- **File type**: Must be `application/pdf`
- **File size**: Maximum 15MB

### PDF Security Checks

The system performs the following validations on uploaded PDFs:

1. **Encryption Check**: Detects encrypted PDFs (rejected)
2. **File only has images**: The file only contains an image, no text
3. **Signature Validation**: Verifies the PDF file signature
4. **File size validator**: Maximum and minimum file size
5. **Liveness Check**: Ensures the PDF is not corrupted
6. **Trailer Check**: Validates the PDF trailer structure

## Testing

1. Open your terminal and navigate to the project folder.

2. Run all tests:
  ```bash
  uv run pytest
  ```
3. Run with coverage:
  ```bash
  uv run pytest --cov=app --cov-report=html
  ```

4. Run specific test file:
  ```bash
  uv run pytest tests/domain/test_convert.py
  ```

5. Linting:
  ```bash
  uv run ruff check .
  ```

6. Type checking:
  ```bash
  uv run mypy app
  ```

## Logging

The application uses **JSON-formatted structured logging** via `python-json-logger`. Logs are written to `stdout` in the following format:

```json
{"asctime": "2026-07-25 10:30:00,123", "name": "pdf-extractext", "levelname": "INFO", "message": "Connected to MongoDB successfully."}
```

The log level is configurable through the `LOG_LEVEL` environment variable (default: `INFO`).

## Tool Configuration

| Tool | Configuration |
|------|--------------|
| **Ruff** | Target: `py314`. Rules: `E`, `F`, `I`, `N`, `W`, `UP` |
| **Pytest** | `asyncio_mode = "auto"`, test paths: `tests/` |
| **Build System** | Hatchling (`hatchling.build`), packages: `app/` |

## Methodology

### Test-Driven Development (TDD)

The project follows the Red-Green-Refactor cycle:

1. **Red**: Write tests that initially fail
2. **Green**: Implement code to make the tests pass
3. **Refactor**: Improve code while keeping tests green

### Clean Code Principles

- Descriptive names that reflect intent
- Single Responsibility Principle
- DRY (Don't Repeat Yourself)
- Small and focused functions
- Code geared toward readability and maintainability

### Design Principles

| Principle | Description |
|-----------|-------------|
| **KISS** | Keep It Simple, Stupid |
| **DRY** | Don't Repeat Yourself |
| **YAGNI** | You Aren't Gonna Need It |
| **SOLID** | Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion |

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
