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

- **fastapi v0.135.3**: Modern and fast web framework
- **pydantic v2.13.1**: Data validation
- **pydantic-settings v2.13.1**: Settings management
- **uvicorn v0.44.0**: ASGI server
- **python-multipart v0.0.26**: Multipart file handling
- **pypdf v6.10.1**: PDF processing and text extraction
- **pymongo 4.17.0**: MongoDB database driver
- **python-dotenv v1.2.2**: Environment variable loading

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
|   │   ├── exceptions/
│   │   │   └── domain_exceptions.py
│   │   ├── contracts/
│   │   │   ├── __init__.py
│   │   │   └── document_converter.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── document_repository.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       ├── checksum.py
│   │       ├── converter.py
│   │       ├── to_dto.py
│   │       ├── crud/
│   │       │   ├── delete_use_case.py
│   │       │   ├── find_use_case.py
│   │       │   ├── save_use_case.py
│   │       │   ├── update_use_case.py
│   │       ├── flows/
│   │       │   ├── flow_building.py
│   │       │   ├── flow_validation.py
│   │       └── verifications/
│   │           ├── encryptation_check.py
│   │           ├── file_only_has_imagen.py
│   │           ├── file_signature_validator.py
│   │           ├── file_size_validator.py
│   │           ├── liveness_check.py
│   │           ├── trailer_check.py
│   │           └── type_check.py
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
│   │           └── mongo_repository.py
│   └── presentation/
│       ├── __init__.py
│       ├── middleware/
│       │   └── check_middleware.py
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── document_delete.py
│       │   ├── document_find_by_checksum.py
│       │   ├── documet_save.py
│       │   ├── document_update.py
│       │   └── document_upload.py
│       └── schemas/
│           ├── __init__.py
│           └── document.py
├── tests/
│   ├── conftest.py
│   ├── data/
│   │   ├── mock_repository.py
│   │   ├── test_delete.py
│   │   ├── test_find_by_checksum.py
│   │   ├── test_save.py
│   │   ├── test_update.py
│   ├── domain/
│   │   ├── mock_pdf.py
│   │   ├── test_checksum.py
│   │   ├── test_convert.py
│   │   ├── test_encryptation_check.py
│   │   ├── test_file_only_has_imagen.py
│   │   ├── test_file_signature_validator.py
│   │   ├── test_file_size_validator.py
│   │   ├── test_liveness_check.py
│   │   └── test_trailer_check.py
│   └── presentation/
│       ├── test_document_delete.py
│       ├── test_document_find_by_checksum.py
│       ├── test_document_save.py
│       ├── test_document_update.py
│       ├── test_document_upload.py
├── pyproject.toml
├── .python-version
├── .gitignore
└── README.md
```

### Layer Descriptions
- **`app/config/`**: Environment management 
- **`app/domain/`**: Core business logic (framework-agnostic)
  - **`entities/`**: Domain entities (Document dataclass)
  - **`exceptions/`**: Define custom errors
  - **`contracts/`**: Contracts/ports for external dependencies
  - **`repositories/`**: Repository interfaces
  - **`use_cases/`**: Application business rules
    - **`crud/`**: Basic database operations
    - **`flows/`**: Controls the validation flow and the building flows
    - **`verifications/`**: PDF validation checks
- **`app/infrastructure/`**: External implementations
  - **`converters/`**: PDF to Text converter implementation
  - **`dependencies/`**: Use case dependencies
  - **`persistence/`**: Database connections and repository implementations
    - **`datebase/`**: Database connection
    - **`repositories/`**: Manages the MongoDB repository
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
│              DOMAIN                     │
│  (Entities, Interfaces, Use Cases,      │
│   Verifications)                        │
├─────────────────────────────────────────┤
│           INFRASTRUCTURE                │
│  (Converters, Persistence, External     │
│   Services)                             │
└─────────────────────────────────────────┘
```

## Requirements

### System Requirements

- **Operating System**: Windows 11
- **Python**: Version 3.14
- **UV**: Latest version (package manager)
- **MongoDB**: Required for document persistence (local or remote instance)

### Python Dependencies

All dependencies are managed via `pyproject.toml` and installed via UV.

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
| POST | `/upload` | Upload a PDF file and convert to text |
| PUT | `/update` | Update a document |
| POST | `/save` | Create and register a new document |
| GET | `/find` | Consult a document |
| DELETE | `/delete` | Delete a document |


### Example Request

**Upload a PDF file:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/document.pdf"
```

**Response**:
```
{
  "file_name": "document.pdf",
  "checksum": "(code (combination of numbers and letters))",
  "text": "Text extracted from PDF document...",
  "date": "YYYY-MM-DDTHH:mm:ss"
}
```

**Update a PDF file:**

```bash
curl -X PUT "http://localhost:8000/update/{checksum}" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "new_name.pdf",
    "text": "new content updated"
  }'
```

**Response**
```
{
  "file_name": "new_name.pdf",
  "text": "new content updated",
  "checksum": "(code (combination of numbers and letters))",
  "date": ""YYYY-MM-DDTHH:mm:ss"
}
```

**Save a PDF file:**

```bash
curl -X POST "http://localhost:8000/save" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "document.pdf",
    "checksum": "{checksum}",
    "text": "full text extracted from the document",
    "date": "YYYY-MM-DDTHH:mm:ss"
  }'
```

**Response**
```
{
  "file_name": "document.pdf",
  "checksum": "(code (combination of numbers and letters))",
  "text": "Full text extracted from the document",
  "date": "YYYY-MM-DDTHH:mm:ss"
}
```

**Find a PDF file:**

```bash
curl -X GET "http://localhost:8000/find/{checksum}"
```
**Response**
```
{
  "file_name": "document.pdf",
  "checksum": "(code (combination of numbers and letters))",
  "text": "Full text extracted from the document",
  "date": "YYYY-MM-DDTHH:mm:ss"
}
```

**Delete a PDF file:**

```bash
curl -X DELETE "http://localhost:8000/delete/{checksum}"
```
**Response**:
```
{
  "file_name": "document.pdf",
  "checksum": "(code (combination of numbers and letters))",
  "text": "full text extracted from the document",
  "date": "YYYY-MM-DDTHH:mm:ss"
}
```
### Validation Rules

- **File type**: Must be `application/pdf`
- **File size**: Maximum 15MB

### PDF Security Checks

The system performs the following validations on uploaded PDFs:

1. **Encryption Check**: Detects encrypted PDFs (rejected)
2. **File only has imagen**: The file only contains an image, no text
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
