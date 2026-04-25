# PDF ExtractText

A REST API system that extracts text from PDF files and converts the content into Markdown (.md) format.

**Developers:** 
* Franco Carballo Prats - [https://github.com/FrancoCarballoPratsUTN]
* Michaux Daiana Macarena - [https://github.com/Macamichaux]

###### Current Status
This project is currently under development.

## Overview

PDF ExtractText is a REST API developed in Python that enables:

- **Uploading** PDF files via REST API
- **Extracting text** from PDF files using pypdf
- **Converting** extracted content into Markdown (.md) format
- **Validating** PDF files through multiple security checks

## Features

- PDF text extraction with pypdf
- Markdown file conversion
- REST API with FastAPI
- PDF security validations:
  - File type verification
  - File size validation (max 15MB)
  - PDF signature validation
  - Encryption detection
  - Liveness check
  - Trailer validation
- Test-Driven Development (TDD)
- Clean Architecture
- Clean code following SOLID principles

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14 |
| Framework | FastAPI |
| PDF Processing | pypdf |
| Dependency Management | UV |
| Testing | Pytest, Pytest-asyncio |
| Linting | Ruff |
| Type Checking | MyPy |

### Main Dependencies

- **fastapi**: Modern and fast web framework
- **pydantic**: Data validation
- **pydantic-settings**: Settings management
- **uvicorn**: ASGI server
- **python-multipart**: Multipart file handling
- **pypdf**: PDF processing and text extraction
- **pymongo**: MongoDB database driver
- **python-dotenv**: Environment variable loading

## Project Structure

```
pdf-extractext/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── document.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   └── document_converter.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── document_repository.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       ├── converter.py
│   │       ├── pipeline.py
│   │       └── verifications/
│   │           ├── encryptation_check.py
│   │           ├── file_signature_validator.py
│   │           ├── file_size_validator.py
│   │           ├── liveness_check.py
│   │           ├── trailer_check.py
│   │           └── type_check.py
│   ├── infrastructure/
│   │   ├── converters/
│   │   │   └── docling_md.py
│   │   └── persistence/
│   │       ├── database/
│   │       │   └── connection.py
│   │       └── repositories/
│   │           └── document_repository.py
│   └── presentation/
│       ├── __init__.py
│       ├── middleware/
│       │   └── check_middleware.py
│       ├── routes/
│       │   ├── __init__.py
│       │   └── document_upload.py
│       └── schemas/
│           ├── __init__.py
│           └── document_upload.py
├── tests/
│   ├── conftest.py
│   ├── data/
│   │   └── test_document_repository.py
│   ├── domain/
│   │   ├── mock_pdf.py
│   │   ├── test_convert.py
│   │   ├── test_encryptation_check.py
│   │   ├── test_file_signature_validator.py
│   │   ├── test_file_size_validator.py
│   │   ├── test_liveness_check.py
│   │   └── test_trailer_check.py
│   └── presentation/
│       └── test_routes.py
├── pyproject.toml
├── .python-version
├── .gitignore
└── README.md
```

### Layer Descriptions

- **`app/domain/`**: Core business logic (framework-agnostic)
  - **`entities/`**: Domain entities (Document dataclass)
  - **`interfaces/`**: Contracts/ports for external dependencies
  - **`repositories/`**: Repository interfaces
  - **`use_cases/`**: Application business rules
    - **`verifications/`**: PDF validation checks
- **`app/infrastructure/`**: External implementations
  - **`converters/`**: PDF to Markdown converter implementation
  - **`persistence/`**: Database connections and repository implementations
- **`app/presentation/`**: API layer
  - **`middleware/`**: Request/response middleware
  - **`routes/`**: API endpoint definitions
  - **`schemas/`**: Pydantic schemas for request/response validation
- **`tests/`**: Test suite

### Architecture (Clean Architecture)

```
┌─────────────────────────────────────────┐
│            PRESENTATION                 │
│   (Routes, Schemas, Middleware, API)    │
├─────────────────────────────────────────┤
│              DOMAIN                      │
│  (Entities, Interfaces, Use Cases,      │
│   Verifications)                         │
├─────────────────────────────────────────┤
│           INFRASTRUCTURE                 │
│  (Converters, Persistence, External     │
│   Services)                              │
└─────────────────────────────────────────┘
```

## Requirements

### System Requirements

- **Operating System**: Windows 10 or later, macOS, Linux
- **Python**: Version 3.14
- **UV**: Latest version (package manager)
- **MongoDB**: Required for document persistence (local or remote instance)

### Python Dependencies

All dependencies are managed via `pyproject.toml` and installed via UV. See the [Technology Stack](#technology-stack) section for more details.

### Prerequisites

- Python 3.14
- UV (package manager and virtual environments)

### Setup

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

## Running

**Development mode:**
```bash
uv run python app/main.py
```

**Production mode:**
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

**Interactive documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Usage

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload a PDF file and convert to Markdown |

### Example Request

**Uploading a PDF file:**
```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/document.pdf"
```

**Response:**
The API returns the extracted Markdown content as a string.

### Validation Rules

- **File type**: Must be `application/pdf`
- **File size**: Maximum 15MB

### PDF Security Checks

The system performs the following validations on uploaded PDFs:

1. **Signature Validation**: Verifies the PDF file signature
2. **Liveness Check**: Ensures the PDF is not corrupted
3. **Trailer Check**: Validates the PDF trailer structure
4. **Encryption Check**: Detects encrypted PDFs (rejected)

## Testing

### Run all tests:
```bash
uv run pytest
```

### Run with coverage:
```bash
uv run pytest --cov=app --cov-report=html
```

### Run specific test file:
```bash
uv run pytest tests/domain/test_convert.py
```

### Linting:
```bash
uv run ruff check .
```

### Type checking:
```bash
uv run mypy app
```

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
